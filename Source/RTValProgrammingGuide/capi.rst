.. RTVPG.capi:

Using RTVals from C++ Applications
=====================================

The section explains how to use RTVals within a |FABRIC_PRODUCT_NAME| client application written in C++ using the :ref:`CAPI <CAPIPG>` interface.

RTVals are Copy-by-Reference
----------------------------

RTVals are represented in C++ as instances of the :cpp:class:`RTVal` class.  RTVals are copy-by-reference within C++, meaning that if you assign one RTVal another variable of type RTVal they will refer to the same RTVal.  If you wish to copy an RTVal by value, use the :cpp:func:`RTVal::Construct` call.

Common Tasks
------------

Constructing RTVals
~~~~~~~~~~~~~~~~~~~

RTVals can be created in one of several ways:

  - RTVals can be constructed using one of the :code:`Construct...` methods of the :cpp:class:`RTVal` class.

  - For existing RTVals that are structure, object, array or dictionary type, methods on the :cpp:class:`RTVal` class can be called to obtain member or element values.  In most cases the returned RTVal is a copy of the member or element data.

  - The value of a member of a DG node (or other DGContainer) can be obtained through the :cpp:func:`DGContainer::getMemberSliceValue` call

To construct a copy of an RTVal, use the :cpp:function:`RTVal::Construct` method, passing the existing RTVal as the sole argument for the construction call.

.. note::

  Constructing an RTVal in this way does the same thing as copy-construction in KL; this means that in the case of pass-by-reference types such as variable arrays and dictionaries, even though the RTVal will be a copy it will still refer to the same underlying data.  To duplicate the data you must instead call :cpp:func:`RTVal::callMethod` to invoke the :code:`clone` method.

Obtaining C++ Equivalents for Simple RTVal Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can get C++ equivalents of the underlying data in simple RTVals using the :code:`get...` methods of the :cpp:class:`RTVal` class.  You should probably use the :code:`is....` methods first to check that the type is as expected, otherwise an exception will be thrown.

Setting RTVals from Simple C++ Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can set members, array elements, and dictionary values using the :code:`set...` methods of the :cpp:class:`RTVal` class.

Describing an RTVal
~~~~~~~~~~~~~~~~~~~

Often for debugging it is convenient to obtain a description of an RTVal; use the :cpp:func:`RTVal::getDesc` method for this.

Calling Methods on RTVals
~~~~~~~~~~~~~~~~~~~~~~~~~

Use the :cpp:func:`RTVal::callMethod` function to invoke a method on an RTVal.

Working with Arrays
~~~~~~~~~~~~~~~~~~~

If an RTVal's type is an array type, you can use the array methods to work with it:

  - :cpp:func:`RTVal::isArray`
  - :cpp:func:`RTVal::isVariableArray`
  - :cpp:func:`RTVal::getArraySize`
  - :cpp:func:`RTVal::getArrayElement`
  - :cpp:func:`RTVal::setArrayElement`

Working with Dictionaries
~~~~~~~~~~~~~~~~~~~~~~~~~

If an RTVal's type is a dictionary type, you can use the array methods to work with it:

  - :cpp:func:`RTVal::isDict`
  - :cpp:func:`RTVal::getDictSize`
  - :cpp:func:`RTVal::getDictElement`
  - :cpp:func:`RTVal::setDictElement`

Working with Structures and Objects
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If an RTVal's type is a structure or an object, you can work with its members:

  - :cpp:func:`RTVal::isStruct`
  - :cpp:func:`RTVal::isObject`
  - :cpp:func:`RTVal::maybeGetMember`
  - :cpp:func:`RTVal::maybeGetMemberRef`

For objects, you can use the :cpp:func:`RTVal::isNullObject` to check if the object that is being reference is null.

Working with Opaque Data
~~~~~~~~~~~~~~~~~~~~~~~~

You can use RTVals of type :code:`Data` to pass opaque data pointers in and out of the core, through to extensions that you use them.

  - :cpp:func:`RTVal::isData`
  - :cpp:func:`RTVal::getData`
  - :cpp:func:`RTVal::setData`

Working with KL :kl-ref:`RTVal`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| You can use cpp RTVals of type KL :kl-ref:`RTVal` to pass generic data in and out of the application. 
| cpp RTVals are not the cpp equivalent of a KL :kl-ref:`RTVal`, there is no one to one correspondance.
| Like other KL types, KL :kl-ref:`RTVal`s are contained within a cpp RTVals when accessed from C++.

| Here is an example of how retrieve the wrapped value of a KL :kl-ref:`RTVal` into a cpp RTVal:
 
.. code-block:: cpp

  //Access the KL :kl-ref:`RTVal` containing the KL data we want. 
  RTVal klRTVal = getRTVal(....);

  //Now, get the type of the KL data wrapped in the KL :kl-ref:`RTVal`. 
  const char * valType = klRTVal.callMethod("String", "type", 0, 0).getStringCString();

  //Then, construct a new cpp RTVal containing the KL data.
  RTVal cppRTVal = RTVal::Construct(client, valType, 1, &klRTVal);
 

API Reference
---------------------------

.. cpp:namespace:: FabricCore

.. cpp:class:: RTVal

  RTVals are represented in C++ as instances of the :code:`RTVal` class.

  .. cpp:function::
    RTVal()

    Creates a new RTVal.  RTVals are copy-by-reference within C++, so this is often used to initialized variables to which RTVals will later be assigned.

  .. cpp:function::
    RTVal( RTVal const &that )

    RTVal copy constructor.  RTVals are copy-by-reference within C++, so this simply makes the RTVal reference to the same RTVal as :code:`that`.

  .. cpp:function::
    RTVal &operator =( RTVal const &that )

    RTVal assignment operator.  RTVals are copy-by-reference within C++, so this simply makes the RTVal refer to the same RTVal as :code:`that`.  If there are no other RTVals refering to our current RTVal, the current RTVal will be freed.


  .. cpp:function::
    static RTVal Construct(Context const &context, char const *typeNameCString, uint32_t argCount, RTVal const *argRTVals)
    static RTVal Construct(Client const &client, char const *typeNameCString, uint32_t argCount, RTVal const *argRTVals)

    Construct a new RTVal using the KL copy construction syntax.  This takes the target type as well as a list of zero or more other RTVals, and it trys to invoke a copy construction from those RTVals.

    Note that invoking this method specifying an :code:`typeNameCString` which is an object type will create a null object reference.  In order to create a new object instance you must use the :code:`Create` method instead.

    Internally, this uses the following KL code to construct the RTVal:

    .. code-block:: kl

      <TypeName> resultRTVal(arg1RTVal, arg2RTVal, ...);

  .. cpp:function::
    static RTVal ConstructBoolean(Context const &context, bool value)
    static RTVal ConstructBoolean(Client const &client, bool value)

    Construct a new RTVal of type :code:`Boolean`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructSInt8(Context const &context, int8_t value)
    static RTVal ConstructSInt8(Client const &client, int8_t value)

    Construct a new RTVal of type :code:`SInt8`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructSInt16(Context const &context, int16_t value)
    static RTVal ConstructSInt16(Client const &client, int16_t value)

    Construct a new RTVal of type :code:`SInt16`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructSInt32(Context const &context, int32_t value)
    static RTVal ConstructSInt32(Client const &client, int32_t value)

    Construct a new RTVal of type :code:`SInt32`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructSInt64(Context const &context, int64_t value)
    static RTVal ConstructSInt64(Client const &client, int64_t value)

    Construct a new RTVal of type :code:`SInt64`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructUInt8(Context const &context, uint8_t value)
    static RTVal ConstructUInt8(Client const &client, uint8_t value)

    Construct a new RTVal of type :code:`UInt8`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructUInt16(Context const &context, uint16_t value)
    static RTVal ConstructUInt16(Client const &client, uint16_t value)

    Construct a new RTVal of type :code:`UInt16`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructUInt32(Context const &context, uint32_t value)
    static RTVal ConstructUInt32(Client const &client, uint32_t value)

    Construct a new RTVal of type :code:`UInt32`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructUInt64(Context const &context, uint64_t value)
    static RTVal ConstructUInt64(Client const &client, uint64_t value)

    Construct a new RTVal of type :code:`UInt64`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructFloat32(Context const &context, float value)
    static RTVal ConstructFloat32(Client const &client, float value)

    Construct a new RTVal of type :code:`Float32`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructFloat64(Context const &context, double value)
    static RTVal ConstructFloat64(Client const &client, double value)

    Construct a new RTVal of type :code:`Float64`, setting the initial value from the value of the parameter :code:`value`.

  .. cpp:function::
    static RTVal ConstructString(Context const &context, char const *data, uint32_t length)
    static RTVal ConstructString(Client const &client, char const *data, uint32_t length)

    Construct a new RTVal of type :code:`String`, setting the initial value from the string bytes given by :code:`data` and :code:`length`.  Note that such a string may contain null bytes.

  .. cpp:function::
    static RTVal ConstructString(Context const &context, char const *cString)
    static RTVal ConstructString(Client const &client, char const *cString)

    Construct a new RTVal of type :code:`String`, setting the initial value from a null-terminated (C-style) string bytes given by :code:`cString`.

  .. cpp:function::
    static RTVal ConstructData(Context const &context, void *data)
    static RTVal ConstructData(Client const &client, void *data)

    Construct a new RTVal of type :code:`Data`, setting the initial value to the given pointer value :code:`data`.  This is a simple way of passing pointers to opaque data through the Fabric core to extensions.

  .. cpp:function::
    static RTVal ConstructFixedArray(Context const &context, char const *elementTypeCString, uint32_t size)
    static RTVal ConstructFixedArray(Client const &client, char const *elementTypeCString, uint32_t size)

    Construct a new RTVal that is a fixed array of the given element type and size.  The elements of the array are initialized to the default value for the element type.

  .. cpp:function::
    static RTVal ConstructVariableArray(Context const &context, char const *elementTypeCString)
    static RTVal ConstructVariableArray(Client const &client, char const *elementTypeCString)

    Construct a new RTVal that is a variable array of the given element type.  The array is initially empty (length 0).

  .. cpp:function::
    static RTVal ConstructExternalArray(Context const &context, char const *elementTypeCString, uint32_t size, void *data)
    static RTVal ConstructExternalArray(Client const &client, char const *elementTypeCString, uint32_t size, void *data)

    Construct a new RTVal that is an external array referencing data of the given element type.  The :code:`size` and :code:`data` parameters should point to the array data that is being referenced.

  .. cpp:function::
    static RTVal ConstructDict(Context const &context, char const *keyTypeCString, char const *valueTypeCString)
    static RTVal ConstructDict(Client const &client, char const *keyTypeCString, char const *valueTypeCString)

    Construct a new RTVal that is a dictionary with the given key and value types.  The dictionary is initially empty.

  .. cpp:function::
    static RTVal Create(Context const &context, char const *typeNameCString, uint32_t argCount, RTVal const *argRTVals)
    static RTVal Create(Client const &client, char const *typeNameCString, uint32_t argCount, RTVal const *argRTVals)

    Create a new KL Object of the given type and assign the result to a new RTVal.  If :code:`typeNameCString` is not an object type an exception will be thrown.

    Note that invoking the :code:`Construct` method specifying a :code:`typeNameCString` that is an object type will create a null object reference.  In order to create a new object instance you must use this method instead.

    Internally, this uses the following KL code to construct the RTVal:

    .. code-block:: kl

      <TypeName> resultRTVal = TypeName(arg1RTVal, arg2RTVal, ...);

  .. cpp:function::
    bool getBoolean()

    Return the value of the RTVal that is of type :code:`Boolean`.  If the RTVal is not of type :code:`Boolean` an exception will be thrown.

  .. cpp:function::
    uint8_t getUInt8()

    Return the value of the RTVal that is of type :code:`UInt8`.  IfIf the RTVal is not of type :code:`UInt8` Exception will be thrown.

  .. cpp:function::
    uint16_t getUInt16()

    Return the value of the RTVal that is of type :code:`UInt16`.  IIf the RTVal is not of type :code:`UInt16` an exception will be thrown.

  .. cpp:function::
    uint32_t getUInt32()

    Return the value of the RTVal that is of type :code:`UInt32`.  IIf the RTVal is not of type :code:`UInt32` an exception will be thrown.

  .. cpp:function::
    uint64_t getUInt64()

    Return the value of the RTVal that is of type :code:`UInt64`.  IIf the RTVal is not of type :code:`UInt64` an exception will be thrown.

  .. cpp:function::
    int8_t getSInt8()

    Return the value of the RTVal that is of type :code:`SInt8`.  IfIf the RTVal is not of type :code:`SInt8` Exception will be thrown.

  .. cpp:function::
    int16_t getSInt16()

    Return the value of the RTVal that is of type :code:`SInt16`.  IIf the RTVal is not of type :code:`SInt16` an exception will be thrown.

  .. cpp:function::
    int32_t getSInt32()

    Return the value of the RTVal that is of type :code:`SInt32`.  IIf the RTVal is not of type :code:`SInt32` an exception will be thrown.

  .. cpp:function::
    int64_t getSInt64()

    Return the value of the RTVal that is of type :code:`SInt64`.  IIf the RTVal is not of type :code:`SInt64` an exception will be thrown.

  .. cpp:function::
    float getFloat32()

    Return the value of the RTVal that is of type :code:`Float32`.  If the RTVal is not of type :code:`Float32` an exception will be thrown.

  .. cpp:function::
    void setFloat32( float value )

    Set the value of the RTVal that is of type :code:`Float32` to :code:`value`.  If the RTVal is not of type :code:`Float32` an exception will be thrown.

  .. cpp:function::
    double getFloat64()

    Return the value of the RTVal that is of type :code:`Float64`.  If the RTVal is not of type :code:`Float64` an exception will be thrown.

  .. cpp:function::
    char const *getStringCString()

    Return the value of the RTVal that is of type :code:`String` as a C-string.  If the RTVal is not of type :code:`String` an exception will be thrown.

  .. cpp:function::
    uint32_t getStringLength()

    Return the string length of the RTVal that is of type :code:`String`.  If the RTVal is not of type :code:`String` an exception will be thrown.

  .. cpp:function::
    void *getData()

    Return the value of the RTVal that is of type :code:`Data` as a void pointer.  If the RTVal is not of type :code:`Data` an exception will be thrown.

  .. cpp:function::
    void setData( void *data )

    Set the value of the RTVal that is of type :code:`Data` to the value of the void pointer :ref:`data`.  If the RTVal is not of type :code:`Data` an exception will be thrown.

  .. cpp:function::
    bool isNullObject() const

    Return whether the RTVal that is of an object type is null.  If the RTVal is not of an object type an exception will be thrown.

  .. cpp:function::
    bool isArray() const

    Return whether the RTVal that is of a type that is a fixed, variable or external array of some other type.  Used to check if it's safe to perform array length and indexing calls.

  .. cpp:function::
    bool isVariableArray() const

    Return whether the RTVal is a variable array of some other type. Used to check if it's safe to perform array resizing calls.

  .. cpp:function::
    bool isDict() const

    Return whether the RTVal is of a dictionary type.

  .. cpp:function::
    bool isStruct() const

    Return whether the RTVal is of a structure type.

  .. cpp:function::
    bool isObject() const

    Return whether the RTVal is of an object type.

  .. cpp:function::
    bool isData() const

    Return whether the RTVal is of type :code:`Data`.

  .. cpp:function::
    bool isInterface() const

    Return whether the RTVal is of an interface type.

  .. cpp:function::
    uint32_t getArraySize() const

    Return the length of the RTVal that is of an array type.  If the RTVal is not of an array type, an exception will be thrown.

  .. cpp:function::
    void setArraySize( uint32_t newSize )

    Resize the RTVal that is of a variable array type.  If the RTVal is not of a variable array type, an exception will be thrown.

  .. cpp:function::
    RTVal getArrayElement( uint32_t index ) const

    Return a new RTVal that is a copy of the element of the array-typed RTVal at the given index.  If the RTVal is not of an array type, or the index is out-of-bounds for the array, an exception will be thrown.

  .. cpp:function::
    void setArrayElement( uint32_t index, RTVal const &value )

    Set the element of the array-typed RTVal at the given index.  The parameter :code:`value` must be an RTVal whose type can be casted to the element type of the array.  If the RTVal is not of an array type, or the index is out-of-bounds for the array, an exception will be thrown.

  .. cpp:function::
    uint32_t getDictSize() const

    Get the size (number of key-value pairs) of the RTVal that is of dictionary type.  If the RTVal is not of a dictionary type, an exception will be thrown.

  .. cpp:function::
    RTVal getDictElement( RTVal const &key ) const

    Return a new RTVal that is a copy of the value in the dictionary-typed RTVal for the given key.  :code:`key` must be an RTVal whose type can be casted to the key type of the dictionary.  If the RTVal is not of a dictionary type, or if there is no element for the given key, an exception will be thrown.

  .. cpp:function::
    void setDictElement( RTVal const &key, RTVal const &value )

    Set the value of the dictionary-typed RTVal for the given key.  :code:`key` must be an RTVal whose type can be casted to the key type of the dictionary.  If the RTVal is not of a dictionary type, an exception will be thrown.

  .. cpp:function::
    RTVal maybeGetMember( char const *memberNameCString ) const

    Return a new RTVal that is a copy of the named member in the structure- or object-typed RTVal.  If the RTVal is not of a structure nor object type, an exception will be thrown.  If there is no member named :code:`memberNameCString`, a null RTVal will be returned.

  .. cpp:function::
    RTVal maybeGetMemberRef( char const *memberNameCString ) const

    Return an RTVal that is a reference to the named member in the structure- or object-typed RTVal.  If the RTVal is not of a structure nor object type, or there is no member named :code:`memberNameCString`, an exception will be thrown.
    
    .. note:: It is the caller's personality to ensure that the result does not outlive the structure that it is referring to!

  .. cpp:function:: void setMember(char const *memberNameCString, RTVal const &value)

    Set the named member in the structure- or object-typed RTVal.  :code:`value` must be an RTVal whose type can be casted to the member type.  If the RTVal is not of a structure nor object type, or there is no member named :code:`memberNameCString`, an exception will be thrown.

  .. cpp:function:: RTVal callMethod(char const *resultTypeCString, char const *methodNameCString, uint32_t argCount, RTVal *argRTVals)

    Call a method on an RTVal.  :code:`resultTypeCString` must be the name of the result type of the method call; :code:`methodNameCString` must be the name of the method to call; and :code:`argCount` and :code:`argRTVals` specify the arguments for the call.

    If the method does not return a value, you must specify the empty string for :code:`resultTypeCString`; in this case, a null RTVal will be returned.  Otherwise, the result is a new RTVal that is return value of the method call.

    If no method exists with the given name and that takes the given argument types and whose result type can be casted to the specified type, an exception will be thrown.

  .. cpp:function::
    RTVal getDesc() const
    
    Return a new RTVal of type :code:`String` that is a description of the RTVal.

  .. cpp:function::
    RTVal getTypeName() const
    
    Return a new RTVal of type :code:`String` that is the name of the type of the RTVal.

  .. cpp:function::
    RTVal getJSON() const
    
    Return a new RTVal of type :code:`String` that is JSON-formatted description of the value.

    .. note:: This may not work for all types!

  .. cpp:function::
    void setJSON(RTVal const &jsonVal)

    Set the value of the RTVal from a JSON description obtained with the :code:`getJSON` method.

    .. note:: This may not work for all types!

.. cpp:class:: DGContainer

  There are a few methods on the :code:`DGContainer` class that work with RTVals.  These methods can be used to obtain RTVals that are copies of member value on DGNodes, for example.

  .. cpp:function::
    RTVal getMemberSliceValue(char const *memberCString, uint32_t index)
    
    Return a copy of the member data for the given slice as an RTVal.

  .. cpp:function::
    void setMemberSliceValue(char const *memberCString, uint32_t index, RTVal const &rtVal)

    Set the member data for the given slice from an RTVal.  If the RTVal cannot be casted to the type of the member, an exception will be thrown.

  .. cpp:function::
    RTVal getJSONStringValue()

    Get a JSON description of the container as an RTVal of type :code:`String`.

  .. cpp:function::
    void setJSONStringValue( RTVal const &stringRTVal )

    Set the contents of the container from a JSON-formatted RTVal string obtained with :cpp:func:`DGContainer::getJSONStringValue`
