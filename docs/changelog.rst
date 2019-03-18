Release history and notes
=========================
`Sequence based identifiers
<http://en.wikipedia.org/wiki/Software_versioning#Sequence-based_identifiers>`_
are used for versioning (schema follows below):

.. code-block:: text

    major.minor[.revision]

- It's always safe to upgrade within the same minor version (for example, from
  0.3 to 0.3.4).
- Minor version changes might be backwards incompatible. Read the
  release notes carefully before upgrading (for example, when upgrading from
  0.3.4 to 0.4).
- All backwards incompatible changes are mentioned in this document.

0.1.5
------
yyyy-mm-dd (not yet released).

- Minor fixes in docs.
- Added Python 3.7 to the test matrix.

0.1.4
------
2019-03-16

- Clean up. Add proper docs.

0.1.3
------
2019-03-14

- Beta release.

0.1.2
------
2019-03-14

- Initial alpha release.