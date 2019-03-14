scripts
=======
Various helper (shell) scripts. Prior running any of those, please install
the project requirements.

.. code-block:: sh

    pip install -r requirements.txt

To set up the example project, type:

.. code-block:: sh

    ./scripts/prepare_project.sh

build_docs.sh
-------------
Build project documentation.

clean_up.sh
-----------
Removes temporary files, compiled python files, log files.

prepare_docs.sh
---------------
Prepares necessary changes for building the docs (combines multiple files
together) but does not yet build documentation.

prepare_project.sh
------------------
Makes necessary changes to the settings, runs migrations, collects statics,
creates necessary directories, creates project data.

rebuild_docs.sh
---------------
Run this each time you have changed a lot of things in the package (added lots
of modules).
