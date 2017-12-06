.. megatroniki documentation master file, created by
   sphinx-quickstart on Thu Nov 30 08:41:41 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to megatroniki's documentation!
=======================================

.. toctree::
   :maxdepth: 4
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Megatroniki
===========

Megatroniki is a project that is a wikipedia style reference with the ability to make and edit your own pages using markdown.

Features
--------

- Download page as a pdf
- Search for page title on google scholar
- Users have passwords encrypted
- Admin user can add users
- Users can receive email notifications when a page is updated
- Users can open page in favorite text editor for editing

Requirements
------------

* Python 2.6, 2.7
* Python `VirtualEnv <http://www.virtualenv.org/>`_ and ``pip`` (recommended installation method; your OS/distribution should have packages for these)

.. _getting_started.installing:

Installing
----------

It's recommended that you install into a virtual environment (virtualenv /
venv). See the `virtualenv usage documentation <http://www.virtualenv.org/>`_
for more details, but the gist is as follows (the virtualenv name, "megatroniki" here,
can be whatever you want):

.. code-block:: bash

    virtualenv megatroniki
    source megatroniki/bin/activate
    pip install megatroniki

Now you can install the packages in requirements.txt

.. code-block:: bash

    pip install -r requirements.txt

Running the Project
-------------------
Run the project with parameter web:

    megatroniki web

Contribute
----------

- Issue Tracker: https://github.com/konzy/CSC440-Wiki-Project/issues
- Source Code: https://github.com/konzy/CSC440-Wiki-Project

Support
-------

If you are having issues, please let us know.
Support will be available at https://github.com/konzy/CSC440-Wiki-Project/issues