.. _scenegraph_extension:

SceneGraph Extension
=======================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The :kl-ref:`SceneGraph` is a generic container of scene objects (:kl-ref:`SGObject`), their 
properties (:kl-ref:`SGObjectProperty`) and the object references (hierarchy). 

See :ref:`scenegraph_overview` for more details.

See :ref:`SceneHub<scenehub>` for a global picture of the
:ref:`SceneGraph<scenegraph_overview>`, the :ref:`sceneassembly` and the :ref:`rtr2`.

Related extensions
-----------------

The SceneGraph extensions is closely related to these other extensions:

- The :ref:`sceneassembly_extension` defines interfaces for abstracting the scene
  along with nodes for filtering or processing scene graph elements.

- The :ref:`scenegraphwrappers_extension` extension defines common higher-level wrappers
  that define common scene types, such as :kl-ref:`SGDirectionalLight` or :kl-ref:`SGCamera`.

- The :ref:`scenegraph_to_rtr_extension` extension provides specialized adaptors from
  the :kl-ref:`SceneGraph` to :ref:`rtr2` objects, such as the :kl-ref:`SGCameraToRTR`.

- The :ref:`alembic_to_scenegraph` extension provides specialized generators 
  mapping AlembicWrapper readers to :kl-ref:`SceneGraph` objects, such as the :kl-ref:`SGAlembicGeometry`.

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  scenegraph_overview
  files
  interfaces
  types
  functions
  constants

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
