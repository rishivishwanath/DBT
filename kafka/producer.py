from kafka import KafkaProducer
import csv
import time
import json

# Kafka config
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'deliveries_raw'
csv_file_path = '../data/ipl_2022_deliveries.csv'

with open(csv_file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        producer.send(topic_name, value=row)
        print(f"Sent: {row}")
        time.sleep(0.5)  # simulate streaming

