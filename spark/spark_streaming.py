from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, get_json_object, col

# Spark session
spark = SparkSession.builder.appName("KafkaTemperatureStreaming").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# Kafka configurations
kafka_bootstrap_servers = "kafka:29092"
kafka_topic = "sensor-topic"

# Read from Kafka
df = (
    spark.readStream.format("kafka")
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers)
    .option("subscribe", kafka_topic)
    .load()
)

# Convert Kafka 'value' to string
sensor_data = df.selectExpr("CAST(value AS STRING) as sensor_json")

# Parse JSON fields
parsed_data = sensor_data.select(
    get_json_object(col("sensor_json"), "$.sensor_id").alias("sensor_id"),
    get_json_object(col("sensor_json"), "$.temperature").alias("temperature")
)

# Convert temperature to float
parsed_data = parsed_data.withColumn("temperature", col("temperature").cast("float"))

# Compute average temperature per sensor
average_temperature = parsed_data.groupBy("sensor_id").agg(expr("avg(temperature) as avg_temperature"))

# Output to console
query = (
    average_temperature.writeStream
    .outputMode("complete")
    .format("console")
    .option("truncate", False)
    .start()
)

query.awaitTermination()
