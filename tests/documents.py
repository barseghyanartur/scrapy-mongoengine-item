from mongoengine import fields, document

__all__ = (
    'IdentifiedPerson',
    'Person',
)


class Person(document.Document):

    name = fields.StringField(required=True, max_length=255, default='Robot')
    age = fields.IntField(required=True)

    def __str__(self):
        return self.name


class IdentifiedPerson(document.Document):

    identifier = fields.IntField(required=True, primary_key=True)
    name = fields.StringField(required=True, max_length=255)
    age = fields.IntField(required=True)

    def __str__(self):
        return self.name
