.. _alembic_to_scenegraph:

AlembicToSceneGraph Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The AlembicToSceneGraph extension provides helpers and generators 
for mapping AlembicWrapper readers to :ref:`SceneGraph<scenegraph_overview>` object wrappers
and generators.

The :kl-ref:`AlembicArchiveToSceneGraph` helper class allows to map an
an :kl-ref:`AlembicArchiveReader` to a SceneGraph object, which will expand to more
children SceneGraph object nodes upon request.

.. warning::

  This extension only defines mapping for base geometry types and transform hierarchies.
  It has not been generalized yet for allowing custom Alembic wrappers.

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  interfaces
  types
  functions
  constants

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
