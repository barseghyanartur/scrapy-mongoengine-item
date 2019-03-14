#!/usr/bin/env bash
pip uninstall scrapy-mongoengine-item -y
rm build -rf
rm dist -rf
rm -rf src/scrapy_mongoengine_item.egg-info
rm -rf src/scrapy-mongoengine-item.egg-info
rm builddocs.zip
rm builddocs/ -rf
