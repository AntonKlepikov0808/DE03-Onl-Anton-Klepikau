# consumer_to_raw.py
import json
from kafka import KafkaConsumer
import psycopg2
import logging

logging.basicConfig(level=logging.INFO)

# Kafka consumer
consumer = KafkaConsumer(
    'pharmacy_prices',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# PostgreSQL connection
conn = psycopg2.connect(
    host='localhost',
    database='pharmacy_prices',
    user='postgres',
    password='postgres'
)
cur = conn.cursor()

for message in consumer:
    data = message.value
    try:
        cur.execute(
            "INSERT INTO raw_data (data, source) VALUES (%s, %s)",
            (json.dumps(data), 'kafka')
        )
        conn.commit()
        logging.info(f"Inserted: {data}")
    except Exception as e:
        logging.error(f"Error: {e}")
        conn.rollback()