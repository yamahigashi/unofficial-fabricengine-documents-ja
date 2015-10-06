.. _events-event-handlers:

Event Graphs, Events and EventHandlers
======================================

|FABRIC_PRODUCT_NAME| provides a method of traversing the Nodes in the dependency graph through objects called Events and EventHandlers.  An Event can be fired, which will then fire a list of EventHandlers; each EventHandler has a list of child EventHandlers which are visited in turn, and each EventHandler has a list of :dfn:`pre-descend operators` that are executed before the child EventHandlers are visited and a list of :dfn:`post-descend operators` that are executed after the child EventHandlers are visit.  Each event handler can also bind to Nodes in the dependency graph to access from its Operators.  A typical use of Events and EventHandlers is for OpenGL rendering.  When an OpenGL viewport is created, a "redraw Event" is associated with it; this event is automatically fired whenever the viewport needs to be redrawn.  The EventHandlers that "chain" off of the redraw Event can then issue OpenGL calls to draw the viewport contents.

Event Creation
--------------------------

To create an Event, call the ``fabricClient.DG.createEvent`` function.  Like Nodes, Events must have a unique name that is not the same as that of a Node, Operator or EventHandler.  To get an existing event's name, call its ``getName`` method.

.. code-block:: none
  
  >>> event = fabricClient.DG.createEvent("anEvent")
  >>> event.getName()
  'anEvent'
  >>> 

EventHandler Creation
--------------------------

Event event has a list of EventHandlers attached so it.  When an Event is fired, each attached EventHandler is fired in sequence.  To create an EventHandler, call ``fabricClient.DG.createEventHandler``.  To append the EventHandler to an Event, call the Event's ``appendEventHandler`` method.

.. code-block:: none
  
  >>> eventHandler = fabricClient.DG.createEventHandler("trivialEventHandler")
  >>> event.appendEventHandler(eventHandler)
  >>> event.getEventHandlers()
  [<fabric._EVENTHANDLER object at 0x2cebfd0>]
  >>>

Operators and EventHandlers
---------------------------

Each EventHandler has two lists of Operators (or, rather, Bindings) called ``preDescendBindings`` and ``postDescendBindings``, as well as a list of child EventHandlers.  When an Event is fired, each of its EventHandlers is visited.  For each EventHandler, Bindings in ``preDescendBindings`` are executed in sequence, then its child EventHandlers are visited in the same way, then Bindings in ``postDescendBindings`` are executed in sequence.

.. code-block:: none
  
  >>> op = fabricClient.DG.createOperator("trivialOperator")
  >>> op.setSourceCode("operator entry() { report('Ran trivialOperator'); }")
  >>> op.setEntryPoint('entry')
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(op)
  >>> binding.setParameterLayout([])
  >>> eventHandler.preDescendBindings.append(binding)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  >>> anotherOp = fabricClient.DG.createOperator("trivialOperatorTwo")
  >>> anotherOp.setSourceCode("operator entry() { report('Ran trivialOperatorTwo'); }")
  >>> anotherOp.setEntryPoint('entry')
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(anotherOp)
  >>> binding.setParameterLayout([])
  >>> eventHandler.postDescendBindings.append(binding)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperatorTwo
  >>> 

EventHandlers in turn can have child EventHandlers.  The child EventHandlers of a given EventHandler are fired, in order, after the pre-descend operators are executed and before the post-descend operators are executed.  Child EventHandlers are added by calling the EventHandler's ``appendChildEventHandler`` method:

.. code-block:: none
  
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(op)
  >>> binding.setParameterLayout([])
  >>> ceh = fabricClient.DG.createEventHandler("childEventHandler")
  >>> ceh.preDescendBindings.append(binding)
  >>> eventHandler.appendChildEventHandler(ceh)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperatorTwo
  >>> 

EventHandlers can access data stored in Nodes by using their ``setScope`` method.  Once a Node is bound to an EventHandler, that Node is guaranteed to be evaluated (if it is dirty) before any Event that could fire the EventHandler is fired.  The name given in the ``setScope`` method is also available to child EventHandlers, their children, and so on, for binding.  If a child EventHandler binds a scope with the same name, it overrides the parent's scope.

.. code-block:: none
  
  >>> node = fabricClient.DG.createNode("someNode")
  >>> node.addMember( "x", "Scalar" )
  >>> node.addMember( "y", "Scalar" )
  >>> squareOp = fabricClient.DG.createOperator("squareOp")
  >>> squareOp.setSourceCode("operator entry( io Scalar x, io Scalar y ) { y = x * x; }")
  >>> squareOp.setEntryPoint("entry")
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(squareOp)
  >>> binding.setParameterLayout(['self.x','self.y'])
  >>> node.bindings.append(binding)
  >>> displayOp = fabricClient.DG.createOperator("displayOp")
  >>> displayOp.setSourceCode( "operator entry( io Scalar x, io Scalar y ) { report(x + ' squared is ' + y); }" )
  >>> displayOp.setEntryPoint("entry")
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(displayOp)
  >>> binding.setParameterLayout(['mynode.x','mynode.y'])
  >>> eventHandler.setScope("mynode",node)
  >>> eventHandler.postDescendBindings.append(binding)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperatorTwo
  [FABRIC] [MT] 0 squared is 0
  >>> node.setData('x',5.0)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperatorTwo
  [FABRIC] [MT] 5 squared is 25
  >>> 

EventHandler Data
--------------------------

EventHandlers themselves can also have data, and they set the name of their own scope, as seen by child EventHandlers, through ``setScopeName``:

.. code-block:: none
  
  >>> eventHandler.setScopeName("childEventHandler")
  >>> eventHandler.addMember("x","Scalar")
  >>> eventHandler.addMember("y","Scalar")
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(squareOp)
  >>> binding.setParameterLayout(['childEventHandler.x','childEventHandler.y'])
  >>> ceh.preDescendBindings.append(binding)
  >>> binding = fabricClient.DG.createBinding()
  >>> binding.setOperator(displayOp)
  >>> binding.setParameterLayout(['childEventHandler.x','childEventHandler.y'])
  >>> ceh.preDescendBindings.append(binding)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] 0 squared is 0
  [FABRIC] [MT] Ran trivialOperatorTwo
  [FABRIC] [MT] 5 squared is 25
  >>> eventHandler.setData("x",7.31)
  >>> event.fire()
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] Ran trivialOperator
  [FABRIC] [MT] 7.31 squared is 53.4361
  [FABRIC] [MT] Ran trivialOperatorTwo
  [FABRIC] [MT] 5 squared is 25
  >>> 
