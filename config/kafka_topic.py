from kafka.admin import KafkaAdminClient, NewTopic

# Connect to Kafka broker (inside Docker, use broker container hostname and port)
admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:9092",  # Docker Kafka container hostname and port
    client_id='admin'
)

# Define a new topic
topic_list = [
    NewTopic(
        name="sensor-topic",      # Topic name
        num_partitions=1,         # Number of partitions
        replication_factor=1      # Replication factor
    )
]

# Create topic
try:
    admin_client.create_topics(new_topics=topic_list, validate_only=False)
    print("Topic 'sensor-topic' created successfully!")
except Exception as e:
    print(f"Error creating topic: {e}")

admin_client.close()
