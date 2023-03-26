import pika
from model import Contacts
from seed import create_contacts, get_contact_ids
from pymongo import MongoClient


client = MongoClient("mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9")
db = client.web9


def main(contacts: list[Contacts]):
    credentials = pika.PlainCredentials('nxivztju', 'Y-QORi4RdYBDdZpu4hx-c9D7QPEHAKUL')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='sparrow-01.rmq.cloudamqp.com', port=5672, virtual_host='nxivztju',
                                  credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue="send_message")

    for id in get_contact_ids(contacts):
        channel.basic_publish(exchange='', routing_key='send_message', body=str(id))
        print(f" [x] Sent email to id: {id}")

    connection.close()


if __name__ == '__main__':
    contacts = create_contacts(5)
    main(contacts)
