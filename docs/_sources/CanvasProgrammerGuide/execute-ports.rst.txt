.. _canvas-programmer-guide-execute-ports:

Execute Ports
===============================

Execute ports are a special type of port used to control execution of the graph.  For the most part execute ports and their connections appear like regular ports and connections in Canvas, but their behavior is somewhat different, as described below.

An execute port is a port whose type is the built-in type `Execute`.  The type `Execute` is an empty type and carries no data; however, the core of Fabric Engine looks for ports of type `Execute` and uses them to control how Canvas graphs are executed.

The Implicit Execute Port
--------------------------------

Every instance node automatically has a port of type `Execute` called `exec`.  This is referred to as the :dfn:`implicit execute port`.  The implicit execute port does not appear alongside regular ports on nodes but rather is accessible through the node header:

.. image:: /images/Canvas/ProgrammerGuide/ExecutePorts/exec-1.png

Once connected, the connection will also originate from or connect to the node header:

.. image:: /images/Canvas/ProgrammerGuide/ExecutePorts/exec-2.png

The implicit execute port is automatically "pulled" by a node before the node is executed.  This allows Canvas programmers to ensure that other nodes that are connected to it will be executed before the node is executed.

.. _canvas-programmer-guide-execute-ports-explicit:

Explicit Execute Ports
----------------------------

In addition to the implicit execute port, you can add explicit execute ports to a node by simply adding ports of type `Execute`:

.. image:: /images/Canvas/ProgrammerGuide/ExecutePorts/exec-3.png

In the above example, which is a Canvas function that implements a for loop, the `body` port has type `Execute`.

In order to cause an implicit execute port to be executed, you simply wrap the name of of the port in the `dfgExecute(...)` construct as shown above.

.. note::

  Note that the `dfgExecute(...)` construct is optional; simply inserting the name of the implicit execute port as an expression will cause it to be executed.  The purpose of this is to allow certain polymorphic nodes such as `Fabric.Core.Control.If` to operate equally well when their ports have execute and non-execute types.

Connections To and From Execute Ports
------------------------------------------

In addition to connections between ports that both have type `Execute`, it is possible to connect from a port that has a type other than `Execute` to a port of type `Execute`:

.. image:: /images/Canvas/ProgrammerGuide/ExecutePorts/exec-4.png

Such a connection simply pulls the port in question and discards the result.

Multiple Connections to Execute Ports
------------------------------------------

Unlike regular ports, it is possible to have multiple connections to a single execute port:

.. image:: /images/Canvas/ProgrammerGuide/ExecutePorts/exec-5.png

In the case of multiple connections, the order in which Canvas "pulls" the connected ports is not guaranteed; this is to enable (eventually) parallel evaluation of multiple branches.  If you wish to guarantee sequential evaluation, use one of the Execute.Merge presets.

.. note::

  It is not currently possible in the Canvas interface to see the order of the connections; therefore it is recommended to lay out the nodes manually in the order of the connections so that it is obvious for someone reading the graph.  This will be fixed in a future version of Fabric.

Multiple Executions of Execute Ports
------------------------------------------

Unlike regular ports, if an implicit execute port is "pulled" multiple times, then it will be evaluated multiple times.  This allows you to create looping-type constructs using execute ports.

Furthermore, whenever an execute port is pulled it will re-evaluate all the (execute and non-execute) ports behind the execute port.  In contrast, when a regular port is pulled it will only evaluate the ports behind it if they haven't already been evaluated.

It is possible to ensure that (execute and non-execute) ports are only pulled a single time by using a explicit `Cache` node.  Simply put the cache node in front of the nodes that you only want to have evaluated a single time.

All of this is illustrated in the ForLoop.canvas example that ships with Fabric, located at :file:`$FABRIC_DIR/Samples/Canvas/ExecutePorts/ForLoop.canvas`.  In this example we use execute ports to execute a collection of nodes as the body of a loop, using a Canvas variable to track the iteration of the loop.

.. note::

  This example is meant to serve primarily as an example of how execute ports work; For a more natural way of looping over groups of nodes please refer to :ref:`the blocks section of the Canvas Programming Guide <canvas-programming-guide-blocks>`

