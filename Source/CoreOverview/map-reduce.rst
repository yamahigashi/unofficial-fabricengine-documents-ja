Map-Reduce
============

|FABRIC_PRODUCT_NAME| provides a generic map-reduce framework that can be used to create recursively-parallel operations on large data sets. Map-reduce is an ideal paradigm for solving problems that are solved recursively, or require a reduction step such as counting elements in large data sets. 

The |FABRIC_PRODUCT_NAME| implementation of map-reduce expands on the concepts of the classic map-reduce model, providing a more flexible tool. By allowing the results of a map-reduce call do be used to drive further map-reduce calls, problems that are difficult to parallelize become solvable in this multi-threaded context.

Complete documentation for map-reduce is provided in the :ref:`MRPG`.
