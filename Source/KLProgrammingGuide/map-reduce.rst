.. index::
  single: map-reduce

.. _map-reduce:

Map-Reduce
==========

|FABRIC_PRODUCT_NAME| provides a generic map-reduce framework that can be used to create recursively-parallel operations on large data sets.

This chapter does not attempt to explain the concepts behind and usage of the |FABRIC_PRODUCT_NAME| map-reduce framework; it serves purely to enumerate the types and functions that are provided in KL to support the framework.  For more information on concepts and usage of the map-reduce framework, refer to the Map-Reduce Programming Guide.

.. index::
  pair: map-reduce; type

.. _mr-types:

Map-Reduce Types
----------------

In order to support map-reduce, KL introduces two new derived types: :samp:`ValueProducer<{ValueType}>` and :samp:`ArrayProducer<{ElementType}>`.

.. index::
  pair: ValueProducer; type

.. _value-producer:

The :samp:`ValueProducer<{ValueType}>` Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given an existing type :samp:`{ValueType}`, the type :samp:`ValueProducer<{ValueType}>` is a map-reduce value producer that produces values of type :samp:`{ValueType}`.  Values of type :samp:`ValueProducer<{ValueType}>` have the following properties:

- They can be assigned to variables of the same type; however, there must be an exact match for :samp:`{ValueType}`.  In other words, :samp:`ValueProducer<{ValueType1}>` and :samp:`ValueProducer<{ValueType2}>` are the same type if and only if :samp:`{ValueType1}` and :samp:`{ValueType2}` are the same type.

- They support a method
  
  .. parsed-literal::
    
    function :samp:`{ValueType}` ValueProducer<:samp:`{ValueType}`\>.produce()
  
  that produces the value producer's value.

- They support a method
  
  .. parsed-literal::
    
    function ValueProducer<:samp:`{ValueType}`\>.flush()
  
  that recursively flushes any caches connected to the value producer.

.. _array-producer:

The :samp:`ArrayProducer<{ElementType}>` Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given an existing type :samp:`{ElementType}`, the type :samp:`ArrayProducer<{ElementType}>` is a map-reduce array producer that produces values of type :samp:`{ElementType}`.  Values of type :samp:`ArrayProducer<{ElementType}>` have the following properties:

- They can be assigned to variables of the same type; however, there must be an exact match for :samp:`{ElementType}`.  In other words, :samp:`ArrayProducer<{ElementType1}>` and :samp:`ArrayProducer<{ElementType2}>` are the same type if and only if :samp:`{ElementType1}` and :samp:`{ElementType2}` are the same type.

- They support a method
  
  .. parsed-literal::
    
    function Size ArrayProducer<:samp:`{ElementType}`\>.getCount()
  
  that returns the number of elements in the array producer.  Calling :samp:`produce({i})` (below) with :samp:`{i}` not less than the result of ``getCount()`` will throw an exception.

- They support a method
  
  .. parsed-literal::
    
    function :samp:`{ElementType}` ArrayProducer<:samp:`{ElementType}`\>.produce(Index :samp:`{i}`)
  
  that produces the array producer's element at index :samp:`{i}`.

- They support a method
  
  .. parsed-literal::
    
    function ArrayProducer<:samp:`{ElementType}`\>.flush()
  
  that recursively flushes any caches connected to the array producer.

.. _mr-functions:

Map-Reduce Functions
--------------------

KL supports several functions to support the creation of new value and array producers from existing producers as well as KL functions and values.

Value Producer Creation Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. js:function:: createConstValue(expr)
  
  Creates a value producer that returns a constant value.
  
  :param ValueType expr:
    The expression to evaluate to obtain the constant value.
  
  :rtype: ValueProducer<ValueType>
  
  Example::
  
    operator entry() {
      ValueProducer<Integer> vp = createConstValue( 42 );
      report(vp);
      report(vp.produce());
    }
  
  Output::
  
    ValueProducer<Integer>
    42

.. js:function:: createValueGenerator(operatorName[,  sharedValueProducer])
  
  Creates a value producer that calls the operator named *operatorName* to generate the value.
  
  :param operatorName:
    The name of the operator to call to generate the value.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ValueProducer<ValueType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        io *ValueType* outputValue,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  The type *ValueType* is inferred from the first parameter of *operatorName*.
  
  Example::
  
    operator gen1(io String output) {
      output = "Hello!";
    }

    operator gen2(io String output, String shared) {
      output = "Hello, " + shared;
    }

    operator entry() {
      ValueProducer<String> vp1 = createValueGenerator(gen1);
      report("vp1 = " + vp1);
      report("vp1.produce() = " + vp1.produce());

      ValueProducer<String> vp2 = createValueGenerator(gen2, vp1);
      report("vp2 = " + vp2);
      report("vp2.produce() = " + vp2.produce());
    }
  
  Output::
  
    vp1 = ValueProducer<String>
    vp1.produce() = Hello!
    vp2 = ValueProducer<String>
    vp2.produce() = Hello, Hello!

.. js:function:: createValueTransform(inputValueProducer, operatorName[, sharedValueProducer])
  
  Creates a value producer that calls the given operator to transform the result of another value producer of the same type.
  
  :param ValueProducer<ValueType> inputValueProducer:
    The input value producer to transform.
  
  :param operatorName:
    The name of the operator to call to transform the value.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ValueProducer<ValueType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        io *ValueType* value,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  Example::
  
    operator multByTwo(
      io Integer value
      )
    {
      value *= 2;
    }
    
    operator multByShared(
      io Integer value,
      Integer shared
      )
    {
      value *= shared;
    }
    
    operator entry() {
      ValueProducer<Integer> vp;
      
      vp = createValueTransform(
        createConstValue( 42 ),
        multByTwo
        );
      report(vp);
      report(vp.produce());
      
      vp = createValueTransform(
        createConstValue( 2 ),
        multByShared,
        createConstValue( 3 )
        );
      report(vp);
      report(vp.produce());
    }
  
  Output::
  
    ValueProducer<Integer>
    84
    ValueProducer<Integer>
    6

.. js:function:: createValueMap(inputValueProducer, operatorName[, sharedValueType])
  
  Creates a value producer that calls the operator *operatorName* to map the result of another value producer, possibly to a value producer of a different type.
  
  :param ValueProducer<InputValueType> inputValueProducer:
    The input value producer whose value to map.
  
  :param operatorName:
    The name of the operator to call to map the value.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ValueProducer<OutputValueType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        in *InputValueType* inputValue,
        io *OutputValueType* outputValue,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  The type *OutputValueType* is inferred from the second parameter of *operatorName*.
  
  Example::
  
    operator multByPi(
      Integer input,
      io Scalar output
      )
    {
      output = 3.14 * input;
    }

    operator multByShared(
      Integer input,
      io Scalar output,
      Scalar shared
      )
    {
      output = input * shared;
    }

    operator entry() {
      ValueProducer<Scalar> vp;
      
      vp = createValueMap(
        createConstValue( 42 ),
        multByPi
        );
      report(vp);
      report(vp.produce());

      vp = createValueMap(
        createConstValue( 2 ),
        multByShared,
        createConstValue( Scalar(2.71) )
        );
      report(vp);
      report(vp.produce());
    }
  
  Output::
  
    ValueProducer<Scalar>
    131.88
    ValueProducer<Scalar>
    5.42

.. js:function:: createValueCache(inputValueProducer)
  
  Creates a value producer that caches the result of another value producer of the same type.  For more information on producer caches, see refer to the Map-Reduce Programming Guide.
  
  :param ValueProducer<ValueType> inputValueProducer:
    The input value producer to cache.
  
  :rtype: ValueProducer<ValueType>
  
  Example::
  
    operator valueGen(
      io Scalar output
      )
    {
      output = 2.71;
      report("Generating output = " + output);
    }
    
    operator entry() {
      ValueProducer<Scalar> vp = createValueCache(createValueGenerator(valueGen));
      report("vp.produce() = " + vp.produce());
      report("vp.produce() = " + vp.produce());
      report("calling vp.flush()");
      vp.flush();
      report("vp.produce() = " + vp.produce());
      report("vp.produce() = " + vp.produce());
    }
  
  Output::
  
    Generating output = 2.71
    vp.produce() = 2.71
    vp.produce() = 2.71
    calling vp.flush()
    Generating output = 2.71
    vp.produce() = 2.71
    vp.produce() = 2.71

Array Producer Creation Functions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. js:function:: createConstArray(arrayExpr)
  
  Creates an array producer that returns constant values.
  
  :param expr:
    The expression to evaluate to obtain the constant array.  The expression must be some sort of KL array (variable-length, fixed-length or external).
  
  :rtype: ArrayProducer<ElementType>
  
  The type *ElementType* is the element type of the the array given by *arrayExpr*.
  
  Example::
  
    operator entry() {
      Integer a[]; a.push(42); a.push(17); a.push(52); a.push(871);
      ArrayProducer<Integer> ap = createConstArray(a);
      report(ap);
      report(ap.getCount());
      report(ap.produce(2));
    }
  
  Output::
  
    ArrayProducer<Integer>
    4
    52

.. js:function:: createArrayGenerator(sizeProducer, operatorName[, sharedValueProducer])
  
  Creates an array producer that calls the operator named *operatorName* to generate the elements of the array.
  
  :param ValueProducer<Size> sizeProducer:
    A value producer that produces a value of type ``Size``.  This value producer is used to determine the size of the array (ie. the number of elements).
  
  :param operatorName:
    The name of the operator to call to generate the elements.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ArrayProducer<ElementType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        io *ElementType* outputElementValue,
        in Size index,
        in Size size,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  The type *ElementType* is inferred from the first parameter of *operatorName*.
  
  Example::
  
    operator generator(
      io Float32 value,
      Size index,
      Size count,
      Float32 shared
      )
    {
      report("generator: value=" + value + " index=" + index + " count=" + count + " shared=" + shared);
      value = shared*index;
    }
    
    operator entry() {
      ValueProducer<Size> cvg = createConstValue(Size(10));
      ArrayProducer<Float32> ag4 = createArrayGenerator(cvg, generator, createConstValue(Float32(3.141)));
      report(ag4);
      report(ag4.getCount());
      for (Size i=0; i<10; ++i)
        report(ag4.produce(i));
    }
  
  Output::
    
    ArrayProducer<Float32>
    10
    generator: value=0 index=0 count=10 shared=3.141
    0
    generator: value=0 index=1 count=10 shared=3.141
    3.141
    generator: value=0 index=2 count=10 shared=3.141
    6.282
    generator: value=0 index=3 count=10 shared=3.141
    9.423
    generator: value=0 index=4 count=10 shared=3.141
    12.564
    generator: value=0 index=5 count=10 shared=3.141
    15.705
    generator: value=0 index=6 count=10 shared=3.141
    18.846
    generator: value=0 index=7 count=10 shared=3.141
    21.987
    generator: value=0 index=8 count=10 shared=3.141
    25.128
    generator: value=0 index=9 count=10 shared=3.141
    28.269

.. js:function:: createArrayTransform(inputArrayProducer, operatorName[, sharedValueProducer])
  
  Creates an array producer that transforms the input array producer by calling the operator named *operatorName* on the individual elements.
  
  :param ArrayProducer<ElementType> inputArrayProducer:
    The input array producer to transform.
  
  :param operatorName:
    The name of the operator to call to transform the elements.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ArrayProducer<ElementType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        io *ElementType* elementValue,
        in Size index,
        in Size size,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  Example::
    
    operator transform(
      io Float32 value,
      Size index,
      Size count,
      Float32 shared
      )
    {
      report("transform: value=" + value + " index=" + index + " count=" + count + " shared=" + shared);
      value *= shared * (index + 1);
    }
    
    operator entry() {
      Float32 inputArray[]; inputArray.push(5.6); inputArray.push(-3.4); inputArray.push(1.4142);
      ArrayProducer<Float32> inputArrayProducer = createConstArray(inputArray);
      ArrayProducer<Float32> transformedArrayProducer = createArrayTransform(inputArrayProducer, transform, createConstValue(Float32(2.56)));
      report(transformedArrayProducer);
      report(transformedArrayProducer.getCount());
      Size transformedArrayProducerCount = transformedArrayProducer.getCount();
      for (Index i=0; i<transformedArrayProducerCount; ++i)
        report(transformedArrayProducer.produce(i));
    }
  
  Output::
  
    ArrayProducer<Float32>
    3
    transform: value=5.6 index=0 count=3 shared=2.56
    14.336
    transform: value=-3.4 index=1 count=3 shared=2.56
    -17.408
    transform: value=1.4142 index=2 count=3 shared=2.56
    10.86106

.. js:function:: createArrayMap(inputArrayProducer, operatorName[, sharedValueProducer])
  
  Creates an array producer that calls the operator *operatorName* to map the elements of another array producer, possibly to an array producer of a different type.
  
  :param ArrayProducer<InputElementType> inputArrayProducer:
    The input array producer whose elements to map.
  
  :param operatorName:
    The name of the operator to call to map the elements.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ArrayProducer<OutputElementType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        in *InputElementType* inputElementValue,
        io *OutputElementType* outputElementValue,
        in Size index,
        in Size size,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  The type *OutputElementType* is inferred from the second parameter of *operatorName*.
  
  Example::
  
    operator map(
      Float32 inputValue,
      io String outputValue,
      Size index,
      Size count,
      Float32 shared
      )
    {
      report("map: inputValue=" + inputValue + " index=" + index + " count=" + count + " shared=" + shared);
      Float32 float32Value = inputValue * shared * (index + 1);
      if (abs(float32Value) < 1.0)
        outputValue = "small";
      else if (abs(float32Value) < 10.0)
        outputValue = "medium";
      else if (abs(float32Value) < 100.0)
        outputValue = "large";
      else
        outputValue = "x-large";
    }
    
    operator entry() {
      Float32 inputArray[]; inputArray.push(5.6); inputArray.push(-0.034); inputArray.push(1.4142);
      ArrayProducer<Float32> inputArrayProducer = createConstArray(inputArray);
      ArrayProducer<String> mappedArrayProducer = createArrayMap(inputArrayProducer, map, createConstValue(Float32(2.56)));
      report(mappedArrayProducer);
      report(mappedArrayProducer.getCount());
      Size mappedArrayProducerCount = mappedArrayProducer.getCount();
      for (Index i=0; i<mappedArrayProducerCount; ++i)
        report(mappedArrayProducer.produce(i));
    }
  
  Output::
  
    ArrayProducer<String>
    3
    map: inputValue=5.6 index=0 count=3 shared=2.56
    large
    map: inputValue=-0.034 index=1 count=3 shared=2.56
    small
    map: inputValue=1.4142 index=2 count=3 shared=2.56
    large

.. js:function:: createArrayCache(inputArrayProducer)
  
  Creates an array producer that caches the result of another array producer of the same type.  For more information on producer caches, refer to the Map-Reduce Programming Guide.
  
  :param ArrayProducer<ElementType> inputArrayProducer:
    The input array producer to cache.
  
  :rtype: ArrayProducer<ElementType>
  
  Example::
  
    operator elementGen(
      io Scalar output,
      Size index
      )
    {
      output = 2.71 * index;
      report("Generating output = " + output);
    }
    
    operator entry() {
      ArrayProducer<Scalar> ap = createArrayCache(
        createArrayGenerator(
          createConstValue(Size(4)),
          elementGen
          )
        );
      report("ap.produce(2) = " + ap.produce(2));
      report("ap.produce(2) = " + ap.produce(2));
      report("calling ap.flush()");
      ap.flush();
      report("ap.produce(2) = " + ap.produce(2));
      report("ap.produce(2) = " + ap.produce(2));
    }
  
  Output::
  
    Generating output = 5.42
    ap.produce(2) = 5.42
    ap.produce(2) = 5.42
    calling ap.flush()
    Generating output = 5.42
    ap.produce(2) = 5.42
    ap.produce(2) = 5.42

Reduce Functions
^^^^^^^^^^^^^^^^

.. js:function:: createReduce(arrayProducer, operatorName[, sharedValueProducer])
  
  Creates a value producer that reduces an array producer to a value producer by calling the operator named *operatorName* to contribute the individual elements to the reduction.
  
  :param ArrayProducer<ElementType> arrayProducer:
    The input array producer to reduce.
  
  :param operatorName:
    The name of the operator to call to transform the elements.
  
  :param ValueProducer<SharedValueType> sharedValueProducer: 
    (optional) Shared value producer to pass to *operatorName*.
  
  :rtype: ValueProducer<ValueType>
  
  The operator *operatorName* must have the following prototype:
  
  .. parsed-literal::
    
      operator *operatorName*\(
        in *ElementType* inputElement,
        io *ValueType* outputValue,
        in Size index,
        in Size size,
        // required if and only if *sharedValueProducer* provided
        in *SharedValueType* sharedValue
        );
  
  Example::
  
    operator generator(
      io Integer outputValue,
      Size index,
      Size size
      )
    {
      outputValue = index + 1;
    }
    
    operator reduce(
      Integer inputValue,
      io Integer outputValue,
      Size index,
      Size size
      )
    {
      report("reduce: inputValue=" + inputValue);
      outputValue += inputValue;
    }
    
    operator entry() {
      ValueProducer<Integer> sum = createReduce(
        createArrayGenerator(
          createConstValue(Size(10)),
          generator
          ),
        reduce
        );
      report("sum.produce() = " + sum.produce());
    }
  
  Output::
  
    reduce: inputValue=1
    reduce: inputValue=2
    reduce: inputValue=3
    reduce: inputValue=4
    reduce: inputValue=5
    reduce: inputValue=6
    reduce: inputValue=7
    reduce: inputValue=8
    reduce: inputValue=9
    reduce: inputValue=10
    sum.produce() = 55
