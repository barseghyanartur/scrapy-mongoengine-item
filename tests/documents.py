from mongoengine import connect
from mongoengine import fields, document

connect()


class Person(document.Document):
    name = fields.StringField(max_length=255, default='Robot')
    age = fields.IntField()


class IdentifiedPerson(document.Document):
    identifier = fields.IntField(primary_key=True)
    name = fields.StringField(max_length=255)
    age = fields.IntField()
