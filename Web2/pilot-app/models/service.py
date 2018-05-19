from mongoengine import *
import mlab


class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField ()
    phone = StringField()
    address = StringField()
    status = BooleanField ()
