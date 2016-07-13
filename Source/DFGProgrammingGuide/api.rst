The DFG API
====================

The DFG API can be accessed through C++ or Python.

The C++ API
-----------------

The C++ DFG API is part of the Fabric Core API (CAPI).  To work with DFGs you first obtain the DFGHost object by calling the Fabric Core client's "getDFGHost()" method.  You can then create bindings to new graphs, which return a DFGBinding object, where you can then do things like addNodeFromPreset(), addPort(), connect() and so on.

Unfortunately, your best bet right now is to refer to FabricCore.h in the DFG classes and also ask Helge for access to the DFG UI repositories.

The Python API
------------------

The Python API is by far the simplest way to use the DFG.

In the Fabric distribution, under the Test/Core/DFG folder, you will find all of our unit tests for the DFG Core API, written in Python.  You can use these as a starting point for using the API.
