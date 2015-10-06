.. _SPLICESCRIPTINGACTIONS:

Splice Scripting Interface
==================================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

DCC-Specific Scripting integration
===============================================
Splice provides a scripting interface in a selection of DCCs. The scripting interface will typically use the DCC's main scripting language (for ex: MEL or JavaScript). You can find information about which scripting language to use in the usage section for each DCC's specific documentation. All examples in this document are provided for Maya, however they are very close to each implementation in other DCCs.

The scripting command in each DCC will take four arguments:

  - String action: Name of the action to perform
  - String reference: Full name of the Splice node in the DCC
  - String data: Json string encoding all additional arguments
  - String auxiliary (optional): String providing auxiliary data.

All of the action arguments listed below refer to arguments provided as part of the String data json argument. So for example for :dfn:`registerKLType` the call in maya would look like this:

.. code-block:: python

    from maya import cmds
    cmds.fabricSplice('registerKLType', '', '{"rt": "Vec3"}')

Available Splice Scripting actions
=====================================================

constructClient
--------------------------------------------------------------

No arguments. Constructs a Fabric:Core client, loads the standard extensions. This can be used if you want to deploy the client prior to the creation of the first Splice node / operator.

.. code-block:: python

    cmds.fabricSplice('constructClient')

destroyClient
--------------------------------------------------------------

No arguments. Destroys the Fabric:Core client if it exists. This is not safe to be called if there are still other containers using the client, such as Splice nodes / operators.

.. code-block:: python

    cmds.fabricSplice('destroyClient')

getClientContextID
--------------------------------------------------------------

No arguments. Returns the contextID of the current Fabric:Core client, which is a string containing a unique identifier. This can be used in the C/C++ or python integrations to construct a client sharing the same contextID, which will then allow you to manipulate the same hosted data.

.. code-block:: python

    contextID = cmds.fabricSplice('getClientContextID')
    print contextID

registerKLType
--------------------------------------------------------------

-  String **rt**: Name of the KL type to register
-  String **extension** (optional): Name of the KL Extension to load

Loads, compiles and registers a KL type. This can be used to load KL types outside of the scope of Splice nodes / operators, for example for use within python.

.. code-block:: python

    cmds.fabricSplice('registerKLType', '', '{"rt": "Vec3", "extension": "Math"}')

toggleRenderer
--------------------------------------------------------------

No arguments. Enables / disables the Splice realtime renderer callback.

.. code-block:: python

    cmds.fabricSplice('toggleRenderer')

startProfiling
--------------------------------------------------------------

No arguments. Starts the profiling of the Splice nodes / operators.

.. code-block:: python

    cmds.fabricSplice('startProfiling')

endProfiling
--------------------------------------------------------------

No arguments. Stops the profiling and prints a profiling report to the DCC's script editor.

.. code-block:: python

    cmds.fabricSplice('endProfiling')

setGlobalLoadRTCommand
--------------------------------------------------------------

- String **commandName**: Name of the command to provide KL source code
- String **rtFilter**: Filter for the KL types to be loaded through this command

Setting a global command to load KL types overrides the standard KL loading functionality. Given a rtFilter (for example MyTypes*) the command will be called every time the Fabric:Core tries to load the source code for a given KL type. The command will then have to return the KL source code as a string. This allows you to implement runtime generated types.

.. code-block:: python

    cmds.fabricSplice('registerKLType', '', '{"rtFilter": "MyType", "commandName": "MyLoadRTCommand"}')

addInputPort / addOutputPort / addIOPort
--------------------------------------------------------------

- String **portName**: The name of the port to add
- String **dataType**: The data type to use for the port:
- String **arrayType**: The array type to use fo the port (defaults to single value)
- Boolean **autoInitObjects** - If set KL objects will be initialized on this port automatically.
- String **extension** (optional): Name of the KL Extension to load

Maya specific:

- Boolean **addMayaAttr**: If set the matching maya attribute will be created.
- Boolean **addSpliceMayaAttr**: If set the maya attribute will be created as opaque data.

Adds a new **input**, **output** or **IO** port to the Splice node. The auxiliary script command argument can provide a json string containing the default value for the port.

.. code-block:: python

    cmds.fabricSplice('addInputPort', 'spliceMayaNode1', '{"portName": "a", "dataType": "Scalar", "addMayaAttr": true}')
    cmds.fabricSplice('addOutputPort', 'spliceMayaNode1', '{"portName": "b", "dataType": "Scalar", "addMayaAttr": true}')

removePort
--------------------------------------------------------------

- String **portName**: The name of the port to add

Removes an existing port from a Splice node.

.. code-block:: python

    cmds.fabricSplice('removePort', 'spliceMayaNode1', '{"portName": "a"}')

setDirtyMechanism (Maya specific)
---------------------------------------

- Boolean **enabled**: Defines if the dirtymechanism should be set or not

Enables or disables the Maya specific dirty mechanism. This can be used to increase performance of longer scripts involving several calls to the Splice scripting interface.

.. code-block:: python

    cmds.fabricSplice('setDirtyMechanism', '', '{"enabled": false}')
    # do all of your calls
    cmds.fabricSplice('setDirtyMechanism', '', '{"enabled": true}')

addKLOperator
---------------

- String **opName**: The name of the operator to add
- String **entry** (optional): The name of the entry function to use, defaults to opName
- Dict **portMap** (optional): A string to string dictionary which defines the portmapping

Adds a KL operator to the Splice node. The auxiliary argument of the Splice scripting command is used to store the KL operator's source code.

.. code-block:: python

    cmds.fabricSplice('addKLOperator', 'spliceMayaNode1', '{"opName": "MyOp"}', """
      operator MyOp(Scalar a, io Scalar b) {
        b = 2.0 * a;
      }
    """)

removeKLOperator
------------------

- String **opName**: The name of the KL operator to remove

Removes a KL operator from the Splice node.

.. code-block:: python

    cmds.fabricSplice('removeKLOperator', 'spliceMayaNode1', '{"opName": "MyOp"}')

setKLOperatorCode
--------------------
- String **opName**: The name of the operator to update
- String **entry** (optional): The name of the entry function to use, defaults to opName

Updates the source code of an existing operator. The auxiliary parameter of the Splice scripting command contains the KL source code.

.. code-block:: python

    cmds.fabricSplice('setKLOperatorCode', 'spliceMayaNode1', '{"opName": "MyOp"}', """
      operator MyOp(Scalar a, io Scalar b) {
        b = 17.3 + a;
      }
    """)

getKLOperatorCode
--------------------
- String **opName**: The name of the operator to query

Returns the KL source code of a given operator.

.. code-block:: python

    code = cmds.fabricSplice('getKLOperatorCode', 'spliceMayaNode1', '{"opName": "MyOp"}')
    print code

setKLOperatorFile
----------------------
- String **opName**: The name of the operator to update
- String **entry** (optional): The name of the entry function to use, defaults to opName
- String **fileName**: The file name to use for the KL source file

Sets the KL operator to be referencing an external KL file. The file will be reloaded upon load of the Splice node each time.

.. code-block:: python

    cmds.fabricSplice('setKLOperatorFile', 'spliceMayaNode1', '{"opName": "MyOp", "fileName": "/tmp/test.kl"}')

setKLOperatorEntry
---------------------
- String **opName**: The name of the operator to update
- String **entry**: The name of the entry function to use, defaults to opName

Changes an existing KL operator's entry function name.

.. code-block:: python

    cmds.fabricSplice('setKLOperatorEntry', 'spliceMayaNode1', '{"opName": "MyOp", "entry": "MyEntry"}')

setKLOperatorIndex
---------------------
- String **opName**: The name of the operator to update
- String **index**: The index of the operator on the stack

Moves a KL operator on the operator stack. If the index is out of range an error is raised.

.. code-block:: python

    cmds.fabricSplice('setKLOperatorIndex', 'spliceMayaNode1', '{"opName": "MyOp", "index": 2}')

saveSplice
-------------------
- String **fileName**: The file name to save the splice file to.

Saves an existing Splice node to an external ascii file.

.. code-block:: python

    cmds.fabricSplice('saveSplice', 'spliceMayaNode1', '{"fileName": "/tmp/test.splice"}')

loadSplice
-------------------
- String **fileName**: The file name to load the splice file from.
- Boolean **asReferenced**: If set to true the content of the splice file will not be persisted within the scope of the DCC, but referenced.

Loads a splice port layout and KL operator stack from an existing splice file onto a given Splice node.

.. code-block:: python

    cmds.fabricSplice('loadSplice', 'spliceMayaNode1', '{"fileName": "/tmp/test.splice"}')

getPortInfo
-------------------

No arguments. Returns a json string providing all of the available contextual information on all ports of a Splice node. This includes the port type, mode, corresponding Core DGNode, corresponding Splice DGGraph etc.

.. code-block:: python

    info = cmds.fabricSplice('getPortInfo', 'spliceMayaNode1')
    print info

setPortPersistence
-------------------
- String **portName**: The name of the port to set the persistence for
- Boolean **persistence**: The persistence setting

Overrides the standard persistence setting for a port, allowing users to drive if a port's data will be serialized into the DCC's persistence file.

.. code-block:: python

    cmds.fabricSplice('setPortPersistence', 'spliceMayaNode1', '{"portName": "a", "persistence": true}')

getPortData
-------------------
- String **portName**: The name of the port get the data from

Returns a json string representing the flattened data currently present on a port.

.. code-block:: python

    data = cmds.fabricSplice('getPortData', 'spliceMayaNode1', '{"portName": "v"}')
    print data

setPortData
-------------------
- String **portName**: The name of the port to set the data for

Takes a json string provided as the auxiliary argument of the Splice scripting command and sets it as the current data of a port on a Splice node.

.. code-block:: python

    data = '{"x": 1.0, "y": 2.0, "z": 3.0}'
    cmds.fabricSplice('setPortData', 'spliceMayaNode1', '{"portName": "v"}', data)
