KL Implementation
=================

As mentioned previously, the map-reduce model is available in KL. Using the map-reduce model directly from within KL allows for simple multithreading directly from within KL itself, without the need to create structures within the host language.

KL Constant Producers
------------------------

In KL, a constant value producer is created using the :samp:`createConstValue({value})` call. The :samp:`{value}` parameter can be any typed KL r-value, eg. a constant value, the value of a variable, or the result of a function call. The result of the value is a value of type :samp:`ValueProducer<{ValueType}>`, where :samp:`{ValueType}` is the type of :samp:`{value}`. For example, the KL code:

.. code-block:: none
  
  operator entry() {
    ValueProducer<Scalar> vp = createConstValue(1.4142);
    report(vp.produce());
  }

produces the result:

.. code-block:: none
  
  1.4142

A constant array producer is created using the :samp:`createConstArray({array})` function. Its single parameter :samp:`{array}` must be an expression that resolves to a fixed-length, variable-length or external array. The return value is of type :samp:`ArrayProducer<{ElementType}>`, where :samp:`{ElementType}` is the type of the array elements. For example, the KL code:

.. code-block:: none
  
  operator entry() {
    String a[];
    a.push('zero'); a.push('one'); a.push('two');
    ArrayProducer<String> ap = createConstArray(a);
    report(ap.produce());
  }

produces the result:

.. code-block:: none
  
  ["zero","one","two"]

KL Generators
------------------------

A value generator in KL is created using the :samp:`createValueGenerator({functionName})`. :samp:`{functionName}` must be the name of a KL function available in the same KL module that has the operator signature :samp:`{functionName}(io {ValueType} value);` the result is a value of type :samp:`ValueProducer<{ValueType}>`. For example, the KL code:

.. code-block:: none
  
  operator gen(io String value[]) {
    value.push("Hello, world!");
  }
  
  operator entry() {
    ValueProducer<String[]>vp = createValueGenerator(gen);
    report(vp.produce());
  }

produces the output:

.. code-block:: none
  
  ["Hello, world!"]

An array generator in KL is created using the :samp:`createArrayGenerator({countValueProducer}, {functionName})`. The :samp:`{countValueProducer}` parameter must be a value producer that produces a value of type :samp:`Size`, ie. a value of type :samp:`ValueProducer<Size>`. If you are generating a fixed-size array of size 16, for instance, you can pass the result of :samp:`createConstValue(16)`, but you can also pass a more complex value producer such as a value generator. :samp:`{functionName}` is the name of a function in the same module with one of the following prototypes:

.. code-block:: none
  
  operator functionName(io ElementType element);
  operator functionName(io ElementType element, Index index);
  operator functionName(io ElementType element, Index index, Size count);

In cases where the index parameter is present, the index of the element within the array is passed to the generator function; similarly, when the count parameter is present the total number of elements in the array is passed. This can be useful for figuring out what value to generate.

An example of an array generator:

.. code-block:: none
  
  operator gen(
    io Scalar v,
    Index i,
    Size n
    )
  {
    // Produces n uniform values on the interval [0,1], including 0 and 1 themselves
    v = Scalar(i) / Scalar(n-1);
  }
  
  operator entry() {
    ArrayProducer<Scalar> ap = createArrayGenerator(createConstValue(Size(10)), gen);
    report(ap.produce());
  }

produces:

.. code-block:: none
  
  [0,0.1111111,0.2222222,0.3333333,0.4444444,0.5555556,0.6666667,0.7777778,0.8888889,1]

In both cases, you can optionally specify a shared value producer as the last parameter to the :samp:`create...Generator()` call. When a shared value producer is provided, the function receives an additional parameter whose type is the value type of the shared value producer. So, for value generators, the prototype of the operator becomes:

.. code-block:: none
  
  operator gen(io ValueType value, SharedType sharedValue) {
    ...
  }

and for array generators the prototype of the operator becomes:

.. code-block:: none
  
  operator gen(io ElementType element, Index index, Size count, SharedType sharedValue) {
    ...
  }

Note that when using a shared value with an array generator you must include the index and count parameters in the operator even if they are unused.

KL Maps
------------------------

A value map in KL is created using the :samp:`createValueMap({inputValueProducer}, {functionName})`. :samp:`{inputValueProducer}` must be a value producer, and :samp:`{functionName}` must be the name of a KL function available in the same KL module that has the operator signature :samp:`{functionName}({InputType} input, io {OutputType} output);` the type :samp:`InputType` must be the same as the value type of the input value producer. The result of the :samp:`createValueMap` call is a value of type :samp:`ValueProducer<{OutputType}>`. For example, the KL code:

.. code-block:: none
  
  operator map(String input, io Size output) {
    output = input.length;
  }
  
  operator entry() {
    ValueProducer<Size> vp = createValueMap(createConstValue("Hello, world!"), map);
    report(vp.produce());
  }

produces the output:

.. code-block:: none
  
  13

An array map in KL is created using the :samp:`createArrayMap({inputArrayProducer}, {functionName})`. The :samp:`{inputArrayProducer}` parameter must be an array producer. Assuming that the element type of :samp:`{inputArrayProducer}` is :samp:`{InputType}`, :samp:`{functionName}` is the name of a function in the same module with one of the following prototypes:

.. code-block:: none
  
  operator functionName(InputType input, io OutputType output);
  operator functionName(InputType input, io OutputType output, Index index);
  operator functionName(InputType input, io OutputType output, Index index, Size count)

In cases where the :samp:`index` parameter is present, the index of the element within the array is passed to the generator function; similarly, when the count parameter is present the total number of elements in the array is passed. The result of the :samp:`createArrayMap` call is a value of type :samp:`ArrayProducer<{OutputType}>`.

An example of an array map:

.. code-block:: none
  
  operator map(String input, io Size output) {
    output = input.length;
  }
  
  operator entry() {
    String a[]; a.push("one"); a.push("two"); a.push("three");
    ArrayProducer<String> iap = createConstArray(a);
    report(iap.produce());
    ArrayProducer<Size> oap = createArrayMap(iap, map);
    report(oap.produce());
  }

produces:

.. code-block:: none
  
  ["one","two","three"]
  [3,3,5]

In both cases, you can optionally specify a shared value producer as the last parameter to the :samp:`create...Map()` call. When a shared value producer is provided, the function receives an additional parameter whose type is the value type of the shared value producer. So, for value maps, the prototype of the operator becomes:

.. code-block:: none
  
  operator gen(InputType input, io OutputType output, SharedType sharedValue) {
    ...
  }

and for array maps the prototype of the operator becomes:

.. code-block:: none
  
  operator gen(
    in InputType input,
    io OutputType output,
    in Index index,
    in Size count,
    in SharedType sharedValue
    )
  {
    ...
  }

Note that when using a shared value with an array map you must include the :samp:`index` and :samp:`count` parameters in the operator even if they are unused.

KL Transforms
------------------------

A value transform in KL is created using the :samp:`createValueTransform({inputValueProducer}, {functionName})`. :samp:`{inputValueProducer}` must be a value producer, and :samp:`{functionName}` must be the name of a KL function available in the same KL module that has the operator signature :samp:`{functionName}(io {ValueType} value)`; the type :samp:`{ValueType}` must be the same as the value type of the input value producer. The result of the :samp:`createValueMap` call is a value of type :samp:`ValueProducer<{ValueType}>`. For example, the KL code:

.. code-block:: none
  
  operator transform(io Scalar value) {
    value = sqrt(value);
  }
  
  operator entry() {
    ValueProducer<Scalar> vp = createValueTransform(createConstValue(Scalar(3.14)), transform);
    report(vp.produce());
  }

produces the output:

.. code-block:: none
  
  1.772004

An array transform in KL is created using the :samp:`createArrayTransform({inputArrayProducer}, {functionName})`. The :samp:`{inputArrayProducer}` parameter must be an array producer. Assuming that the element type of :samp:`{inputArrayProducer}` is :samp:`{ElementType}`, :samp:`{functionName}` is the name of a function in the same module with one of the following prototypes:

.. code-block:: none
  
  operator functionName(io ElementType element);
  operator functionName(io ElementType element, Index index);
  operator functionName(io ElementType element, Index index, Size count);

In cases where the :samp:`{index}` parameter is present, the index of the element within the array is passed to the generator function; similarly, when the :samp:`{count}` parameter is present the total number of elements in the array is passed. The result of the :samp:`createArrayTransform` call is a value of type :samp:`ArrayProducer<{ElementType}>`.

An example of an array transform:

.. code-block:: none
  
  operator transform(io Scalar value) {
    value = sqrt(value);
  }

  operator entry() {
    Scalar ia[]; ia.push(3.14); ia.push(2.71); ia.push(10.0); ia.push(87.32);
    ArrayProducer<Scalar> iap = createConstArray(ia);
    report(iap.produce());
    ArrayProducer<Scalar> oap = createArrayTransform(iap, transform);
    report(oap.produce());
  }

produces:

.. code-block:: none
  
  [3.14,2.71,10,87.32]
  [1.772004,1.646208,3.162278,9.344517]

In both cases, you can optionally specify a shared value producer as the last parameter to the :samp:`create...Transform()` call. When a shared value producer is provided, the function receives an additional parameter whose type is the value type of the shared value producer. So, for value maps, the prototype of the operator becomes:

.. code-block:: none
  
  operator gen(io ValueType value, SharedType sharedValue) {
    ...
  }

and for array maps the prototype of the operator becomes:

.. code-block:: none
  
  operator gen(io ElementType element, Index index, Size count, SharedType sharedValue) {
    ...
  }

Note that when using a shared value with an array map you must include the :samp:`index` and :samp:`count` parameters in the operator even if they are unused.

KL Reduce Operations
------------------------

To create a reduce operation in KL, use the :samp:`createReduce({inputArrayProducer}, {functionName})` call. :samp:`{inputArrayProducer}` must be an array producer; assume its element type is :samp:`{InputType}`. :samp:`{functionName}` must be the name of a function in the same module with one of the prototypes:

.. code-block:: none
  
  operator functionName(InputType input, io OutputType output);
  operator functionName(InputType input, io OutputType output, Index index);
  operator functionName(InputType input, io OutputType output, Index index, Size count);

The result of the :samp:`createReduce` call is a value producer with value type :samp:`{OutputType}`, ie. a result of type :samp:`ValueProducer<{OutputType}>`. An example of using a reduce operation in KL:

.. code-block:: none
  
  operator generate(io Size value, Index index) {
    value = index + 1;
  }

  operator reduce(Size input, io Size output) {
    output += input;
  }

  operator entry() {
    // Report the sum 1+2+...+99+100
    ValueProducer<Size> vp = createReduce(
      createArrayGenerator(
        createConstValue(Size(100)),
        generate
      ),
      reduce
    );
    report(vp.produce());
  }

This produces the result:

.. code-block:: none
  
  5050

You can optionally specify a shared value producer as the last parameter to the :samp:`createReduce()` call. When a shared value producer is provided, the function receives an additional parameter whose type is the value type of the shared value producer. The prototype of the operator becomes:

.. code-block:: none
  
  operator reduce(
    in InputType input,
    io OutputType output,
    in Index index,
    in Size count,
    in SharedType sharedValue
    ) {
    ...
  }

Note that when using a shared value with an array map you must include the :samp:`{index}` and :samp:`{count}` parameters in the operator even if they are unused.

KL Caches
------------------------

A value cache is created in KL using the :samp:`createValueCache({inputValueProducer})` call. The element type of the resulting value producer is the same as that of :samp:`{inputValueProducer}`. Example usage of a value cache in KL:

.. code-block:: none
  
  operator gen(io String output) {
    report("  Running generator!");
    output = "Hello";
  }

  operator entry() {
    // test caching ValueGenerator
    ValueProducer<String> vp1 = createValueCache(createValueGenerator(gen));
    report("vp1 = " + vp1);
            
    report("Should run generator");
    report("vp1.produce() = " + vp1.produce());
                
    report("Should not run generator (use cache)");
    report("vp1.produce() = " + vp1.produce());
                    
    vp1.flush();
    report("Should run generator");
    report("vp1.produce() = " + vp1.produce());
  }

resulting in:

.. code-block:: none
  
  vp1 = ValueProducer<String>
  Should run generator
    Running generator!
  vp1.produce() = Hello
  Should not run generator (use cache)
  vp1.produce() = Hello
  Should run generator
    Running generator!
  vp1.produce() = Hello

Similarly, an array cache is created using the :samp:`createArrayProducer({inputArrayProducer})` call. The resulting array producer has the same element type as :samp:`{inputArrayProducer}`. Example usage:

.. code-block:: none
  
  operator generator(
    io Integer value
    )
  {
    report("  Running generator");
    value = 42;
  }
  
  operator entry() {
    // Generator caching
    ValueProducer<Size> cvg = createConstValue(Size(10));
    ArrayProducer<Integer> gen = createArrayCache(
      createArrayGenerator(cvg, generator)
      );
  
    report(gen);
    report(" gen.getCount() = " + gen.getCount());
  
    report("Should run generator 10x");
    for (Index i=0; i<10; ++i)
      report(" gen.produce() = " + gen.produce(i));
  
    report("Should not run generator (cached)");
    for (Index i=0; i<10; ++i)
      report(" gen.produce() = " + gen.produce(i));
  
    gen.flush();
    report("Should run generator 10x");
    for (Index i=0; i<10; ++i)
      report(" gen.produce() = " + gen.produce(i));
  }

resulting in:

.. code-block:: none
  
  ArrayProducer<Integer>
   gen.getCount() = 10
  Should run generator 10x
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
    Running generator
   gen.produce() = 42
  Should not run generator (cached)
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
   gen.produce() = 42
  Should run generator 10x
    Running generator
   gen.produce() = 42
    Running generator
    Running transform
   tr.produce() = 2
    Running transform
   tr.produce() = 4
    Running transform
   tr.produce() = 6
    Running transform
   tr.produce() = 8
    Running transform
   tr.produce() = 10
    Running transform
   tr.produce() = 12
    Running transform
   tr.produce() = 14
    Running transform
   tr.produce() = 16
    Running transform
   tr.produce() = 18

