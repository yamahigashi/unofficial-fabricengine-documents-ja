.. _geometry_extension:

Geometry Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The ``Geometry`` extension provide a KL implementation of common geometry types, such as :kl-ref:`Points`, :kl-ref:`Lines` and :kl-ref:`PolygonMesh`. 
The extension additionally defines the various components and interfaces that are common to these geometry types.

All geometry types implement the :kl-ref:`Geometry` interface. They use the same type of :kl-ref:`GeometryAttributes` 
container to hold the attribute values that are associated to their components, such as positions, UVs and colors. This extension
contains the definition of various attribute types, such as the :kl-ref:`Vec3Attribute` and the :kl-ref:`ColorAttribute`. Custom attribute
types can be attached to a geometry, as long as they define the :kl-ref:`GeometryAttribute` interface.

All geometry types implement the :kl-ref:`SpatialQueryable` interface, which allows to perform spatial queries such
as raycast or getClosest. This extension defines two spatial acceleration structures, the :kl-ref:`Octree` and the :kl-ref:`SparseGrid`,
which are being used internally by the geometries to accelerate the spatial queries. For :ref:`spatialqueriesusage` for more details about
 the spacial query interfaces.

Geometries can be used in GPU compute kernels, enabling high performance geometry processing entirely on the GPU. With minimal changes, existing
code can be modified to run on the GPU. See :ref:`utilizinggpucompute` for more details about using Geometries in GPU compute kernels.

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2

  polygonmeshstructure
  spatialqueriesusage
  utilizinggpucompute
  files
  interfaces
  types
  functions

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
