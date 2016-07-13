.. _fabricstatistics_extension:

FabricStatistics Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The ``FabricStatistics`` extension wraps a singleton statistics collector which can efficiently collect and
synthesize custom statistics and profiling information. Through a thread-safe singleton, statistic source objects 
and profiling events can be recorded at any time from KL code.

The FabricStatistics extension has been designed for both simplicity of usage and to minimize overhead. 
In particular, most of the work for analyzing statistics and profiling events is delayed until a final report is requested.

.. _fabricstatistics:

Statistics
__________

The FabricStatistics extension can collect custom statistics and information for any registered objects, from any KL source code (extension, operator...). 
It supports object hierarchies, which simplifies the reports, and allows to sum values through the hierarchy (eg: memory usage).

Statistics collection for an object is enabled through the implementation of the :kl-ref:`StatisticSource` interface.
Through the :kl-ref:`StatisticSource.getStatistics` method, the object can submit any statistics or information that 
can be useful for further analysis. The implementation of the :kl-ref:`StatisticSource` can be simplified by using 
the :kl-ref:`StatisticsAutoRegisterMember` helper object, as seen in the example below.

In order to be registered by the FabricStatistics extension, objects implementing the :kl-ref:`StatisticSource` interface must 
call :kl-ref:`RegisterToFabricStatistics` in their constructor(s), and :kl-ref:`UnregisterFromFabricStatistics` in their destructor. 
Again, this process can be simplified and made more robust by using the :kl-ref:`StatisticsAutoRegisterMember` helper. 

Statistic source objects will be recorded only if statistics have been previously enabled by a call to the :kl-ref:`EnableFabricStatistics` function.
Statistic source objects that were constructed before a call to :kl-ref:`EnableFabricStatistics` will not be monitored, so it is recommended 
to enable statistics before the scene gets populated.

If a :kl-ref:`StatisticSource` has some sub-objects that are themselves a :kl-ref:`StatisticSource` (eg: `PolygonMesh` has a `GeometryAttributes` container), 
this relationship must be explicitly recorded by calling the :kl-ref:`AddStatisticsChild` function.

.. warning::

  Failing to unregister an object in its destructor can lead to a crash, since the FabricStatistics extension only keeps 
  a `Ref<>` (unowned) of the object in order to avoid leaks (else, the object would never destroyed). Again, this can be
  avoided by using the :kl-ref:`StatisticsAutoRegisterMember` helper.

Statistics returned by an object through the :kl-ref:`StatisticSource.getStatistics` method are simple name / value pairs, 
embedded in a :kl-ref:`StatisticRecord`. Support statistic value types include `String`, `SInt64` and `Float64`. Although 
returned statistics can be arbitrary (eg: `Image` returning its `width` and `eight``), there are some standard fields:

- "Name" (the `Statistic_Name` constant): objects should provide a name, as this is the best way to identify an object in the statistics report.

- "Category" (the `Statistic_Category` constant): this allows to regroup objects of different types in the statistics report for more clarity.

- "Type" (the `Statistic_Type` constant): the KL type of the source. This one doesn't have to be provided, as it is 
  automatically generated using the ``.type()`` KL feature. The statistics report can regroup objects of the same type for more clarity.

- "Memory" (the `Statistic_MemoryUsage` constant): the main memory usage for an object. If the object has sub-objects 
  that implement themselves the StatisticSource interface, these should not be included in the "Memory", but 
  rather registered as children objects (using the :kl-ref:`AddStatisticsChild` function). By default, the "Memory" 
  statistic will get summed through the hierarchy in the final report. Since KL doesn't provide (yet) facilities for 
  retrieving actual memory usage, this has to be estimated manually.

- "GPUMemory" (the `Statistic_GPUMemoryUsage` constant): similar to "Memory" (above), but for the GPU (eg: OpenGL buffer objects).

.. kl-example::

  require FabricStatistics;

  object MyObject : StatisticSourceWithAutoRegisterMember {
      String name;
      Float32 scalars[];

      StatisticsAutoRegisterMember autoStats;
    };

  function MyObject() {
    if( FabricStatisticsEnabled() ) //Reduce overhead if stats are turned off
      this.autoStats = StatisticsAutoRegisterMember(this);
  }

  function StatisticRecord[] MyObject.getStatistics() {
    StatisticRecord stats[];
    stats.push(StatisticRecord(Statistic_Name, this.name));
    stats.push(StatisticRecord(Statistic_MemoryUsage, this.scalars.size()*4 ));
    return stats;
  }

  operator entry() {

    EnableFabricStatistics();

    MyObject obj1();
    obj1.name = "obj1";
    obj1.scalars.resize(10);

    MyObject obj2();
    obj2.name = "obj2";
    obj2.scalars.resize(20);

    MyObject obj3();
    obj3.name = "obj3";
    obj3.scalars.resize(30);

    //Make obj3 a children of obj2
    AddStatisticsChild(obj2.autoStats, obj3.autoStats);

    report( GetStatisticsReport() );
  }

Statistics for all registered objects and their hierarchy can be retrieved by calling functions such as 
:kl-ref:`GetStatisticStrings` and :kl-ref:`GetStatisticsCSV`. In order to minimize runtime overhead, 
statistic source objects' :kl-ref:`StatisticSource.getStatistics` methods are only called when 
the statistic report is built. Information about destroyed objects is not retained.

The report can generate the sum of some statistics (eg: "Memory"). The list of 
the statistics to sum through the object hierarchies is provided by the `ColumnsToSum` argument in functions such as :kl-ref:`GetStatisticStrings`.

.. note::

  The :kl-ref:`FabricStatistics_RTValWrapper` object simply wraps the `FabricStatistics` global functions so they can 
  be accessible through `RTVals` (global functions are not accessible because of a limitation)

.. _fabricstatisticsprofiling:

Profiling
__________

The FabricStatistics extension provides some facility for recording custom profiling events. 
FabricStatistics profile events are mostly useful for tracking specific details, 
for example breaking operators into multiple steps, identified with custom tags. The FabricStatistics 
profile events can be nested, and the hierarchy of events will be recorded.

Submitted profiling events will only be recorded if profiling is enabled by a call to 
:kl-ref:`StartFabricProfiling` or :kl-ref:`StartFabricProfilingFrames`.

Profiling events need to be bracketed through a call to :kl-ref:`BeginProfilingEvent` and :kl-ref:`EndProfilingEvent`.
The `key` returned by :kl-ref:`BeginProfilingEvent` must be passed to the corresponding :kl-ref:`EndProfilingEvent`. 
When applicable, events can refer a :kl-ref:`StatisticSource` object in order to provide more information.
The :kl-ref:`AutoProfilingEvent` struct can simplify profiling events recording since it will automatically 
call :kl-ref:`EndProfilingEvent` upon destruction.

All recorded events from the last profiling session can be retrieved by calling :kl-ref:`GetProfilingEvents` or :kl-ref:`GetProfilingReport`.

.. kl-fileexample:: ${FABRIC_SCENE_GRAPH_DIR}/Test/Exts/Statistics/CPUProfiling.kl


Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  interfaces
  types
  functions
  constants

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
