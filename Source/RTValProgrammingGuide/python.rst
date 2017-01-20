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
  [FABRIC:MT] Fabric Engine version 2.4.0 (development)
  [FABRIC:MT] Crash handler registered.
  [FABRIC:MT] Loading DFG presets from C:\Users\helge\Fabric\Presets
  [FABRIC:MT] Registered extensions {Alembic:1.1.0,AlembicImporter:1.0.0,AlembicWrapper:1.7.0,Animation:1.1.1,AttributeHelpers:1.0.1,BinPacking:1.0.0,Bullet:1.0.3,BulletHelpers:1.0.0,Characters:1.2.0,Containers:1.2.0,DFGWrapper:1.2.0,FabricInterfaces:1.1.0,FabricSynchronization:1.2.0,Fbx:1.2.1,FbxHelpers:1.1.0,FbxImporter:1.0.0,FileIO:1.3.1,FreeTypeGL:2.3.0,GenericImporter:1.0.0,Geometry:1.6.0,Images:2.1.0,InlineDrawing:1.6.0,JSON:1.1.0,LA:1.0.0,Manipulation:1.2.1,Math:1.5.0,FabricOBJ:1.1.0,ObjImporter:1.0.0,OGLWrappers:1.2.0,FabricOGL:1.1.0,OpenImageIO:1.1.0,OSOGL:1.1.0,Parameters:1.1.0,Singletons:1.1.2,FabricStatistics:1.1.1,Text:2.4.0,Util:1.4.1,ImageProcessing,RTR,RTRAdaptors,Multipede,Particles} in directory: ${FABRIC_DIR}\Exts
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

Creating an RTVal for KL basic types or Structures
---------------------------------------------------

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


Creating an RTVal for KL Objects
---------------------------------

.. warning::

  As with objects in KL, a newly-created RTVal of an object type is always null.  
  To create a non-null object RTVal, call ``client.RT.types.<MyObjType>.create(<create args>)``.
  However, if a KL object implements a constructor WITH PARAMETERS, a non-null object RTVal can be constucted by calling directly ``client.RT.types.<MyObjType>(<create args>)``.

Here is a example of structures (or basic types) and object RTVals constrution in Python.
KL object and structure declaration defined in MyExt extension :

.. code-block:: kl

  object MyObj {
    Float32 value;
  };

  MyObj() {
    this.value = 0.0f;
  }

  MyObj(Float32 value) {
    this.value = value;
  }

  struct MyStruct {
    Float32 value;
  };

  MyStruct() {
    this.value = 0.0f;
  }

  MyStruct(Float32 value) {
    this.value = value;
  }

Construction in Python :
 
.. code-block:: none
  
  client.loadExtension('MyExt')

  # 1. Objects
  # 1.1 Direct call from RTVal
  myObj = self.client.RT.types.MyObj()
  str(myObj.type('String').getSimpleType()) >>> None
  str(myObj) >>> Obj <RTVal:null>

  myObj = self.client.RT.types.MyObj(1)
  str(myObj.type('String').getSimpleType()) >>> MyObj
  str(myObj) >>> <RTVal:{value:+1.0}>

  myObj = self.client.RT.types.MyObj.create()
  str(myObj.type('String').getSimpleType()) >>> MyObj
  str(myObj) >>> <RTVal:{value:+0.0}>

  myObj = self.client.RT.types.MyObj.create(1)
  str(myObj.type('String').getSimpleType()) >>> MyObj
  str(myObj) >>> <RTVal:{value:+1.0}>

  # 1.2 Call from RTVal type
  myObjType = getattr(self.client.RT.types, "MyObj")

  myObj = myObjType()
  str(myObj.type('String').getSimpleType()) >>> None
  str(myObj) >>> <RTVal:null>

  myObj = myObjType(1)
  str(myObj.type('String').getSimpleType()) >>> MyObj
  str(myObj) >>> <RTVal:{value:+1.0}>

  myObj = myObjType.create()
  str(myObj.type('String').getSimpleType()) >>> MyObj
  str(myObj) >>> <RTVal:{value:+0.0}>

  myObj = myObjType.create(1)
  str(myObj.type('String').getSimpleType()) >>> MyObj
  str(myObj) >>> <RTVal:{value:+1.0}>


  # 2. Structures (same for basic types)
  # 2.1 Direct call from RTVal
  myStruct = self.client.RT.types.MyStruct()
  str(myStruct.type('String').getSimpleType()) >>> MyStruct 
  str(myStruct) >>> <RTVal:{value:+0.0}>

  myStruct = self.client.RT.types.MyStruct(1)
  str(myStruct.type('String').getSimpleType()) >>> MyStruct
  str(myStruct) >>> <RTVal:{value:+1.0}>

  # 2.2 Call from RTVal type
  myStructType = getattr(self.client.RT.types, "MyStruct")
  myStruct = myStructType()
  str(myStruct.type('String').getSimpleType()) >>> MyStruct
  str(myStruct) >>> <RTVal:{value:+0.0}>

  myStruct = myStructType(1)
  str(myStruct.type('String').getSimpleType()) >>> MyStruct
  str(myStruct) >>> <RTVal:{value:+1.0}>


Creating RTVal Arrays
---------------------

To create an array of a type, call the method ``client.RT.types.<TypeName>.createArray(<OptionalListOfRTVals>)``:

.. code-block:: none

  >>> // Create an empty Vec3 Array
  >>> myRTValArray = client.RT.types.Vec3.createArray()
  >>> print myRTValArray
  <RTVal:[]>
  >>>
  >>> // Create a Vec3 Array with two Vec3 items
  >>> vec1 = client.RT.types.Vec3(0, 1, 0)
  >>> vec2 = client.RT.types.Vec3(0, 2, 0)
  >>> myRTValArray = client.RT.types.Vec3.createArray([vec1, vec2])
  >>>
  >>> print myRTValArray
  <RTVal:[{x:+0.0,y:+1.0,z:+0.0},{x:+0.0,y:+2.0,z:+0.0}]>
  >>>
  >>> // Create a Scalar Array with two items from Python built in float types
  >>> myRTValArray = client.RT.types.Scalar.createArray([1.5, 2.5])
  >>>
  >>> print myRTValArray
  <RTVal:[+1.5,+2.5]>

Creating 2D RTVal Arrays
------------------------

To create a 2D array of a type, users will need to query the registered types object for an attribute that is named ``<Type>[]`` and call the ``.createArray()`` method on the returned type.

.. code-block:: none

  >>> matrixA = client.RT.types.Mat44()
  >>> matrixB = client.RT.types.Mat44()
  >>>
  >>> matrixC = client.RT.types.Mat44()
  >>> matrixD = client.RT.types.Mat44()
  >>> matrixE = client.RT.types.Mat44()
  >>>
  >>> subArray1 = client.RT.types.Mat44.createArray([matrixA, matrixB])
  >>> subArray2 = client.RT.types.Mat44.createArray([matrixC, matrixD, matrixE])
  >>>
  >>> registeredTypes = client.RT.types
  >>> mat44ArrayType = getattr(registeredTypes, 'Mat44[]')
  >>> matrix2DArray = mat44ArrayType.createArray([subArray1, subArray2])
  >>>
  >>> print "Matrix 2D Array Size: " + str(len(matrix2DArray))
  >>> print "SubArray 1 Array Size: " + str(len(matrix2DArray[0]))
  >>> print "SubArray 2 Array Size: " + str(len(matrix2DArray[1]))
  Matrix 2D Array Size: 2
  SubArray 1 Array Size: 2
  SubArray 2 Array Size: 3


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

  >>> quat = client.RT.types.Quat()
  >>> upVec = client.RT.types.Vec3(0, 1, 0)
  >>> dirVec = client.RT.types.Vec3(1, 0, 0)
  >>>
  >>> // You have to pass an emtpy string when calling methods that don't return a type.
  >>> quat.setFromDirectionAndUpvector('', dirVec, upVec)
  >>>
  >>> print quat
  <RTVal:{v:{x:+0.0,y:+0.707106,z:+0.0},w:+0.707106}>
  >>>

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

There are several special method names defined by the Python interface to the Fabric Core, such as ``getJSON`` and ``getDesc``.  If the method name you wish to call is exactly the same as one of these special method names then you will not be able to call it directly as above.  Instead, use the (special) method ``callMethod`` to call the method by name.  ``callMethod`` takes the return type name as a first parameter and the method name as a second parameter, followed by the arguments to the method call, if any.

.. code-block:: none

  >>> myRTVal.callMethod('', 'tweet')
  [FABRIC:MT] Tweet tweet!  string='Hello, there' uint32=113
  >>>

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

Working with KL :kl-ref:`RTVal`
-------------------------------

| You can use Python RTVals of type KL :kl-ref:`RTVal` to pass generic data in and out of the application. 
| Python RTVals are not the Python equivalent of a KL :kl-ref:`RTVal`, there is no one to one correspondance.
| Like other KL types, KL :kl-ref:`RTVal`s are contained within a Python RTVals when accessed from Python.

| Here is an example of how retrieve the wrapped value of a KL :kl-ref:`RTVal` into a Python RTVal:
 
.. code-block:: none

  # Access the KL :kl-ref:`RTVal` containing the KL data we want. 
  klRTVal = getRTVal(....);
  
  # Now, get the type of the KL data wrapped in the KL :kl-ref:`RTVal`. 
  valType = str(klRTVal.type('String').getSimpleType())
  
  # Then, construct a new Python RTVal containing the KL data.
  rtValType = getattr(self.client.RT.types, valType)
  pythonRTVal = rtValType(klRTVal)

 
