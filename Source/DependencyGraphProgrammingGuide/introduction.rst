Introduction
============

Fabric Engine is a platform for enabling high-performance computing inside of dynamic languages, running from both the command line and in graphical applications such as |FABRIC_PRODUCT_NAME|.  A Fabric Engine application can enable its high-performance components by creating and manipulating dependency graphs and associated event graphs using the dynamic language interface that Fabric Engine provides.  In many cases, such as through use of |FABRIC_PRODUCT_NAME|, this work is done by a higher-level framework that provides specific functionality to applications; however, in some cases it may be necessary to work directly with the core of Fabric Engine to extend these frameworks, create new frameworks, or to do lower level computation.

This document explains the concepts that are central to Fabric Engine's dependency graph model of parallel computation, and explains in detail how to work directly with this model of Fabric Engine.

Playing with the Fabric Engine Core
------------------------------------

The Fabric Engine :dfn:`core` refers to the lowest-level access to Fabric Engine that is available to a dynamic language, as opposed to higher-level interfaces such as through |FABRIC_PRODUCT_NAME|.  The Fabric Engine core is manipulated using a Python interface, and the easiest way to learn how to work directly with the dependency graph is through this interface.  This can be done using the |FABRIC_PRODUCT_NAME| module for Python.

Examples
------------------------------------

This document includes lots of examples showing |FABRIC_PRODUCT_NAME| core commands and the resulting output.  The commands are presented as if entered on the Python command line:

.. code-block:: none
  
  >>> print "Hello, world!"
  Hello, world!
  >>> 

.. _DGPG.client.create:

The ``fabricClient`` Object
------------------------------------

An object (``fabricClient`` in the examples below) through which you can manipulate the core can be obtained as follows in Python and Node.js:

.. code-block:: none
  
  >>> import FabricEngine.Core
  [FABRIC] Fabric Engine Core version |FABRIC_VERSION|
  >>> fabricClient = FabricEngine.Core.createClient()
  [FABRIC] [FabricTEEM] Extension registered
  ...
  >>> 
