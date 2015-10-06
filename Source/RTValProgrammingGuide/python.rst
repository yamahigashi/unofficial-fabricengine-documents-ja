.. RTVPG.python:

Using RTVals from Python Applications
=====================================

The section explains how to use RTVals within a |FABRIC_PRODUCT_NAME| client application written in Python

Obtain a |FABRIC_PRODUCT_NAME| Client Handle
---------------------------------------------------

We will assume that you have already obtained a |FABRIC_PRODUCT_NAME| client handle.  For more information on obtaining a client handle, see :ref:`DGPG.client.create`.

For the rest of this section, we will assume that the client handle is referred to by the Python variable named `client`.

.. code-block:: none
  
  $ python
  >>> import FabricEngine.Core
  >>> client = FabricEngine.Core.createClient()
  [FABRIC:MT] Fabric Core version 1.10.0
  [FABRIC:MT] Registered extensions {BadVersion,UnitTest,FabricALEMBIC,FabricBULLET,FabricCIMG,FabricEXR,FabricFBX,FabricFILESTREAM,Geometry,FabricHDR,FabricLIDAR,Math,FabricOBJ,FabricOPENCV,FabricOGL,FabricPNG,FabricStringTools,FabricTEEM,FabricTGA,FabricVIDEO} in directory: /Users/pzion/Fabric/CreationPlatform/stage/Darwin/x86_64/Release/Exts
  >>> 

Using Derived Types
---------------------

You can always use a base KL type such as ``String`` or ``UInt32`` for an RTVal; they are built-in and always available.

If you want your RTVal to be of a :ref:`derived type <KLPG.types.derived>`, the type must already be registered.

Many custom types are already provided by :ref:`built-in extensions <EXTR>`.  You can use any of these types for an RTVal, provided that the extension has been loaded.  Extensions are loaded by KL code that uses them (eg. DG operators), or you can explicitly load extensions by using the ``client.loadExtension(<extension name>)`` method.

You can also register a custom type to then use for RTVals; see :ref:`DGPG.registered-types`.

For the purposes of these examples, we will register a custom structure MyType with a custom constructor and a couple of methods:

.. code-block:: none
  
  >>> myTypeSource = """
  ... function MyType(String string, UInt32 uint32) {
  ...   this.string = string;
  ...   this.uint32 = uint32;
  ... }
  ... 
  ... function MyType.tweet() {
  ...   report("Tweet tweet!  string='" + this.string + "' uint32=" + this.uint32);
  ... }
  ... 
  ... function MyType.append!(MyType that) {
  ...   this.string += that.string;
  ...   this.uint32 += that.uint32;
  ... }
  ... """
  >>> 
  >>> myTypeDesc = {
  ...   'members': [{'string': 'String'}, {'uint32': 'UInt32'}],
  ...   'klBindings': {
  ...     'filename': "(inline)",
  ...     'sourceCode': myTypeSource
  ...    }
  ... }
  >>> 
  >>> client.RT.registerType('MyType', myTypeDesc)
  [FABRIC:MT] Compiled extension MyType in 0.961ms
  [FABRIC:ID] Optimized extension MyType in 29.553ms
  >>> print client.RT.getRegisteredTypes()['MyType']
  {'uuid': '8E8A7F4C', 'name': 'MyType', 'members': [{'type': 'String', 'name': 'string'}, {'type': 'UInt32', 'name': 'uint32'}], 'size': 32}
  >>> 

Creating an RTVal
------------------

To create a type, call the method ``client.RT.types.<TypeName>(<constructor parameters>)``:

.. code-block:: none
  
  >>> myRTVal = client.RT.types.MyType("Hello", 42)
  >>> print myRTVal
  <RTVal:{string:"Hello",uint32:42}>
  >>> 

You can see that the constructor for the RTVal was called with the passed
parameters.  You can see that RTVals have an automatic conversion to a string that describe the value, which is very handy for debugging.

If you try to construct with a non-existing constructor, you'll get an exception:

.. code-block:: none
  
  >>> client.RT.types.MyType("foo")
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  AttributeError: KL compile failed: constructArgs__ST.kl:2:106: error: no resolution for constructor MyType(io _CN<ST>)
  candidates are:
    function MyType(MyType)
    function MyType()
    function MyType(String, UInt32)
  >>> 

Getting Python values from an RTVal
-----------------------------------

By default RTVal methods and members are represented in Python by an 'RTVal' type, however in the case of simple types such as integers and strings a user may want these to be represented by the default Python type. The getSimpleType() method can be used on any
RTVal to return its value as a simple Python type, or 'None' if there is no default Python type that can be used to represent it:

.. code-block:: none

  >>> print myRTVal
  <RTVal:{string:"Hello",uint32:42}>
  >>> print myRTVal.getSimpleType()
  None
  >>> print myRTVal.uint32
  <RTVal:42>
  >>> print myRTVal.uint32.getSimpleType()
  42

Calling an RTVal Method
-----------------------

To call a method, simply calling the method, passing arguments.

.. note::
  
  Method calls in Python have a quirk where the name of the return type, as a string, must be passed as a first parameter; if there is no return type for the method, pass the empty string.  This quirk will be fixed in a future version of |FABRIC_PRODUCT_NAME|.

.. code-block:: none
  
  >>> myRTVal.tweet('')
  [FABRIC:MT] Tweet tweet!  string='Hello' uint32=42
  >>> 

In addition to plain Python types like integers and strings, you can also pass other RTVals as arguments:

.. code-block:: none
  
  >>> myRTVal2 = client.RT.types.MyType(", there", 71)
  >>> print(myRTVal2)
  <RTVal:{string:", there",uint32:71}>
  >>> myRTVal.append('', myRTVal2)
  >>> myRTVal.tweet('')
  [FABRIC:MT] Tweet tweet!  string='Hello, there' uint32=113
  >>> 

Creating Objects
----------------

As with objects in KL, a newly-created RTVal of an object type is always null.  To create a non-null object RTVal, call ``client.RT.types.<MyObjType>.create(<create args>)``.

Copying RTVal References
------------------------

Python variables that point to RTVals are references; as such, when you assign an RTVal to a variable it just makes another reference, and doesn't copy the underlying value.

Destroying an RTVal
--------------------

In Python, RTVals are automatically destroyed when they go out of scope.

Interfacing with the Dependency Graph
-------------------------------------

RTVals can be used to interface with the :ref:`dependency graph <DGPG>`.  You can use the ``node.getValue(<member>, <slice>)`` method to get a member value as an RTVal:

.. code-block:: none
  
  >>> node = client.DG.createNode("node")
  >>> node.addMember("myType", "MyType")
  >>> print node.getValue("myType", 0)
  <RTVal:{string:"",uint32:0}>
  >>> 

Similarly, you can use the ``setValue(<member>, <slice>, <value>)`` method to set the value from an RTVal:

.. code-block:: none
  
  >>> node.setValue("myType", 0, myRTVal)
  >>> print node.getValue("myType", 0)
  <RTVal:{string:"Hello, there",uint32:113}>
  >>> 

The same methods can also be used to work with events and event handlers.

.. warning::
  
  When you call ``getValue`` on a dependency graph node, the returned RTVal is a copy, and not a reference, of the value.  Thus, if you change the returned RTVal you will not change the value in the node from which it came.
