from mongoengine import connect
from mongoengine import fields, document

connect()


class Person(document.Document):
    name = fields.StringField(required=True, max_length=255, default='Robot')
    age = fields.IntField(required=True)


class IdentifiedPerson(document.Document):
    identifier = fields.IntField(required=True, primary_key=True)
    name = fields.StringField(required=True, max_length=255)
    age = fields.IntField(required=True)
