from mongoengine import *

connect(host="mongodb+srv://user:567234@mongodb.x4pxdoh.mongodb.net/web9", ssl=True)


class Contacts(Document):
    fullname = StringField(max_length=500)
    email = StringField(max_length=500)
    sent = BooleanField(default=False)


