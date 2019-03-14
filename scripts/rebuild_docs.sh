#!/usr/bin/env bash
rm docs/scrapy_mongoengine_item*.rst
rm -rf builddocs/
sphinx-apidoc scrapy_mongoengine_item --full -o docs -H 'scrapy-mongoengine-item' -A 'Artur Barseghyan <artur.barseghyan@gmail.com>' -V '0.1' -f -d 20
cp docs/conf.py.distrib docs/conf.py

./scripts/build_docs.sh
