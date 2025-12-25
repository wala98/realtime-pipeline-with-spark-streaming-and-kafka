# Real-time Temperature Pipeline

A simple end-to-end real-time pipeline that publishes sensor temperature events to Kafka and computes per-sensor average temperature using Spark Structured Streaming.

## Contents
- [docker-compose.yml](docker-compose.yml) — Kafka & Zookeeper setup
- [config/kafka_topic.py](config/kafka_topic.py) — topic creation helper
- [producer/producer.py](producer/producer.py) — reads `producer/sensor_data.csv` and publishes to Kafka
- [producer/requirements.txt](producer/requirements.txt) — producer dependencies
- [producer/sensor_data.csv](producer/sensor_data.csv) — sample sensor events
- [spark/spark_streaming.py](spark/spark_streaming.py) — Spark Structured Streaming job

## Prerequisites
- Docker & Docker Compose (for Kafka)
- Java JDK 8+ (for Spark)
- Python 3.8+
- Spark (or use `spark-submit` on a machine with Spark installed)
- Install Python deps listed in `producer/requirements.txt` and `pyspark` if running locally

## Quick Setup

1. Install Python deps:
```bash
python -m pip install -r [requirements.txt](http://_vscodecontentref_/3)
python -m pip install pyspark