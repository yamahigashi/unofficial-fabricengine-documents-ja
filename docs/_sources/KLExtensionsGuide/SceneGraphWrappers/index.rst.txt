.. _scenegraphwrappers_extension:

SceneGraphWrappers Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The SceneGraphWrappers extension provides various built-in wrappers for defining common behaviors 
for :ref:`SceneGraph<scenegraph_overview>` objects.

See :ref:`sgobjectwrapper_overview` for the definition of a scene graph object wrapper.

See :ref:`SceneHub<scenehub>` for a global picture of the
:ref:`SceneGraph<scenegraph_overview>`, the :ref:`sceneassembly` and the :ref:`rtr2`.

Here are some of the included wrappers:

- The :kl-ref:`SGTransformed` wrapper, which manages the transform and bounding box
  of the associated object, and defines a `localTransform`, `localBBox`, `globalTransform` 
  and `globalBBox` property.

- The :kl-ref:`SGInstance`, :kl-ref:`SGInstanceGroup` and :kl-ref:`SGInstanceArray` wrappers,
  allowing to specify one or many children objects.

- The :kl-ref:`SGPointLight`, :kl-ref:`SGSpotLight` and :kl-ref:`SGDirectionalLight`,
  which allow to define the properties of base light types.

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
