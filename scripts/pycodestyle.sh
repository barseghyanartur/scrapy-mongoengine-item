#!/usr/bin/env bash
reset
pycodestyle src/django_elasticsearch_dsl_drf/ --exclude migrations,south_migrations
