.. _FabricForMaya.pre-2.0:

Using the Splice Maya plugin (legacy)
======================================

.. note:: The Splice Maya (pre-2.0) feature are still supported in 2.0, but might be deprecated in future release.

Launch Maya and load the Splice plugin, you should see a new entry in the top menus which says :dfn:`Splice`. In order to start using the Splice Editor UI you need to create a Splice Maya node, to do so just open the Splice top menu and create a spliceMayaNode. Open maya's Attribute Editor and click the button Open Splice Editor.

If the Splice Editor was already open it will simply refresh to point at the currently selected node once you click the button in the Attribute Editor.

In order to make the node's interface compatible with a KL operator you need to add some attributes and ports, to do so you can use the Splice Editor and click on the button Add located under the Contained Ports part of the Editor.

.. note:: A Splice Node uses Ports to store and retrieve KL data, Ports can be accessed within KL operators. If a Maya Attribute is added with the same name of a Port then the Port's data is automatically synchronized with the Maya attribute's data, the KL Port data will transfered in and out of maya depending if the Port was set as input or output. Once the interface of the node is defined in terms of ports and attributes you can add a KL operator from the Splice Editor Add button, under the Contained Operators part of the UI. When the operator is created the KL editor will show it along with the ports interface to interact with it.

.. note:: KL Operators are global to the scope of Creation Splice, they don't belong exclusively to the node they've been created for and they can be applied to every Splice Maya node that has a compatible interface.

That's it for the spliceMayaNode overview, have fun playing inside the body of the KL operator, if new to the KL language please refer to the :ref:`KLPG`.

.. _nodetypes:

Maya Nodes Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Splice Maya plugin comes with three node types, the :dfn:`spliceMayaNode` is a generic MPxNode where you can attach almost every kind of maya attribute type, it will be suited for any generic computation such as rigging or simulation solvers.

The :dfn:`spliceMayaDeformer` is a deformer node that seamlessly works with maya's deformation tools and commands, it comes with two arrays of points, one as input and another for the output, any other necessary attribute can still be added to this node once instantiated.

The :dfn:`spliceMayaDebugger` allows for custom OpenGL drawings generated inside a KL operator to be visualized inside maya's 3D viewport. Drawing inside a KL operator is done by using the InlineGeometryType.

.. _mayascripting:

Scripted Splice
^^^^^^^^^^^^^^^^^^^

Anything done with the Splice Editor graphical interface can also be automated in MEL and Python via the fabricSplice command, thus offering the possibility to include Splice nodes in scripted procedural rigs or other kind of automated scene setups. Referencing external KL files is also possible via the fabricSplice command, this could be useful to have KL operators under source control or share them with other people or simply to take advantage of external code editors. Once a scene is saved the code of eachKL operator is also stored along with the path to the KL file, on scene loading the code of the operator will be used if the specified KL file is not found anymore.

For a full list of scripting actions and parameters, please see the :ref:`SPLICESCRIPTINGACTIONS` section.

The following examples show how to interact with the fabricSplice command with Python syntax:

.. code-block:: python

    from maya import cmds
    
    # creating a node and attaching an operator
    node = cmds.createNode('spliceMayaNode')
    
    cmds.fabricSplice('addInputPort', node, '{"portName":"in1", "dataType":"Scalar", "addMayaAttr":true}')
    cmds.fabricSplice('addInputPort', node, '{"portName":"in2", "dataType":"Scalar", "addMayaAttr":true}')
    cmds.fabricSplice('addOutputPort', node, '{"portName":"out", "dataType":"Scalar", "addMayaAttr":true}')
    cmds.fabricSplice('addKLOperator', node, '{"opName":"helloWorldOp"}', """
    operator helloWorldOp(Scalar in1, Scalar in2, io Scalar out) {
      report('computing KL in maya!');
      report(in1 + " + " + in2);
      out = in1 + in2;
    }
    """)
    
    cmds.setAttr(node + '.in1', 1.0)
    cmds.setAttr(node + '.in2', 2.0)
    print cmds.getAttr(node + '.out') == 3.0
    
    # referencing an external KL operator file
    cmds.fabricSplice('setKLOperatorFile', node, '{"opName":"helloWorldOp", "fileName":"/somePath/helloWorldOp.kl"}')

Port UI Limits
^^^^^^^^^^^^^^^^^^^^

Any unconsumed flag added to the :dfn:`addInputPort`, :dfn:`addOutputPort` or :dfn:`addIOPort` actions will be setup as 
additional flag data on the resulting ports. This data will also be persisted with the maya scene or with exported splice files.

Some of the optional flags are used for UI hints, for example :dfn:`uiMin`, :dfn:`uiMax`, :dfn:`uiSoftMin` and :dfn:`uiSoftMax`.
With these you can define slider ranges for :dfn:`Integer` or :dfn:`Scalar` ports.

.. code-block:: python

    cmds.fabricSplice('addInputPort', node, '{"portName":"slider", "dataType":"Scalar", "addMayaAttr":true, "uiMin": -10.0, "uiMax": 10.0}')

Compound Attributes
^^^^^^^^^^^^^^^^^^^^^^^^^

.. versionadded:: 1.12.0

Using the :ref:`compoundparam` KL type maya compound attributes can now be transfered to and from Splice. :ref:`compoundparam` objects are a way of describing hierarchical parameters. With this version we support all of the basic types, excluding geometries such as MFnMesh etc.

The actual compound attribute is not created by Splice however, it needs to be created by the maya user (or responsible scripts). The Splice conversion layer will then turn the data into the right nested data structure in KL. Of course :ref:`compoundparam` objects supported hierarchical nesting, so you can put a :ref:`compoundparam` into another :ref:`compoundparam`.

.. code-block:: python

    import maya.cmds as cmds
    import maya.OpenMaya as OpenMaya
    import maya.OpenMayaMPx as OpenMayaMPx

    node = cmds.createNode('spliceMayaNode')
    cmds.select(node, r=True)

    # setup the compound attribute
    cmds.addAttr(node, ln='values', at='compound', nc=4)
    cmds.addAttr(node, ln='a', at='bool', p='values')
    cmds.addAttr(node, ln='b', at='long', p='values')
    cmds.addAttr(node, ln='c', at='float', p='values')
    cmds.addAttr(node, ln='d', at='double3', p='values')
    cmds.addAttr(node, ln='dX', at='double', p='d')
    cmds.addAttr(node, ln='dY', at='double', p='d')
    cmds.addAttr(node, ln='dZ', at='double', p='d')

    # create a port for the compound
    cmds.fabricSplice('addIOPort', node, '{"portName":"values", "dataType":"CompoundParam", "addMayaAttr":false}')    
    cmds.fabricSplice('addOutputPort', node, '{"portName":"result", "dataType":"Scalar", "addMayaAttr":true}')    

    # create a KL operator for it
    cmds.fabricSplice('addKLOperator', node, '{"opName": "testCompoundOp"}', '''
    require Parameters;

    operator testCompoundOp(io CompoundParam values) {
      for(Size i=0;i<values.paramCount();i++) {
        Param param = values.getParam(i);
        report(param.getName()+' is of type '+param.getValueType());
      }
    }
    ''')

    # the expected output is as follows:
    # [KL]: [FABRIC:MT:mayaGraph_DGNode:testCompoundOp] a is of type Boolean // 
    # [KL]: [FABRIC:MT:mayaGraph_DGNode:testCompoundOp] b is of type SInt32 // 
    # [KL]: [FABRIC:MT:mayaGraph_DGNode:testCompoundOp] c is of type Float64 // 
    # [KL]: [FABRIC:MT:mayaGraph_DGNode:testCompoundOp] d is of type Vec3 // 

Aside from using MEL commands to generate the compound, you can also use json. With this second approach the compound structure will also be persisted as part of the splice file. The json elements for each compound support the very same flags as the port generating commands. Also you can nest compounds as well. Finally with this approach you can also create arrays of compounds by using an array as the data type.

.. code-block:: python

    import json
    import maya.cmds as cmds
    import maya.OpenMaya as OpenMaya
    import maya.OpenMayaMPx as OpenMayaMPx

    node = cmds.createNode('spliceMayaNode')
    cmds.select(node, r=True)

    # setup the compound attribute
    compound = json.dumps({
      "a": {"dataType": "Boolean"},
      "b": {"dataType": "Integer", "uiMin": 1.0, "uiMax": 4.0},
      "c": {"dataType": "Scalar"},
      "d": {"dataType": "Vec3"},
    })

    # create a port for the compound
    cmds.fabricSplice('addIOPort', node, '{"portName":"values", "dataType":"CompoundParam", "addMayaAttr":true}', compound)
    cmds.fabricSplice('addOutputPort', node, '{"portName":"result", "dataType":"Scalar", "addMayaAttr":true}')

    # create a KL operator for it
    cmds.fabricSplice('addKLOperator', node, '{"opName": "testCompoundOp"}', '''
    require Parameters;

    operator testCompoundOp(io CompoundParam values) {
      for(Size i=0;i<values.paramCount();i++) {
        Param param = values.getParam(i);
        report(param.getName()+' is of type '+param.getValueType());
      }
    }
    ''')


Deformers
^^^^^^^^^^^^^^^^^^^^

Use the standard deformer command to create a node of type spliceMayaDeformer:

.. code-block:: python

    cmds.deformer(type = "spliceMayaDeformer")

A spliceMayaDeformer uses a :ref:`polygonmesh` array port, the name has to be "meshes".

.. code-block:: python

    cmds.fabricSplice('addOutputPort', 'spliceMayaDeformer1', '{"portName":"meshes", "dataType":"PolygonMesh[]"}')

    operator testDeformer(io PolygonMesh meshes[]) {
      meshes[0].setPointPosition(0, Vec3(1,2,3));
    }

Procedural Geometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Splice Maya Nodes can also generate procedural geometry by adding a PolygonMesh output port and attribute, which will allow Splice to build the Maya mesh with optimal performance.

.. code-block:: kl

    require Math;
    require PolygonMesh;
    
    operator geomGen(Scalar factor, io PolygonMesh geo) {
      geo.clear();
    
      Vec3 profile[];
      profile.push(Vec3(3, 0, 1));
      profile.push(Vec3(4, 0, 2));
      profile.push(Vec3(7, 0, 3));
      profile.push(Vec3(1, 0, 4));
    
      Xfo xfos[];
      xfos.push(Xfo());
      Xfo inc;
      inc.tr.y = 1.0;
      inc.ori.setFromEulerAngles(Vec3(0.2 * factor, 0.4 * factor, 0.1 * factor));
      for(Size i=0;i<30;i++)
        xfos.push(xfos[i] * inc);
    
      geo.addExtrusion(xfos, profile, false);
      geo.recomputePointNormals(0.4);
      
      geo.addShell(0.25);
      geo.recomputePointNormals(0.4);
    }


Custom KL DataTypes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When working with complex networks of Splice Maya Nodes you might want to also pass complex KL data structures from one node to another, 
this is easily achieved by registering a new KL extension. KL extension can contain pure KL code (aside from the ones providing binary libraries). To define a new KL extension, simply implement a series KL files (or just one) and add a fpm.json file to the same folder. The fpm.json file may look like this:

.. code-block:: klon

  {
    "code": [
      "myKLFile1.kl",
      "myKLFile2.kl"
    ]
  }

To register a new extension location, first set a path to be scanned for KL files using the environment variable :envvar:`FABRIC_EXTS_PATH`, do that before to launch maya.
Any fpm.json file in that path containing a struct will be registered and the Kl struct will be made available inside KL operators.

.. note:: Your KL files will need to be named accordingly to the name of the struct they will contain. Ex. MyStruct.kl defines: struct MyStruct{}; 

To add a maya attribute capable of holding a Registered Type just use the fabricSplice maya command as follows:

.. code-block:: python

    cmds.fabricSplice('addInputPort', "mySpliceMayaNodeName", '{"portName":"myStructAttrIn", "dataType":"MyStruct", "addMayaAttr":true, "addSpliceMayaAttr": true}')
    cmds.fabricSplice('addOutputPort', "mySpliceMayaNodeName", '{"portName":"myStructAttrOut", "dataType":"MyStruct", "addMayaAttr":true, "addSpliceMayaAttr": true}')

Custom Registered Types can also be used to just hold some data even if it's not intended to be passed to another node.
To do that just add an output port using the fabricSplice command without specifying to add a maya attribute as well:

.. code-block:: python

    cmds.fabricSplice('addIOPort', "mySpliceMayaNodeName", '{"portName":"myStructAttrIn", "dataType":"MyStruct", "addMayaAttr":false}')

SpliceMayaData - Opaque KL Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Custom KL types can be setup to be opaque to Maya. This way you can connect several of these attributes using the Maya graph, but Maya
itself won't know what the content of the data is. For this, as seen above, you need to use the :dfn:`addSpliceMayaAttr` flag when adding a port.

.. code-block:: python

    cmds.fabricSplice('addInputPort', "mySpliceMayaNodeName", '{"portName":"myStructAttrIn", "dataType":"MyStruct", "addMayaAttr":true, "addSpliceMayaAttr": true}')

This flag will cause the attribute to be of type :dfn:`SpliceMayaData`.

.. note:: One caveat to keep in mind is that all SpliceMayaData ports can be interconnected, even if the data structures they wrap are not compatible.

Accessing Port Layout
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since a splice node in maya can contain more ports than mapped attributes a scripting facility is provided to gain access to that information. The portInfo string is JSON encoded and provides the same information which is also used during persistence of a splice file.
    
.. code-block:: python

    portInfo = cmds.fabricSplice('getPortInfo', "mySpliceMayaNodeName")

Manipulating Port Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use ports inside a splice node as caches for internal data structures. This is extremely useful when certain parts of the computation should not be driven by splice itself, but by some external script. The data is provided as JSON strings, and can therefore reflect any data structure accessible within splice (excluding opaque data). Given the example of a 'Vec3' port called 'myVec', this is how you can set the data. Setting the data also enables the persistence of that port, so the set data will be saved alongside the maya scene.

.. code-block:: python

    cmds.fabricSplice('setPortData', 'mySpliceMayaNodeName', '{"portName":"myVec"}', '{"x":1,"y":2,"z":3}')

To gain access to the data again, you can use another action of the fabricSplice command like below. Not that getting of data works on all ports, while setting of data only works for IN and IO ports.

.. code-block:: python

    data = cmds.fabricSplice('getPortData', 'mySpliceMayaNodeName', '{"portName":"myVec"}')

Maya Python FabricCore Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aside from manipulating data through JSON and making use of getPortData and setPortData, you can also use the new python client which ships with Splice for Maya. You'll need to make sure that the python subfolder of the maya module is part of the :envvar:`PYTHONPATH`. The first Splice node will create the FabricCore client, but you can also manage the creation and destruction of the client manually - for example if there is no splice maya node in the scene yet.

.. code-block:: python

    import json
    from maya import cmds
    import FabricEngine.Core

    #create a client - will be ignored if it already exists
    cmds.fabricSplice("constructClient")

    # get the client id from splice 
    contextID = cmds.fabricSplice("getClientContextID")

    # create a python client 
    client = FabricEngine.Core.createClient({'contextID':contextID})

Once the client exists, you can use it to do anything the core can do, of course. One especially useful facility however is getting access to RTVals stored within Splice nodes. This is even more efficient with KL object RTVals, since they are just referenced and never copied into python. This allows you to build custom UI, for example, which can interact with members within a RTVal inside a Splice port, and even call methods on them.

.. code-block:: python

    # create a splice node with a mesh
    spliceNode = cmds.createNode("spliceMayaNode")
    cmds.fabricSplice("addInputPort", spliceNode, '{"portName":"dummy", "dataType": "Integer", "addMayaAttr": true}')
    cmds.fabricSplice("addOutputPort", spliceNode, '{"portName":"mesh", "dataType": "PolygonMesh", "addMayaAttr": true}')

    # create a mesh 
    mesh = client.RT.types.PolygonMesh.create()

    # create some topology (this calls into KL) 
    # first arg empty string marks return type 
    mesh.createPoints("", 3)
    mesh.setPointPosition('', 0, client.RT.types.Vec3(-1, 0, 1))
    mesh.setPointPosition('', 1, client.RT.types.Vec3(1,0,-1))
    mesh.setPointPosition('', 2, client.RT.types.Vec3(1,0,1))
    mesh.beginStructureChanges("") 
    mesh.addPolygon("", 0, 1, 2) 
    mesh.endStructureChanges("")

    # you could now use this mesh within a splice node 
    infos = cmds.fabricSplice('getPortInfo', spliceNode, '{"portName":"mesh"}') 
    infos = json.loads(infos)
    for info in infos:
      if info['name'] == 'mesh':
          break
    dgNodeName = info['graph'] + '_' + info['node'] 
    member = info.get('member', info['name']) # default to name if member not provided
    dgNode = client.DG.getNodeByName(dgNodeName)

    # set the RTVal in the splice node's core member 
    dgNode.setValue(member, 0, mesh)
    # increment the dummy member to force maya
    # to evaluate the node again
    cmds.setAttr(spliceNode+'.dummy', 12)

    # pipe the mesh into a maya mesh
    meshNode = cmds.createNode('mesh')
    cmds.connectAttr(spliceNode+'.mesh', meshNode+'.inMesh')

Dirty Mechanism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Do avoid the execution of Splice's internal dirty mechanism, you can disable it during an execution of script. This will speed up the performance of scripts since any update will happen at the end of the script only.

.. code-block:: python

    cmds.fabricSplice("setDirtyMechanism", spliceNode, '{"enabled": false"}')

    ... do you stuff ...

    cmds.fabricSplice("setDirtyMechanism", spliceNode, '{"enabled": true"}')

Forcing Port Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default splice in maya will only store those ports that have simple types and that are not arrays. 
This behavior can be overridden with a special command if a complex port needs to be persisted in the scene:

.. code-block:: python

    cmds.fabricSplice('addOutputPort', 'mySpliceMayaNodeName', '{"portName":"myCache", "dataType":"Vec3[]", "addMayaAttr":false, "arrayType":"Array (Multi)"}')
    cmds.fabricSplice('setPortPersistence', 'mySpliceMayaNodeName', '{"portName":"myCache", "persistence":true'})

Exporting Splice files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To export the ascii representation of a Maya Splice node, simply select the node in the hypergraph or in the node editor and hit :dfn:`Export Splice Node` in the :dfn:`Fabric:Splice` top menu. This will save a text file containing the full description of a splice node, including it's ports and KL operators.

Importing Splice files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To load a previously saved Fabric:Splice file, simply select a new spliceMayaNode node in the hypergraph or in the node editor and hit :dfn:`Import Splice Node` in the :dfn:`Fabric:Splice` top menu. This will load the splice file and create all of the ports, KL operators and Maya attributes.
