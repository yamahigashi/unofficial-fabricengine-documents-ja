.. _bullet_extension:

Bullet Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The Bullet extension provides a wrapping of the BulletPhysics API. The Bullet API has been exposed in KL with minimal changes to the way the API is used. Some of the examples that ship with bullet have been migrated directly to kL to show how KL can be used to interact with the Bullet framework. 

For documentation on the Bullet API and how to use it, please refer to the Bullet Physics website and the documentation found there: (http://bulletphysics.org/)

.. note::
    The Bullet extension implements this slightly higher level wrapping of the Bullet API, enabling KL arrays to be passed into methods that, in the C++ API expect a count and pointer to be passed. Look at the provided source code of the Bullet extension for examples of how this has been implemented.

For example, in the Bullet API, to construct a btConvexHullShape, an array of scalar values is expected, with a stride of btVector3. These arguments are not easily expressed in KL as pointers are not supported in KL. 

.. kl-example::

  btConvexHullShape::btConvexHullShape( const btScalar* points = 0,
    int   numPoints = 0,
    int   stride = sizeof(btVector3) 
  );

The higher level constructor for the :kl-ref:`BulletConvexHullShape` takes instead a array of Vec3 values. The Bullet Extension handled unpacking the values from the array to pass to the C++ API.

.. kl-example::

  function BulletConvexHullShape(Vec3 points[]);

The :ref:`bullethelpers_extension` provides a set of higher level objects and functions that simplify working with the Bullet API.


Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  types

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
