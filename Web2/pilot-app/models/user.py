from mongoengine import *
import mlab


class Uervice(Document):
    fullname = StringField()
    email = StringField()
    Username = StringField()
    password = StringField()
    
