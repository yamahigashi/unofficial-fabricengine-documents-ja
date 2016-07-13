.. _spatialqueriesusage:

Using spatial queries with geometries
=====================================

Spatial queries are a set of operations which perform searches based on geometric 
position. Common spatial queries include finding a ray intersection (`raycast`), finding 
the closest surface (`getClosest`), or searching an intersection with a volume 
like a sphere. The :kl-ref:`SpatialQueryable` interface allows to perform various spatial queries on 
:kl-ref:`Geometry` types such as the :kl-ref:`PolygonMesh`, the :kl-ref:`Lines` and 
the :kl-ref:`Points`.

When multiple spatial queries are performed on a same geometry, an acceleration structure
can greatly improve the performance. The :kl-ref:`SpatialQueryable` implementations of
built-in :kl-ref:`Geometry` types can internally cache an acceleration structure.
The acceleration structure needs to be properly prepared and updated before performing
queries; see :ref:`spatialqueryaccelerationstructures` for more details.

.. note::

  Performing spatial queries on a geometry is thread safe if the geometry is not modified
  and no calls are made to :kl-ref:`SpatialQueryable.prepareForSpatialQueries` or 
  :kl-ref:`SpatialQueryable.removeSpatialQueryAcceleration`.

.. kl-example:: Performing a simple shrink wrap deformer using SpatialQueryable

  require Geometry;

  operator ParallelShrinkWrap<<<index>>>( io PolygonMesh source, SpatialQueryable target ) {
    Ray ray;
    ray.start = source.getPointPosition( index );
    ray.direction = -ray.start.unit();//Unit vector toward sphere's center

    GeometryLocation location = target.raycast(ray, true, 0.0, SCALAR_INFINITE);
    if( location.isValid() )
      source.setPointPosition( index, target.getPositionAtLocation( location ) );
    else
      report("Unexpected: no hit");
  }

  operator entry(){
    //Shrink wrap a sphere onto a cylinder
    PolygonMesh source(), target();
    source.addSphere(Xfo(), 10.0, 3, true, false);

    //Cylinder (Y from -2.0 to 2.0)
    target.addCylinder(Xfo(), 4.0, 4.0, true, 16, 16, true, false);

    //Initialize options to use a sparse grid
    GenericValueContainer options = GenericValueContainer();
    PrepareForSpatialQueries_setSparseGrid(options);

    //Prepare for one query per source point
    target.prepareForSpatialQueries( source.pointCount(), options );

    report("Point 0 initial position: " + source.getPointPosition(0));
    ParallelShrinkWrap<<<source.pointCount()>>>( source, target );
    report("Point 0 deformed position: " + source.getPointPosition(0) );
  }

.. _spatialqueryobject:

Using the SpatialQuery object
-----------------------------

Some queries, such as :kl-ref:`SpatialQuery.getElementsInBBox`, are only accessible through to 
a :kl-ref:`SpatialQuery` object. The :kl-ref:`SpatialQuery` object is obtained by calling
:kl-ref:`SpatialQueryable.beginSpatialQuery`, and needs to be used temporarily until released 
by a call to :kl-ref:`SpatialQueryable.endSpatialQuery`. 

A :kl-ref:`SpatialQuery` object is valid if:

- it is used in the local scope between :kl-ref:`SpatialQueryable.beginSpatialQuery` and 
  :kl-ref:`SpatialQueryable.endSpatialQuery` (same thread)

- the geometry is not modified

- no calls to :kl-ref:`SpatialQueryable.prepareForSpatialQueries` or 
  :kl-ref:`SpatialQueryable.removeSpatialQueryAcceleration` are made

- it was not released with a call to :kl-ref:`SpatialQueryable.endSpatialQuery`

.. note::

  The :kl-ref:`SpatialQuery` object holds the thread-specific temporary storage needed for 
  efficiently performing one or multiple queries. These objects are recycled internally
  for a better performance.

  A call to :kl-ref:`SpatialQueryable.beginSpatialQuery` is thread-safe, but the returned
  :kl-ref:`SpatialQuery` object is not (should only be used locally).

The following example demonstrates proper multithreaded usage of a :kl-ref:`SpatialQuery` :

.. kl-example::

  require Geometry;

  operator ParallelBBoxSearch<<<index>>>( Ref<SpatialQueryable> target, io Boolean intersectsElementsBBox[10] ) {
    //Allocate a temporary query object
    Ref<SpatialQuery> query = target.beginSpatialQuery();

    Size elementCount = query.getElementsInBBox( Vec3(0, index, 0), Vec3(1, index+1, 1) );
    if( elementCount )
      intersectsElementsBBox[index] = true;

    //Release temporary query object
    target.endSpatialQuery(query);
  }

  operator entry(){
    //Check which unit bboxes with Y = 0..9 intersect the surface of a sphere of radius 5.0
    PolygonMesh target();
    target.addSphere(Xfo(), 5.0, 3, true, false);

    Boolean intersectsElementsBBox[10];
    target.prepareForSpatialQueries( 10, null );

    ParallelBBoxSearch<<<10>>>( target, intersectsElementsBBox );
    report("Intersected bounding boxes:\n " + intersectsElementsBBox );
  }

.. _geometrylocationstructure:

GeometryLocation structure
--------------------------

For methods such as :kl-ref:`SpatialQueryable.raycast`, where the result is a specific surface point, 
a :kl-ref:`GeometryLocation` structure is returned. The content and meaning of the :kl-ref:`GeometryLocation`
members is specific to each :kl-ref:`Geometry` type:

- :kl-ref:`PolygonMesh`:

  - `index` stores the polygon index

  - `subIndex` stores polygon's sub-triangle index. For example, in a quadrilateral with points [4,5,6,7],
    triangulated as [4,5,6] and [4,6,7], the `subIndex` for each triangle is 0 and 1, respectively.

  - `barycentric` store the barycentric weights relative to a triangle's points. For a triangle corresponding to
    attribute values [a,b,c], the resulting attribute value can be computed by the linear combination 
    ``(a * barycentric.x) + (b * barycentric.y) + (c * barycentric.z)``. 

- :kl-ref:`Lines`:

  - `index` stores the line segment index

  - `barycentric.xy` stores the weights for the start and the end points of the segment, respectively. For a segment
    where the start and end attribute values are [a,b], the resulting attribute value can be computed by the linear combination ``(a * barycentric.x) + (b * barycentric.y)``. 

- :kl-ref:`Points`:

  - `index` stores the point index, which is the same as the attribute index.

  - `barycentric` might store, when applicable, a `normal` relative to the point.
    This allows to keep the specific surface location when points have a size,
    and are considered as spheres.

.. note::

  A :kl-ref:`GeometryLocation` is valid only for a specific Geometry, or one with
  an identical structure (`topology`). A :kl-ref:`GeometryLocation` is stable through deformation
  (animation).

The :kl-ref:`GetAttributeAtLocation` helper functions can return the value of an attribute
corresponding to a :kl-ref:`GeometryLocation`. These are simple
wrappers around :kl-ref:`SpatialQueryable.getLocationAttributeIndicesAndWeights` and
attributes' `getLinearCombination` methods.

.. _spatialqueryaccelerationstructures:

Acceleration structures
-----------------------

Spatial queries can be performed with an internally cached acceleration structure like 
an :kl-ref:`Octree` or a :kl-ref:`SparseGrid`. Performing multiple queries without a cached 
acceleration structure can be very slow, particularly on complex geometries. A few rules need to be 
followed in order to properly use acceleration structures through the :kl-ref:`SpatialQueryable` interface.

Built-in geometries (:kl-ref:`PolygonMesh`, :kl-ref:`Lines`, :kl-ref:`Points`) support 
none, :kl-ref:`Octree` or :kl-ref:`SparseGrid` acceleration structures. These can be specified using the
:kl-ref:`SpatialQueryable.prepareForSpatialQueries` options. 

The default acceleration structure is the :kl-ref:`Octree` since it behaves well in all situations. 
Both acceleration structures support incremental updates (small change, small update cost).
See :ref:`octreesparsegridcompare` for a comparison of these acceleration structures.

The :kl-ref:`SpatialQueryable.prepareForSpatialQueries` method will install or update an 
acceleration structure in order to accelerate subsequent query calls (which can then be multithreaded). 
If :kl-ref:`SpatialQueryable.prepareForSpatialQueries` is not called initially or after geometry changes,
the geometry will detect it (from attribute and structure versions) and disable acceleration, which can lead
to poor performance.

.. note::

  When calling :kl-ref:`SpatialQueryable.prepareForSpatialQueries` again after a :kl-ref:`Geometry` type was
  modified, the acceleration structure will be updated incrementally. This implies that the acceleration structure 
  will be only partially modified to match the changes, which improves the performance. This is particularly
  helpful during playback, where the surface deformation is typically small from frame to frame.

.. note::

  The acceleration structures are internally made of compact arrays. Compiling KL
  in `unguarded` mode will usually speed up spatial queries by 30%.

The :kl-ref:`SpatialQueryable.removeSpatialQueryAcceleration` allows to delete the acceleration structure 
and free its memory. However, it is usually not recommended to call this method (see method's
description for more details).

.. _octreesparsegridcompare:

Octree versus SparseGrid
........................

Here is a quick comparison between the :kl-ref:`Octree` and the :kl-ref:`SparseGrid`:

- Memory: the Octree takes about twice the memory of a SparseGrid. Even if both structures were optimized for
  a low memory usage, they still require a noticeable amount of memory, which can be comparable to the memory used
  by the structure of a PolygonMesh.

- A SparseGrid builds and updates faster than an Octree, often by a factor of 2 or more.

- :kl-ref:`SpatialQuery.raycast`: if geometry elements (polygons, points) are relatively uniformly 
  distributed in space, the SparseGrid can be faster by about 30%, but could be slower if the 
  geometric elements' density varies a lot.

- :kl-ref:`SpatialQuery.getClosest`: the Octree is usually much faster than the SparseGrid.
  The SparseGrid is particularly slow if the search point is far from geometry's surface.

- :kl-ref:`SpatialQuery.getElementsInBBox` and :kl-ref:`SpatialQuery.getElementsInBSphere`: the SparseGrid will 
  be faster if the search volume is similar to the distance between geometry elements, and 
  if the geometry elements are relatively uniformly distributed in space. 
