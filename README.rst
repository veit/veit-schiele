============
Veit Schiele
============

Download and installation
-------------------------

#. Download

   .. code-block:: console

    $ git clone git@ce.cusy.io:veit/veit-schiele.git

#. Create virtual environment

   .. code-block:: console

    $ cd veit-schiele
    $ python3 -m venv .venv
    $ . .venv/bin/activate
    $ python -m pip install -e ".[dev]"
    $ pre-commit install

#. Create HTML

   .. code-block:: console

    $ cd docs
    $ make html
