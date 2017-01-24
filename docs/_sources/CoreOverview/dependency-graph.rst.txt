Dependency Graph (Deprecated)
=============================

The dependency graph model in |FABRIC_PRODUCT_NAME| abstracts the concepts of thread management from the user, enabling any developer to create highly scalable multi-threaded applications.

.. warning::
  
  The dependency graph compute model in |FABRIC_PRODUCT_NAME| is deprecated and
  will be removed in a future version.  New software should use the Canvas compute model
  instead!

Multi-Threaded Evaluation
-------------------------

Nodes are constructed using the developer’s preferred dynamic language, and the developer defines dependencies between those nodes. Operators are constructed and applied to the nodes in the graph. This combination of nodes, dependencies, and KL operators describes a complete workload made up of many tasks that can be distributed across available compute resources

Task-Based Parallelism
----------------------

Each node in the dependency graph can have operators applied to it. Operators define how the data should be processed and when it is propagated through the graph. The binding of an operator to a node represents a task to be executed. During evaluation of the graph |FABRIC_PRODUCT_NAME| can simultaneously evaluate nodes that do not have dependencies on each other. 

Data-Based Parallelism
----------------------

Each node in the dependency graph can be sliced. Each member contained in a node is duplicated according to the number of node slices. This enables nodes to define homogeneous data sets by storing large quantities of data across many slices. This enables data-based parallelism as operators bound to a node can be invoked for each slice in parallel.

Dynamic Graph Manipulation
--------------------------

|FABRIC_PRODUCT_NAME| systems can be modified at runtime, meaning that the behavior of a running application can be change based on such things as user input or network events. Between evaluations of the Core, the dynamic language can add or remove data, nodes, or operators. The structure of the graph can be changed causing different behavior. A validation is performed after modifications and then execution continues at full speed.

Event Graph
----------------------

The Event graph is used to sequence the execution of a set of operators through the construction of a tree structure. While the dependency graph is used for multi-threaded evaluation, the event graph is used for single-threaded evaluation. The event tree is built using a combination of a single event node and a tree of event handlers arranged in a tree structure below it. Evaluation always starts at the event node, then traverses the tree in a depth-first fashion. Operators are evaluated during descent and during ascent. 

Event handler nodes in the event tree can have nodes in the dependency graph bound to them. When an event is fired, the nodes in the dependency graph are bound to the event graph and are evaluated along with their dependencies. This system of binding the event tree to the dependency graph defines a dependency between the event tree and any number of nodes in the dependency graph. Firing the event will cause the bound sections of the dependency graph to be updated.

Rendering
^^^^^^^^^^^^^

The event graph is typically used to build rendering pipelines that draw to the screen using OpenGL. Each viewport in |FABRIC_PRODUCT_NAME| provides a custom event node that is fired whenever the viewport needs to be rendered. This causes all of the operators in the tree to be evaluated in the sequence that is defined by the structure of the tree.

The structure of the event graph and the sequential evaluation of this graph enable complex rendering configurations to be built. The resulting tree evaluates quickly and can be modified at runtime.

Custom Events
^^^^^^^^^^^^^

Custom events can be constructed and tree structures built below them. These events can be fired from the host language, which causes the operators in the tree to evaluate and also returns data structures to the host language. This enables tools to query data in the graph that may be distributed across many nodes. In |FABRIC_PRODUCT_NAME|, the event system is used to compute ray intersections with the geometry in the scene.

Documentation
----------------------

Complete documentation for working with the dependency graph is provided in the :ref:`DGPG`.
