#!/usr/bin/env python
import os
import sys


def main():
    sys.path.insert(0, os.path.abspath('.'))
    from IPython import start_ipython
    from mongoengine import connect
    connect()
    start_ipython(argv=[])


if __name__ == '__main__':
    sys.exit(main())
