import pika
from time import sleep
from pymongo import MongoClient
from model import Contacts

client = MongoClient("mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9")
db = client.web9


def main():
    credentials = pika.PlainCredentials('nxivztju', 'Y-QORi4RdYBDdZpu4hx-c9D7QPEHAKUL')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, virtual_host='nxivztju',
                                  credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue="send_message")

    def callback(ch, method, properties, body):
        contacts = Contacts.objects()
        contact_id = body.decode()
        contact_email = contacts(id=contact_id)[0].email
        sleep(1)
        print(f" [x] Sent message to email: '{contact_email}' with id: {contact_id}")
        contacts(id=contact_id)[0].update(sent=True)

    channel.basic_consume(queue='send_message', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for user identifiers. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    main()
