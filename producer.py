import pika
import json
from model import upload_data
from pymongo import MongoClient

client = MongoClient("mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9")
db = client.web9

credentials = pika.PlainCredentials('nxivztju', 'Y-QORi4RdYBDdZpu4hx-c9D7QPEHAKUL')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, virtual_host='nxivztju',
                              credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='task_mock', exchange_type='direct')
channel.queue_declare(queue='task_queue', durable=True)
channel.queue_bind(exchange='task_mock', queue='task_queue')


def main():
    # upload_data()
    contacts = db.contacts.find()
    for c in contacts:
        message = {
            "Send": f"Mail for {c['fullname']} {c['email']}",
            "id": f"{c['_id']}",
        }

        channel.basic_publish(
            exchange='task_mock',
            routing_key='task_queue',
            body=json.dumps(message).encode(),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(message)
    connection.close()


if __name__ == '__main__':
    main()
