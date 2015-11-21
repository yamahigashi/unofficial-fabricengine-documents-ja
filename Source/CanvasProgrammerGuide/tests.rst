.. _test_graph:

Testing a graph
===============================

In order to automatize tests on Canvas graphs/presets, the following python script can be used.
It reads a :ref:`.canvas` graph and executes it.

.. code-block:: python

  ### Execute '*.canvas' graph 
  # To use the script : python DFGTest.py graph.canvas
  # Set the PYTHONPATH environment variable as : export PYTHONPATH=$PYTHONPATH:PATH-TO-FABRIC-PYTHON

  import FabricEngine.Core, sys, os
   
  # Check the number of argument, should be >= 2
  if(len(sys.argv) < 2) :
    print 'There is no canvas file to test'
    sys.exit(0)
    
  # Check if the file exists and is canvas
  if not os.path.isfile(sys.argv[1]) or not sys.argv[1].endswith('.canvas'):
    print 'There is no canvas file to test'
    sys.exit(0)

  # Create a Fabric client
  client = FabricEngine.Core.createClient()
    
  # Open the file, load the graph and execute it
  f = open(sys.argv[1]) 
  binding = client.DFG.host.createBindingFromJSON( str(f.read()) );
  binding.execute()
    
  # Close the client
  client.close()

