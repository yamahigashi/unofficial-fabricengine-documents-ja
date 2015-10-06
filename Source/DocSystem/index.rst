.. _DOCSYSTEM:

Fabric Engine Documentation System
======================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The Fabric Engine Documentation system is modeled on top of Sphinx. You'll need to install sphinx following the default installation instructions.

`http://sphinx-doc.org/ <http://sphinx-doc.org/>`_

The documentation system used in the Fabric Engine products utilizes sphinx and a series of sphinx directives. These directives expand recursively to build the restructured text content.

Additionally the Fabric Core is used to provide AST from KL files. This allows to embed documentation of KL extension directly into the KL files.

Table of Contents
-----------------

.. toctree::
  :maxdepth: 1
 
  prerequisites
  example
  directives
  qualifiers

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
