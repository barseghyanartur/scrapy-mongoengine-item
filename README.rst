=======================
scrapy-mongoengine-item
=======================
Bringing ``Scrapy`` and ``MongoEngine`` together.

.. image:: https://img.shields.io/pypi/v/scrapy-mongoengine-item.svg
   :target: https://pypi.python.org/pypi/scrapy-mongoengine-item
   :alt: PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/scrapy-mongoengine-item.svg
    :target: https://pypi.python.org/pypi/scrapy-mongoengine-item/
    :alt: Supported Python versions

.. image:: https://img.shields.io/travis/barseghyanartur/scrapy-mongoengine-item/master.svg
   :target: http://travis-ci.org/barseghyanartur/scrapy-mongoengine-item
   :alt: Build Status

.. image:: https://img.shields.io/badge/license-GPL--2.0--only%20OR%20LGPL--2.1--or--later-blue.svg
   :target: https://github.com/barseghyanartur/scrapy-mongoengine-item/#License
   :alt: GPL-2.0-only OR LGPL-2.1-or-later

.. image:: https://coveralls.io/repos/github/barseghyanartur/scrapy-mongoengine-item/badge.svg?branch=master
    :target: https://coveralls.io/github/barseghyanartur/scrapy-mongoengine-item?branch=master
    :alt: Coverage

``scrapy-mongoengine-item`` is an extension that allows you to define `Scrapy items
<http://doc.scrapy.org/en/latest/topics/items.html>`_ using existing
`MongoEngine documents <http://docs.mongoengine.org/guide/defining-documents.html>`_.

Documentation is available on `Read the Docs
<http://scrapy-mongoengine-item.readthedocs.io/>`_.

Prerequisites
=============
Both ``Python 2.7`` and ``Python 3.5/3.6`` are
supported. For ``Python 3`` you need ``Scrapy v1.1`` or above.

Latest tested MongoEngine version is ``MongoEngine 0.17.0``.

Installation
============
(1) Install latest stable version from PyPI:

    .. code-block:: sh

        pip install scrapy-mongoengine-item

    or latest stable version from GitHub:

    .. code-block:: sh

        pip install https://github.com/barseghyanartur/scrapy-mongoengine-item/archive/stable.tar.gz

    or latest stable version from BitBucket:

    .. code-block:: sh

        pip install https://bitbucket.org/barseghyanartur/scrapy-mongoengine-item/get/stable.tar.gz

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

Creating a MongoEngine document for the examples:

.. code-block:: python

    from mongoengine import fields, document

    class Person(document.Document):

        name = fields.StringField(max_length=255)
        age = fields.IntField()

Defining a basic ``MongoEngineItem``:

.. code-block:: python

    from scrapy_mongoengine_item import MongoEngineItem

    class PersonItem(MongoEngineItem):

        mongoengine_document = Person

``MongoEngineItem`` works just like Scrapy items:

.. code-block:: python

    p = PersonItem()
    p['name'] = 'John'
    p['age'] = 22

To obtain the MongoEngine document from the item, we call the extra method
``MongoEngineItem.save()`` of the ``MongoEngineItem``:

.. code-block:: python

    person = p.save()
    person.name
    # 'John'
    person.age
    # 22
    person.id
    # 1

The document is already saved when we call ``MongoEngineItem.save()``, we
can prevent this by calling it with ``commit=False``. We can use
``commit=False`` in ``MongoEngineItem.save()`` method to obtain an unsaved
document:

.. code-block:: python

    person = p.save(commit=False)
    person.name
    # 'John'
    person.age
    # 22
    person.id
    # None

As said before, we can add other fields to the item:

.. code-block:: python

    import scrapy
    from scrapy_mongoengine_item import MongoEngineItem

    class PersonItem(MongoEngineItem):

        mongoengine_document = Person
        sex = scrapy.Field()

.. code-block:: python

   p = PersonItem()
   p['name'] = 'John'
   p['age'] = 22
   p['sex'] = 'M'

And we can override the fields of the document with your own:

.. code-block:: python

    class PersonItem(MongoEngineItem):

        mongoengine_document = Person
        name = scrapy.Field(default='No Name')

This is useful to provide properties to the field, like a default or any other
property that your project uses. Those additional fields won't be taken into
account when doing a ``MongoEngineItem.save()``.

Development
===========
Testing
-------
To run tests in your working environment type:

.. code-block:: sh

    ./runtests.py

To test with all supported Python versions type:

.. code-block:: sh

    tox

Running MongoDB
---------------
The easiest way is to run it via Docker:

.. code-block:: sh

    docker pull mongo:latest
    docker run -p 27017:27017 mongo:latest

Writing documentation
---------------------
Keep the following hierarchy.

.. code-block:: text

    =====
    title
    =====

    header
    ======

    sub-header
    ----------

    sub-sub-header
    ~~~~~~~~~~~~~~

    sub-sub-sub-header
    ^^^^^^^^^^^^^^^^^^

    sub-sub-sub-sub-header
    ++++++++++++++++++++++

    sub-sub-sub-sub-sub-header
    **************************

License
=======
GPL-2.0-only OR LGPL-2.1-or-later

Support
=======
For any issues contact me at the e-mail given in the `Author`_ section.

Author
======
Artur Barseghyan <artur.barseghyan@gmail.com>
