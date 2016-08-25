Core Instrumentation Interface
==============================

The lowest-level access to the Fabric Engine instrumentation interface is through the :samp:`startInstrumentation` and :samp:`stopInstrumentation` methods that are available on Fabric client objects.

The :samp:`startInstrumentation` Method
--------------------------------------------

The :samp:`startInstrumentation` method tells Fabric Engine to start collecting instrumentation data.  It takes no parameters.  Calling this function a second time in a row has no effect.  Instrumentation data will continue to be collected until the :samp:`stopInstrumentation` method is called.

The :samp:`stopInstrumentation` Method
--------------------------------------------

The :samp:`stopInstrumentation` method tells Fabric Engine to stop collecting instrumentation data and returns the collected instrumentation data.  It takes a single parameter whose value specifies the format of the data that is returned; it should be one of the following values:

:samp:`"raw"`
  Return the raw instrumentation data.  The format for this data is described below.

:samp:`"svg"`
  Return the data as an SVG-formatted string that is suitable for display in any SVG-enabled display widget.

The Raw Data Format
-------------------

The result of the :samp:`stopInstrumentation` method when passed the :samp:`"raw"` argument is the raw instrumentation data.  Its format is as follows:

- An array of :dfn:`thread objects` each of which are an object with the following members:
  
  - An :samp:`"n"` member whose value, a string, is the name of the thread (eg. :samp:`"Worker Thread 1"`)
  
  - An :samp:`"s"` member whose value is an array of :dfn:`time records`.  Each sub-array time record specifies Fabric Engine accounted for while instrumenting, and the time records happened immediately after each other in the order of the array.  Each time record is itself an array with the following elements, in order:
    
    - A :dfn:`duration` value (floating-point) measured in seconds
    
    - A :dfn:`description` value (string)
    
    - A :dfn:`nesting depth` value (non-negative integer), used internally by the time record keeping mechanism
    
    - A :dfn:`category` value indicating where the operation was happening, having one of the following values:
      
      
      :samp:`0`
        Time spent was external to Fabric (ie. by the dynamic language) or used by a worker thread while idle
      
      :samp:`1`
        Time spent was internal to the Fabric Engine core itself but not in user code
      
      :samp:`2`
        Time spent was in user code (ie. KL operators)
      
      :samp:`2`
        Time spent was in an extension.  NOTE: as of this writing this category is currently not used and all time spend in extensions shows up in the user category.

Example
-------

.. code-block:: none
  
  $ python 
  Python 2.7.1 (r271:86832, Jul 31 2011, 19:30:53) 
  [GCC 4.2.1 (Based on Apple Inc. build 5658) (LLVM build 2335.15.00)] on darwin
  Type "help", "copyright", "credits" or "license" for more information.
  >>> import json
  >>> import FabricEngine.Core as fabric
  [FABRIC] Fabric Engine Core version |FABRIC_VERSION|
  >>> fabricClient = fabric.createClient()
  [FABRIC] Searching extension directory '/Users/pzion/Library/Fabric/Exts'
  [FABRIC] [FabricALEMBIC] Extension registered
  [FABRIC] [FabricBULLET] Extension registered
  ...
  [FABRIC] [FabricVIDEO] Extension registered
  [FABRIC] [TimeSample] Extension registered
  [FABRIC] Searching extension directory '/Library/Fabric/Exts'
  [FABRIC] Warning: unable to open extension directory '/Library/Fabric/Exts'
  >>> fabricClient.startInstrumentation(); json.dumps(fabricClient.stopInstrumentation("raw"))
  '[{"s": [[0.000253727, "dynamic language", 0, 0], [4.105e-05, "|FABRIC_PRODUCT_NAME|", 1, 1]], "n": "Main Thread"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 1"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 2"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 3"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 4"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 5"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 6"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 7"}, {"s": [[0.000294777, "scheduler (idle)", 0, 0]], "n": "Worker Thread 8"}]'
  >>> fabricClient.startInstrumentation(); fabricClient.stopInstrumentation("svg") 
  u'<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n<svg wid  ...  hor="middle" y="0.3692485019564629in" alignment-baseline="middle" font-family="Helvetica" font-size="12" >\nscheduler (idle)  </text>\n</svg>\n'
  >>> quit()
  mbp:Core pzion$ 
