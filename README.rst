=======================
scrapy-mongoengine-item
=======================

.. image:: https://img.shields.io/pypi/v/scrapy-mongoengine-item.svg
   :target: https://pypi.python.org/pypi/scrapy-mongoengine-item
   :alt: PyPI Version

.. image:: https://img.shields.io/travis/barseghyanartur/scrapy-djangoitem/master.svg
   :target: http://travis-ci.org/barseghyanartur/scrapy-mongoengine-item
   :alt: Build Status

.. image:: https://img.shields.io/github/license/barseghyanartur/scrapy-mongoengine-item.svg
   :target: https://github.com/barseghyanartur/scrapy-mongoengine-item/blob/master/LICENSE
   :alt: License


``scrapy-mongoengine-item`` is an extension that allows you to define `Scrapy items
<http://doc.scrapy.org/en/latest/topics/items.html>`_ using existing
`MongoEngine documents <http://docs.mongoengine.org/guide/defining-documents.html>`_.

This utility provides a new class, named ``DjangoItem``, that you can use as a
regular Scrapy item and link it to a Django model with its ``django_model``
attribute. Start using it right away by importing it from this package::

    from scrapy_mongoengine_item import MongoEngineItem

Installation
============

Starting with ``v1.1`` both ``Python 2.7`` and ``Python 3.5/3.6`` are
supported. For ``Python 3`` you need ``Scrapy v1.1`` or above.

Latest tested MongoEngine version is ``MongoEngine 0.17.0``.

Install from ``PyPI`` using::

  pip install scrapy-mongoengine-item


Introduction
============

``MongoEngineItem`` is a class of item that gets its fields definition from a
MongoEngine document, you simply create a ``MongoEngineItem`` and specify what
MongoEngine document it relates to.

Besides of getting the document fields defined on your item, ``MongoEngineItem``
provides a method to create and populate a MongoEngine document instance with
the item data.

Usage
=====

``MongoEngineItem`` works as follows: you create a subclass and define its
``mongoengine_document`` attribute to be a valid MongoEngine document. With
this you will get an item with a field for each MongoEngine document field.

In addition, you can define fields that aren't present in the document and even
override fields that are present in the model defining them in the item.

Let's see some examples:

Creating a Django model for the examples::

    from mongoengine import fields, document

    class Person(document.Document):
        name = fields.CharField(max_length=255)
        age = fields.IntegerField()

Defining a basic ``MongoEngineItem``::

    from scrapy_mongoengine_item import MongoEngineItem

    class PersonItem(MongoEngineItem):
        mongoengine_document = Person

``MongoEngineItem`` works just like Scrapy items::

    >>> p = PersonItem()
    >>> p['name'] = 'John'
    >>> p['age'] = '22'

To obtain the MongoEngine document from the item, we call the extra method
``MongoEngineItem.save()`` of the ``MongoEngineItem``::

    >>> person = p.save()
    >>> person.name
    'John'
    >>> person.age
    '22'
    >>> person.id
    1

The document is already saved when we call ``MongoEngineItem.save()``, we
can prevent this by calling it with ``commit=False``. We can use
``commit=False`` in ``MongoEngineItem.save()`` method to obtain an unsaved
document::

    >>> person = p.save(commit=False)
    >>> person.name
    'John'
    >>> person.age
    '22'
    >>> person.id
    None

As said before, we can add other fields to the item::

    import scrapy
    from scrapy_mongoengine_item import MongoEngineItem

    class PersonItem(MongoEngineItem):
        mongoengine_document = Person
        sex = scrapy.Field()

::

   >>> p = PersonItem()
   >>> p['name'] = 'John'
   >>> p['age'] = '22'
   >>> p['sex'] = 'M'

And we can override the fields of the document with your own::

    class PersonItem(MongoEngineItem):
        mongoengine_document = Person
        name = scrapy.Field(default='No Name')

This is useful to provide properties to the field, like a default or any other
property that your project uses. Those additional fields won't be taken into
account when doing a ``MongoEngineItem.save()``.

Development
===========

Test suite from the ``tests`` directory can be run using ``tox`` by running::

  tox

...using the configuration in ``tox.ini``. The ``Python`` interpreters
used have to be installed locally on the system.
