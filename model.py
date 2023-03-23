from mongoengine import *
from faker import Faker

connect(host="mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9", ssl=True)


class Contacts(Document):
    fullname = StringField(max_length=500)
    email = StringField(max_length=500)
    logical = StringField('False')


NUMBERS_CONTACTS = 5
fake = Faker()


def create_contacts():
    contacts = [{'fullname': fake.name(), 'email': fake.email(), 'logical': 'False'} for i in range(NUMBERS_CONTACTS)]
    return contacts


def upload_data():
    contacts = create_contacts()
    for c in contacts:
        contact = Contacts()
        contact.fullname = c['fullname']
        contact.email = c['email']
        contact.logical = c['logical']
        contact.save()


if __name__ == '__main__':
    upload_data()
