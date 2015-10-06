Concepts
===============

In traditional software development, programmers create data structures and write functions to manipulate the data.  In order for the program to perform operations in parallel, thereby taking advantage of multi-core CPUs, the programmer must call functions within the programming language itself to schedule the execution of the parallel pieces of code.

In a |FABRIC_PRODUCT_NAME| application, no explicit scheduling of execution is needed; the parallelism is instead expressed through higher-level models.  One of these models is the :dfn:`dependency graph` model, the subject of this book.  A |FABRIC_PRODUCT_NAME| application builds a dependency graph that describes the computation it needs perform; the |FABRIC_PRODUCT_NAME| core then automatically executes in parallel operations which are not interdependent.  This model requires that the user express data dependencies rather than have them implicit in the program itself.  By analyzing these interdependencies, the Fabric code creates an execution schedule that runs independent parts of the computation in parallel; in this way, Fabric achieves :dfn:`task-based` parallelism.

In addition, Fabric supports the notion of :dfn:`slicing` data.  A :dfn:`Node` in Fabric is a generic, typed data container that has one or more members that contain data; each Node also has a :dfn:`slice count` N, and the Node acts as if it were N independent copies of the same data that are operated on in parallel.  In this way, Fabric achieves :dfn:`data-based` (or :dfn:`SIMD`) parallelism.  For more information on Nodes, members, and slice counts, see :ref:`nodes`.

In addition to the dependency graph, Fabric provides a method of traversing the Nodes in the dependency graph through objects called Events and EventHandlers.  The Fabric SceneGraph uses Events and EventHandlers to draw OpenGL viewports in its rendering system.  For more information on Events and EventHandlers, see :ref:`events-event-handlers`.

The actual code that performs computation in Fabric is contained in objects called :dfn:`Operators`.  Operators can then be :dfn:`bound` to Nodes and EventHandlers using glue objects called Bindings; Bindings tell Fabric what data should be passed to the functions defined in the code in an Operator.  For more information on Operators, see :ref:`operators-bindings`.
