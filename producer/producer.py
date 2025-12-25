from kafka import KafkaProducer
import json
import time
import csv

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

with open(r"sensor_data.csv") as f:
    reader = csv.DictReader(f)  # Automatically parses CSV headers
    for row in reader:
        # Convert temperature to float for numeric aggregation in Spark
        #row["temperature"] = float(row["temperature"])
        producer.send("sensor-topic", row)
        print(f"Sent: {row}")
        time.sleep(1)  # Adjust for near real-time simulation

producer.flush()
producer.close()
