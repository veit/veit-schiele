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
    $ $ python3 -m venv .
    $ source bin/activate
    $ python -m pip install --upgrade pip
    $ python -m pip install -r requirements_dev.txt
    $ pre-commit install

#. Create HTML

   .. code-block:: console

    $ make html
