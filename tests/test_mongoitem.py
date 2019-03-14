import os
import unittest

from faker import Faker

from mongoengine import connect

from scrapy import Field
from scrapy_mongoengine_item import MongoEngineItem
from tests.documents import Person, IdentifiedPerson

__all__ = (
    'MongoEngineItemTest',
)

connect()


class BasePersonItem(MongoEngineItem):

    mongoengine_document = Person


class NewFieldPersonItem(BasePersonItem):

    other = Field()


class OverrideFieldPersonItem(BasePersonItem):

    age = Field()


class IdentifiedPersonItem(MongoEngineItem):

    mongoengine_document = IdentifiedPerson


class MongoEngineItemTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.faker = Faker()

    def assertSortedEqual(self, first, second, msg=None):
        return self.assertEqual(sorted(first), sorted(second), msg)

    def test_base(self):
        i = BasePersonItem()
        self.assertSortedEqual(i.fields.keys(), ['age', 'name'])

    def test_new_fields(self):
        i = NewFieldPersonItem()
        self.assertSortedEqual(i.fields.keys(), ['age', 'other', 'name'])

    def test_override_field(self):
        i = OverrideFieldPersonItem()
        self.assertSortedEqual(i.fields.keys(), ['age', 'name'])

    def test_custom_primary_key_field(self):
        """
        Test that if a custom primary key exists, it is
        in the field list.
        """
        i = IdentifiedPersonItem()
        self.assertSortedEqual(i.fields.keys(), ['age', 'identifier', 'name'])

    def test_save(self):
        i = BasePersonItem()
        self.assertSortedEqual(i.fields.keys(), ['age', 'name'])

        i['name'] = self.faker.name()
        i['age'] = self.faker.pyint()
        person = i.save(commit=False)

        self.assertEqual(person.name, i['name'])
        self.assertEqual(person.age, i['age'])

    def test_save_commit(self):
        i = BasePersonItem()
        self.assertSortedEqual(i.fields.keys(), ['age', 'name'])

        i['name'] = self.faker.name()
        i['age'] = self.faker.pyint()
        person = i.save()

        self.assertEqual(person.name, i['name'])
        self.assertEqual(person.age, i['age'])

    def test_override_save(self):
        i = OverrideFieldPersonItem()

        i['name'] = self.faker.name()
        # it is not obvious that "age" should be saved also, since it was
        # redefined in child class
        i['age'] = self.faker.pyint()
        person = i.save(commit=False)

        self.assertEqual(person.name, i['name'])
        self.assertEqual(person.age, i['age'])

    def test_validation(self):
        long_name = 'z' * 300
        name = self.faker.name()
        i = BasePersonItem(name=long_name)
        self.assertFalse(i.is_valid())
        self.assertEqual(set(i.errors), {'age', 'name'})
        i = BasePersonItem(name=name)
        self.assertTrue(i.is_valid())
        self.assertEqual({}, i.errors)

        # once the item is validated, it does not validate again
        i['name'] = long_name
        self.assertTrue(i.is_valid())

    def test_override_validation(self):
        i = OverrideFieldPersonItem()
        i['name'] = self.faker.name()
        self.assertFalse(i.is_valid())

        i = i = OverrideFieldPersonItem()
        i['name'] = self.faker.name()
        i['age'] = self.faker.pyint()
        self.assertTrue(i.is_valid())

    def test_default_field_values(self):
        i = BasePersonItem()
        person = i.save(commit=False)
        self.assertEqual(person.name, 'Robot')


if __name__ == '__main__':
    unittest.main()
