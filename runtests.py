#!/usr/bin/env python
import sys

import pytest


def main():
    sys.path.insert(0, ".")
    return pytest.main()


if __name__ == '__main__':
    sys.exit(main())
