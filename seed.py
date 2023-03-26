from faker import Faker
from model import Contacts


def create_contacts(numbers_contacts):
    Contacts.drop_collection()
    faker = Faker()

    gen_contacts = []

    for _ in range(numbers_contacts):
        new_contact = Contacts(fullname=faker.name())
        new_contact.email = faker.email()
        new_contact.save()

        gen_contacts.append(new_contact)

    return gen_contacts


def get_contact_ids(contacts: list[Contacts]):
    return [contact.id for contact in contacts]
