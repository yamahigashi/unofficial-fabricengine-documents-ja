.. _nodes:

Nodes
=====

The fundamental unit of the |FABRIC_PRODUCT_NAME| dependency graph is called a :dfn:`Node`.  A Node contains data and has a list of Operators, written in the KL programming language, that manipulate the data.

Node Creation
---------------

Each node must have a unique name which is specified when it node is created.  The name of the node must not conflict with the name of any Event, EventHandler or Operator (see below).  To create a node, call ``fabricClient.DG.createNode``.

.. code-block:: none
  
  >>> node = fabricClient.DG.createNode('vertices')
  >>> 

The name of a node can be retrieved through the ``getName`` method.

.. code-block:: none
  
  >>> node.getName()
  'vertices'
  >>> 

Node Members
---------------

A Node has zero or more :dfn:`members`.  Each member has a name (a non-empty string), a type (referred to as the name of a registered type), and, optionally, a default value.  Members can be added to nodes with the ``addMember`` method and an object with details of all the members can be retrieved with the ``getMembers`` method.

.. code-block:: none
  
  >>> node.addMember("position", "Vec3", Vec3(0.0, 0.0, 0.0))
  >>> node.getMembers()['position']
  {'defaultValue': <__main__.Vec3 instance at 0x1109727e8>, 'type': 'Vec3', 'name': 'position'}
  >>> 

.. note:: The optional third argument to ``node.addMember()`` is NOT an RTVal; it is a simple Python structure that has the same layout of the KL type.  Use of this default value is NOT recommended as it is from a very old version of the DG API.

Each member has a value, or in the case of a node with a slice count greater than one (see below), one value per slice.  The value of a member is retrieved using the ``getData`` method and set using the ``setData`` method.  Both methods take the member name as the first argument and the slice index as the second argument.

.. code-block:: none
  
  >>> vars(node.getData('position', 0))
  {'y': 0, 'x': 0, 'z': 0}
  >>> node.setData('position', 0, Vec3(1.0, 2.0, 3.0))
  >>> vars(node.getData('position', 0))
  {'y': 2, 'x': 1, 'z': 3}
  >>>

Node Slice Counts
-----------------

Each Node has a :dfn:`slice count`.  Setting the slice count of a node to a number greater than one enables the core to compute over an array of data ("SIMD parallelization"); each member has one value for each slice of the node.  The default slice count for a node is one.

.. note:: Operators can run on nodes per-slice or on all slices at once, depending on how the operator is bound to the node.  This will be explained below.

The slice count for a node is set with the ``setSliceCount`` (or ``setSize``) method and retrieved with the ``getSliceCount`` (or ``getSize``) method.

.. code-block:: none
  
  >>> node.getCount()
  1
  >>> node.getData('position', 1)
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/home/andrew/src/python_modules/fabric/__init__.py", line 883, in getData
      self._dg._executeQueuedCommands()
    File "/home/andrew/src/python_modules/fabric/__init__.py", line 460, in _executeQueuedCommands
      self.__client.executeQueuedCommands()
    File "/home/andrew/src/python_modules/fabric/__init__.py", line 315, in executeQueuedCommands
      raise Exception( '|FABRIC_PRODUCT_NAME| exception: ' + result[ 'exception' ] )
  Exception: |FABRIC_PRODUCT_NAME| exception: DG.verticies.getData('{"sliceIndex": 1, "memberName": ...'): index (1) out of range (1)
  >>> node.setCount(2)
  >>> node.getCount()
  2
  >>> vars(node.getData('position', 1))
  {'y': 0, 'x': 0, 'z': 0}
  >>> 

Node Dependencies
-----------------

Each node has zero or more named :dfn:`dependencies`; the dependency is another node.  If a node A has a dependency on another node B, then all of the operators of node A will run after all of those on node B have finished running.

- The name of a dependency must be a non-empty string.

- The name of the dependency is used to bind operators to the data in the dependency node

- Each dependency of a node must have a different name

- You cannot create a dependency loop between Nodes, ie. you cannot have Node A dependent on Node B at the same time as Node B is dependent on Node A.

Dependencies are added using the ``setDependency`` method, and dependencies of a node are retrieved using the ``getDependencies`` method.

.. code-block:: none
  
  >>> anotherNode = fabricClient.DG.createNode("originalVertices")
  >>> node.setDependency(anotherNode, "original")
  >>> node.getDependencies()
  {'original': <fabric._NODE object at 0x1050ffb10>}
  >>> 

Node Evaluation
---------------

Each node is either :dfn:`clean` or :dfn:`dirty`.  A node become dirty if any of the following happen:

- The node's ``setData`` method is called

- Anything about the node changes (eg. added dependencies, added members)

- Any of the node's dependencies becomes dirty

Nodes can be :dfn:`evaluated`.  Evaluating a node does the following: if the node is clean, nothing happens.  Otherwise,

- All the dependencies of the node are evaluated

- All of the operators bound to the node are executed

- The node is marked as clean

A node can be manually evaluated by calling the `evaluate` method.  Nodes are automatically evaluated when:

- A node is a dependency of another node that is evaluated

- An EventHandler (see below) has an operator bound to the data in the node, and the EventHandler is executed

.. code-block:: none
  
  >>> op = fabricClient.DG.createOperator("offsetPosition")
  >>> op.setEntryPoint("offset")
  >>> op.setSourceCode("require Vec3; operator offset(io Vec3 position, io Vec3 newPosition) { newPosition = position + Vec3(1.0,1.0,1.0); }")
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(op)
  >>> binding.setParameterLayout(["self.position", "self.newPosition"])
  >>> node.addMember("newPosition", "Vec3")
  >>> node.bindings.append(binding)
  >>> vars(node.getData("position", 0))
  {'y': 2, 'x': 1, 'z': 3}
  >>> vars(node.getData( "newPosition", 0 ))
  {'y': 0, 'x': 0, 'z': 0}
  >>> node.evaluate();
  >>> vars(node.getData( "newPosition", 0 ))
  {'y': 3, 'x': 2, 'z': 4}
  >>> 

