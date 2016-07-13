.. _scenehub:

SceneHub overview
=================

The SceneHub is the name for a set of components allowing to create, process and render a scene. The SceneHub includes the following components:

- The :ref:`SceneGraph<scenegraph_overview>` is a generic KL-based scene graph which allows to define a hierarchy 
  of objects and properties. The :ref:`SceneGraph<scenegraph_overview>` implements the :ref:`sceneassembly` 
  interfaces, allowing it to be queried and processed by a generic procedural graph. The :ref:`SceneGraph<scenegraph_overview>`
  can be populated by generators such as Alembic readers (:ref:`alembic_to_scenegraph`).

- The :ref:`sceneassembly` defines a set of interfaces to abstract a scene and allow generic processing of its elements.
  It defines, too, a set of scene element queries and filter nodes which can define a scene processing procedural graph. The components that define or work with these abstracted scene interfaces are labeled with ``SW``, which stands for "Scene Wrapper".

- The :ref:`rtr2` defines a realtime renderer framework which is fast and flexible. It includes, too, components
  allowing to render scenes that are defining the :ref:`sceneassembly` interfaces. The :ref:`scenegraph_to_rtr_extension`
  defines specialized adaptors for mapping higher-level scene graph types (wrappers) to :ref:`rtr2` objects.

All these define KL runtime components of the SceneHub, but don't include specific UI or tools. The ``sceneHub`` application provides a 
simple base application for exploring SceneHub, and provides a basic implementation of tools such as selection and transform.
Additionally, it can be used to launch samples, for example ``sceneHub /Samples/RTR2/GeneratedInstances.kl``.

.. warning::

  The SceneHub and its components is a work in progress, and is still missing various functionality, examples, documentation.
  Although its general design should not change, it will continue to evolve.

.. _scenehub_scene_to_rtr:

From SceneGraph to RTR
----------------------

The following image illustrates an overview of the data flow from the :ref:`scenegraph` to the :ref:`rtr2`. The SceneGraph data is being filtered and processed by :ref:`sceneassembly` components:

.. image:: /images/SceneHub/SceneHub.png

The following steps are illustrated:

- A :kl-ref:`SceneGraph` structure is defined, which includes multiple scene graph objects (:kl-ref:`SGObject`) and their relationships.
  The scene graph objects are associated with higher-level wrappers which define concrete behavior and features for the scene graph 
  object. In this example, "My Wrapper" defines an intermediate between a the "My Asset" custom asset object and the scene graph. A generator is associated with the scene graph object so that the data can be fetched only when requested by the :ref:`sceneassembly` or :ref:`rtr2`.

- SceneGraph objects are extracted by a :ref:`sceneassembly` query. The resulting elements are returned as an array of 
  scene element references (:kl-ref:`SWElementReference`). These scene element references are lightweight and link directly
  to the related SceneGraph object or property. They provide a generic functionality such as getting a sub-property or getting
  the underlying value or interface.

- Various filters and processing :ref:`sceneassembly` nodes will further refine the selected data. These processing nodes 
  support incremental and asynchronous changes, which is a functionaity provided by their base class (:kl-ref:`BaseDynamicGroup`).
  The provided generic nodes are using the abstracted :kl-ref:`SceneWrapper` interfaces, however they can be specialized to provide
  a specific behavior (eg: RTR2 defines :kl-ref:`RTRCullFromCameraTask` which culls based on the volume of an :kl-ref:`RTRCamera`).
  
  .. warning::

    The set of provided processing or filtering nodes at this point is pretty limited, for example these don't 
    include nodes to "merge" multiple scenes together. Additionally, DFG support for the assembly graph is planned but
    hasn't been realized at this point.

- Finally, the :ref:`rtr2` will create rendering objects (such as instances or lights) corresponding to the provided 
  set of scene element references. Specific render object adaptors will be created depending on the type of the referenced 
  scene elements, using an adaptor registry mechanism (see :ref:`scenehub_adaptors`). The :ref:`rtr2` will further process
  the scene elements with its own task graph (:kl-ref:`RTRTask`) in order to generate the required drawing data and effects.

See :ref:`sceneassembly` for more details about procedural scene processing.

.. _scenehub_adaptors:

Scene element adaptors
----------------------

A fundamental concept of the SceneHub is the usage of adaptors. An adaptor is a KL Object
(usually an :kl-ref:`ObjectAdaptor`) which provides a data cache and functionality bridge
between a specific source scene element type and a specific target (eg: OpenGL RealTime Renderer
or a specific offline renderer).

The goal of adaptors is to provide specialized functionality and data cache
for mapping a source specialized type to a required target, which allows to have
custom objects properly translated by generic processing tasks. For example,
a source :kl-ref:`Vec3AttributeToRTR` adaptor will associate a :kl-ref:`Vec3Attribute`
with an :kl-ref:`OGLBuffer_` shared cache. Similarly, the :kl-ref:`SGDirectionalLightToRTR`
adapts a SceneGraph-specific :kl-ref:`SGDirectionalLight` to a RTR-specific
:kl-ref:`RTRDirectionalLight`.

Adaptors are registered with the :kl-ref:`RegisterAdaptor` global function, and
can be created by the :kl-ref:`CreateAdaptor` global function (these internally use a global
factory object: :kl-ref:`AdaptorRegistry`). Adaptors must be registered
before they can be created.

The :kl-ref:`SWElementReference` allows to create and attach adaptors to source scene items
(:kl-ref:`SWElementReference.getAdaptor`) and updates them. The adaptors remain attached
to the scene element itself, so different :kl-ref:`SWElementReference` referring the same
scene element will share a same adaptor. It is possible, however, that a different adaptor
is returned for different evaluation contexts (animated value).

.. _scenehub_adaptors_example:

SceneGraph to RTR adaptors example
...................................


The example below illustrates the components involved in creating adaptors from the SceneGraph
to the RTR:

.. image:: /images/SceneHub/SGtoRTRAdaptors.png

In the diagram above, the following steps are shown:

- The :kl-ref:`RTRSWGroupToInstanceTask` requests adaptors for mapping SceneGaph objects to RTR objects.
  More precisely, it needs to creates a `RTRInstance` for each input 
  :kl-ref:`SWElementReference` (stored in a :kl-ref:`SWElementReferenceArray`), and
  gets an adaptor for the "RTROGL" target.

- The :kl-ref:`SWElementReferenceArray` asks the :kl-ref:`AdaptorRegistry` for an adaptor
  from a :kl-ref:`SGGeometry` to an "RTROGL" target, and gets a :kl-ref:`RTRSWInstance`. It stores a reference
  of this adaptor in the SceneGraph, associated with the source :kl-ref:`SGGeometry` object so it is shared for all references.

- The :kl-ref:`RTRSWGroupToInstanceTask` updates the :kl-ref:`RTRSWInstance`, which recursively
  creates an adaptor for the underlying geometry (:kl-ref:`PolygonMeshToRTR`) and for the
  postions attribute (:kl-ref:`Vec3AttributeToRTR`).
