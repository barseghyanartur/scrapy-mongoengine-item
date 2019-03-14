import copy
from six import with_metaclass
from mongoengine.errors import ValidationError
from scrapy.item import Field, Item, ItemMeta


__all__ = (
    'MongoEngineItem',
)


class MongoEngineItemMeta(ItemMeta):

    def __new__(mcs, class_name, bases, attrs):
        cls = super(MongoEngineItemMeta, mcs).__new__(
            mcs,
            class_name,
            bases,
            attrs
        )
        cls.fields = cls.fields.copy()

        if cls.mongoengine_document:
            cls._document_fields = []
            cls._document_meta = cls.mongoengine_document._meta
            for document_field in cls.mongoengine_document._fields:
                if document_field.name != cls._document_meta['id_field']:
                    cls.fields[document_field.name] = Field()
                cls._model_fields.append(document_field.name)
        return cls


class MongoEngineItem(with_metaclass(MongoEngineItemMeta, Item)):

    mongoengine_document = None

    def __init__(self, *args, **kwargs):
        super(MongoEngineItem, self).__init__(*args, **kwargs)
        self._instance = None
        self._errors = None

    def save(self, commit=True):
        if commit:
            self.instance.save()
        return self.instance

    def is_valid(self):
        self._get_errors()
        return not bool(self._errors)

    def _get_errors(self):
        if self._errors is not None:
            return self._errors

        self._errors = {}

        try:
            self.instance.validate()
        except ValidationError as err:
            self._errors = self._errors.update(copy.copy(err.errors))

        try:
            self.instance.clean()
        except ValidationError as err:
            self._errors = self._errors.update(copy.copy(err.errors))

        # uniqueness is not checked, because it is faster to check it when
        # saving object to database. Just beware, that failed save()
        # raises IntegrityError instead of ValidationError.

        return self._errors
    errors = property(_get_errors)

    @property
    def instance(self):
        if self._instance is None:
            document_args = dict(
                (k, self.get(k))
                for k in self._values
                if k in self._model_fields
            )
            self._instance = self.mongoengine_document(**document_args)
        return self._instance
