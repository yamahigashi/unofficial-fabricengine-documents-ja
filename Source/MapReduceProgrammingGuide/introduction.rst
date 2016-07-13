Introduction
============

In addition to the dependency graph model of parallel programming, |FABRIC_PRODUCT_NAME| provides a separate model of parallel programming called "Map-Reduce" that is inspired by models of parallelism provided by functional programming languages and commercial MapReduce frameworks for large-scale computing. The map-reduce functionality is available from within the KL language. It is simple to use, provides highly-parallel performance and incurs a minimal memory overhead.

Background
----------------

Traditionally, the map-reduce paradigm provides a simple way of performing parallel operations on large sets of data. The input to map-reduce is a large array of data whose elements are of a common type, and the output is a single value of another type. The output is produced from the input by performing the following steps:

- For each input element :samp:`{Xi}` in the input array :samp:`[{X1},{X2},...{Xn}]`, the value :samp:`{Mi} = map({Xi})` is computed. This can be done for the input elements in parallel.

- The result :samp:`{R} = reduce([{M1},{M2},...,{Mn}])` is computed by combining the results of the map operations.

The canonical example of a map-reduce operation is to count the number of occurrences of a given word in a large set of documents (for simplicity, strings). Then the :samp:`map({Xi})` operation counts the number of occurrences of the word in the string :samp:`{Xi}`, and the :samp:`reduce([{M1},{M2},...,{Mn}])` operation simply sums the results of all the :samp:`{Mi}`.

There are several problems with map-reduce in its simplest form:

- The individual :samp:`{Xi}` themselves might be values that need to be computed and/or that take a lot of memory. As such, it makes sense to retrieve (or compute) the value :samp:`{Xi}` right before computing :samp:`map({Xi})` and then to immediately throw away the value of :samp:`{Xi}`.

- Instead of computing :samp:`reduce([{M1},{M2},...,{Mn}])` once all the :samp:`{Mi}` are computed, we use less memory and make better use of parallelism by accumulating the result. First we initialize :samp:`{R}` to a default value, and then as each :samp:`{Mi}` is computed we compute :samp:`{R} = reduce({R}, {Mi})`. Once this is done for all the :samp:`{Mi}`, we return the resulting :samp:`{R}`. We must use a mutex to guarantee that :samp:`reduce({R}, {Mi})` is only ever executed by one thread at a time.

|FABRIC_PRODUCT_NAME| addresses these issues as well as others to provide a more general framework for parallel computation inspired by the traditional map-reduce case.

Concepts
----------------

Map-reduce in |FABRIC_PRODUCT_NAME| has a more generic and powerful implementation that arises from a core set of concepts and operations. The traditional map-reduce case is then just a specific case of what can be done with the |FABRIC_PRODUCT_NAME| map-reduce framework. All of the concepts and operations are available both within KL programs and are accessible using the host language interface to the |FABRIC_PRODUCT_NAME|.

Producers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The first concept is the notion of a producer. A :dfn:`producer` is a first-class object whose methods can be used to produce scalar and vector values; these values can be any of the built-in KL types, any registered (user-defined) types, or even more producers.  For more information about built-in KL types see the chapter "The KL Type System" of the :ref:`KLPG`.

For more information about registered types in |FABRIC_PRODUCT_NAME| see :ref:`DGPG.registered-types` in the :ref:`DGPG`.

There are two classes of producers in |FABRIC_PRODUCT_NAME|, described below.

Value Producers
"""""""""""""""""""""""""

A :dfn:`value producer` is a producer that can produce a scalar value; it has the method :samp:`produce()` that returns the value, as well as the method :samp:`flush()` that flushes any cached values (see the section :ref:`caches`).

Array Producers
"""""""""""""""""""""""""

An :dfn:`array producer` is a producer that can produce an array (vector) of elements; it has five methods:


- :samp:`getCount()`: returns the number of elements in the array

- :samp:`produce({index})`: returns the element of the array with index :samp:`{index}` 

- :samp:`produce({startIndex}, {count})`: returns the subarray of :samp:`{count}` elements of the array starting with index :samp:`{startIndex}` 

- :samp:`produce()`: returns the array of all elements

- :samp:`flush()`: flushes any cached values (see the section :ref:`caches`).

The indices are zero-based, as in KL. All the the array elements have the same type; in a strong sense, an array producer is an object that can be used to populate a variable-length KL array.

Note that an array producer specifies how to produce the elements of an array without actually producing them. This means that you can create an array produce for an array with billions of elements and it takes no more memory than an array producer for one element; it's only when the elements are produced that the results may be stored, depending on how the results are used.

The :samp:`produce()` and :samp:`produce({startIndex}, {count})` methods produce the individual elements of the array in parallel.

Types of Producers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each class (value or array) of producer, there are four basic types of producers that produce values in different ways.

Constant Producers
"""""""""""""""""""""""""

A constant producer has fixed values that are produced. It does not need to execute any code to produce its values, and the values it produces are specified when the constant producer is created.

Generators
"""""""""""""""""""""""""

A generator is a producer that calls a function to produce its value. In the case of an array producer, the function that is called can optionally receive the index within the array and the total number of elements of the array; these can be used to calculate the element to generate. Both value and array producers can optionally take a "shared value" which can be used to pass things like shared parameters to the generator. The shared value is itself the result of calling :samp:`produce()` on a value producer, which means that it can itself potentially be a calculated value.

Maps
"""""""""""""""""""""""""

A map is a producer that takes as input a value of one type and produces from it a value of another, potentially different, type. An example of a simple map might be one that takes a string as input and produces the length of the string as output. As with generators, an array map can optionally take the index of the element being produced as well as the count of the array, and both value and array maps can take a shared value.

Transforms
"""""""""""""""""""""""""

A transform is a producer that modifies the value of another producer. The same behavior could be accomplished using a map that uses the same type for input and output, but using a transform instead will require less memory and generally result in slightly better runtime performance. An example of a simple transform might be one that normalizes a vector. As with generators and maps, an array transform can optionally take the index of the element being produced as well as the count of the array, and both value and array transforms can take a shared value.

Reduce
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The reduce operation is the bridge between array producers and value producers. A reduce operation takes an array producer and a function as input and returns a value producer as output. The reduce operation works by calling the function for each element produced by the array producer; this function is then used to progressively produce the result of reduce operation as a value producer. There are two guarantees for the function:

- The function is called exactly once for each element of the input array producer; and

- The function is called by only one thread at a time so that no manual synchronization is necessary.

However, the order in which the elements of the array producer is undefined, and as such algorithms cannot depend on this order.

As with generators, maps and transforms, the reduce function can optionally take the index of element of the input array producer as well as its total count, and you can optionally pass a shared value.

A simple example of a reduce operation would be to sum an array of values. The array producer would produce the individual values, and the reduce function would simply add each value to the result.

.. _caches:

Caches
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A cache is a producer that simply caches the value of another producer. Caches are a simple solution for situations where the same results would be computed multiple times. As an example, if multiple producers all used the same shared value producer, it would probably make sense to put a value cache in front of the value producer so that it's not recomputed every time it's used.

All producers support a method called :samp:`flush()` that recursively flushes any caches. So, for example, if you have a reduce operation that uses a shared value that is cached, calling :samp:`flush()` on the reduce operation will flush the connected shared value cache.

Composing Producers and Reduce Operations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The power of the |FABRIC_PRODUCT_NAME| map-reduce model is found through the use of composition. Maps, transforms and reduce operations all take other producers as input and allow modification of the results. As well, generators, maps, transforms and reduce operations all optionally take shared values that are the results of the :samp:`produce()` operation of a value producer; this value produce can in turn be a complex, composed operation such as a reduce operation on a map.

As an example, suppose you had a large set of documents and you wanted to count the occurrence of the longest word that occurs across all the documents; assume for the example that there is a unique longest word. You need to first figure out what this word is and then count it. The compositional model would be:

.. code-block:: none
  
  reduce(
    input: map(
      input: constArray(documents),
      function: countWord,
      sharedValue: reduce(
        input: map(
          input: constArray(documents),
          function: findLongestWord
          ),
        function: pickLongestWord
      ),
    function: sumValue
    )

Then the functions would look something like:

.. code-block:: none
  
  operator findLongestWord(String document, io String longestWord) {
    // Set longestWord to the longest word in document
  }
  
  operator pickLongestWord(String word, io String longestWord) {
    if (word.length > longestWord.length)
      longestWord = word;
  }
  
  operator countWord(String document, io Size count, String word) {
    // Set count to the number of occurrences of word in document
  }
  
  operator sumValue(Size count, io Size totalCount) {
    totalCount += count;
  }
