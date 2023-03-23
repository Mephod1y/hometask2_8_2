import pika
import time
import json
from pymongo import MongoClient

client = MongoClient("mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9")
db = client.web9

credentials = pika.PlainCredentials('nxivztju','Y-QORi4RdYBDdZpu4hx-c9D7QPEHAKUL')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com',port=5672, virtual_host='nxivztju',credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print(' [*] Waiting for messages. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(f"{ch}, {method}, {properties}, {body}")
    message = json.loads(body.decode())
    print(f" [x] Received {message}")
    time.sleep(1)

    сontacts = db.contacts.find()
    for c in сontacts:
        if c['_id'] == message['id']:
            print(message['id'])
            c.logical = 'True'
            с.save()

    print(f" [x] Done: {method.delivery_tag}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)


if __name__ == '__main__':
    channel.start_consuming()