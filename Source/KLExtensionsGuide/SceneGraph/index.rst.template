.. _scenegraph_extension:

SceneGraph Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The :kl-ref:`SceneGraph` is a generic container of scene objects (:kl-ref:`SGObject`), their 
properties (:kl-ref:`SGObjectProperties`) and the relationships between these objects.

The :kl-ref:`SceneGraph` provides the following functionality:

- Providing various type of object references which can be used in a flexible
  way such as defining hierarchies, shared assets or object groups

- Supporting property propagation over hierarchies, with both default
  and overriden values, and allowing instance-specific property storage

- Allowing for higher-level wrapping of :kl-ref:`SGObjects` by specialized :kl-ref:`SGObjectWrapper`
  such as :kl-ref:`SGInstance` or :kl-ref:`SGCamera`

- Supporting :kl-ref:`SGObject` or :kl-ref:`SGObjectProperty` generators that can compute
  the requested values for a given context (:kl-ref:`SGContext`), with support
  of dependencies between generators (dependency graph). For example, the :kl-ref:`SGInstanceGroup`
  computes its `localBBox` from the children objects.
  
- Caching and management of contextual (animated) data [to be implemented]

- Allowing asynchronous updates by providing services such as the
  :kl-ref:`SGObjectPropertyWatch`, the :kl-ref:`SGIncrementalObserver`, the :kl-ref:`SGInstanceQuery`
  and by supporting the SceneInterface wrappers such as :kl-ref:`SWElementReference`

- Allowing for fast, runtime creation or deletion of scene objects
  and properties

- Minimizing memory allocations and fragmentation by grouping 
  objects and property sets in a few contiguous arrays

See the :kl-ref:`SceneGraph`, :kl-ref:`SGObject` and :kl-ref:`SGObjectProperty` for more details
about the SceneGraph API.

Related extensions
-----------------

The SceneGraph extensions is closely related to these other extensions:

- The SceneInterfaces extension define implementation-independant
  scene wrapper interfaces that are supported by the :kl-ref:`SceneGraph`
  or specialized wrapper objects (such as :kl-ref:`SceneGraphWrapper` or :kl-ref:`SGElementReferenceData`)

- The :kl-ref:`SceneGraphWrappers` extensions defines various higher-level wrappers
  such as the :kl-ref:`SGDirectionalLight` or :kl-ref:`SGCamera`

- The SceneGraphToRTR extension provides specialized adaptors from
  the :kl-ref:`SceneGraph` to RTR objects (eg: :kl-ref:`SceneGraphToRTR`,
  :kl-ref:`SGCameraToRTR`)

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
