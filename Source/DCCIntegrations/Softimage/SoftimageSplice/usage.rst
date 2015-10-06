Using the Splice Softimage plugin
==============================================================

In order to start using the Splice Editor UI, click on the Fabric Menu and choose :dfn:`Splice Editor`

To create a new Splice operator you need to first pick the element in the scene to output to. Currently allowed elements are kinematic states and polygon mesh primitives. You may select multiple kinematic states / objects and right click to end the picking session.

Once the SpliceOp is created you can re-open the Splice Editor UI by selecting the operator and clicking the :dfn:`Splice Editor` menu entry from the Fabric menu again.

With the Splice Editor UI open you can add :dfn:`parameters` to the SpliceOp (standard Softimage parameters which are stored on the custom operator), additional :dfn:`XSI ports` (port connections to kinematic states or polygon mesh primitives) or so called :dfn:`Cache Ports` (internal ports which don't communicate with Softimage). When performing a picking session please follow the instructions stated in the status bar, and hit right click to end a picking session.

Furthermore, Splice supports accessing values off the ICE system. For that use the :dfn:`Add ICE Port` button, pick a name for the Splice port and define the name of the ICEAttribute you want to read. Then choose the right geometry storing the attribute during the picking session.

Aside from interacting with Ports you can also edit the KL operator stack on each SpliceOp. You may add, remove or edit KL operators. New KL operators will receive some auto generated KL code which makes accessing previously defined ports easier. Hitting the 'Edit' button will set the edited KL operator on the :dfn:`KL` tab.

.. note:: KL Operators are global to the scope of Splice, they don't belong exclusively to the node they've been created for and they can be applied to every SpliceOp that has a compatible interface. This means you should choose the name fo the KL operators consciously. If all KL operators are called 'testOp', this will create conflicts.

That's it for the SpliceOp overview. If you are new to the KL language please refer to the :ref:`KLPG`.

Scripting a SpliceOp and Referencing KL Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Anything done with the Splice Editor graphical interface can also be automated through scripting via the fabricSplice command, thus offering the possibility to include SpliceOp in scripted procedural rigs or other kind of automated scene setups. Referencing external KL files is also possible via the fabricSplice command, this could be useful to have KL operators under source control or share them with other people or simply to take advantage of external code editors. Once a scene is saved the code of eachKL operator is also stored along with the path to the KL file, on scene loading the code of the operator will be used if the specified KL file is not found anymore.

For a full list of scripting actions and parameters, please see the :ref:`SPLICESCRIPTINGACTIONS` section.

The following examples show how to interact with the fabricSplice command with JScript syntax:

.. code-block:: kl

    // creating the operator
    var op = fabricSplice("newSplice", '{"targets":"null.kine.global","portName":"output"}');

    // creating a standard port, a parameter and an internal port
    fabricSplice("addInputPort", op, '{"targets":"null1.kine.global,null2.kine.global","portName":"matrices","dataType":"Mat44[]"}');
    fabricSplice("addParameter", op, '{"portName":"blend","dataType":"Scalar"}');
    fabricSplice("addInternalPort", op, '{"portName":"debugGeo","dataType":"InlineGeometryType","portMode":"io"}');

    // creating a KL operator
    fabricSplice("createKLOperator", op, '{"opName":"myCustomConstraint"}');
    var klCode = [
      "require Xfo, Mat44;",
      "operator myCustomConstraint(Scalar blend, Mat44 matrices[], io Mat44 output) {",
      "  Xfo a(matrices[0]);",
      "  Xfo b(matrices[1]);",
      "  output = a.linearInterpolate(b, blend).toMat44();",
      "}"
    ];
    fabricSplice("setKLOperatorCode", op, '{"opName":"myCustomConstraint"}', klCode.join("\n"));

    // changing the blend value
    SetValue(op+".blend", 0.5);
      
    // referencing an external KL operator file
    // fabricSplice("setKLOperatorFile", op, '{"opName":"myCustomConstraint", "fileName":"C:/temp/myCustomConstraint.kl"}');

Generative Procedural Geometry
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Splice operators can also generate procedural geometry by adding a PolygonMesh output port which will allow Splice to build the polygon mesh with optimal performance.

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

Gaining access to the information about the internal ports
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Since a SpliceOp in Softimage can contain more ports than mapped attributes, a scripting facility is provided to gain access to that information. The portInfo string is JSON encoded and provides the same information which is also used during persistence of a splice file.
    
.. code-block:: kl

    var op = "null.kine.global.SpliceOp";
    var portInfo = fabricSplice("getPortInfo", op);
    LogMessage(portInfo);

Manipulating internal port data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can use ports inside a splice node as caches for internal data structures. This is extremely useful when certain parts of the computation are not driven by splice, but by some external script. The data is provided as JSON strings, and can therefore reflect any data structure accessible within splice (excluding opaque data). Given the example of a 'Vec3' port called 'myVec', this is how you can set the data. Setting the data also enables the persistence of that port, so the set data will be saved alongside the maya scene.

.. code-block:: kl

    var op = "null.kine.global.SpliceOp";
    fabricSplice('setPortData', op, '{"portName":"myVec"}', '{"x":1,"y":2,"z":3}');

To gain access to the data again, you can use another action of the fabricSplice command like below. Not that getting of data works on all ports, while setting of data only works for IN and IO ports.

.. code-block:: kl

    var op = "null.kine.global.SpliceOp";
    var data = fabricSplice('getPortData', op, '{"portName":"myVec"}');
    LogMessage(data);



Accessing Port values as RTVals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One especially useful facility is getting access to RTVals stored within Splice nodes. This is even more efficient with KL object RTVals, since they are just referenced and never copied into python. This allows you to build custom UIs, for example, which can interact with members within a RTVal inside a Splice port, and even call methods on them.

.. code-block:: python

    var op = "null.kine.global.SpliceOp";

    #create a client - will be ignored if it already exists
    Application.fabricSplice('constructClient')

    # get the client id from splice
    contextID = Application.fabricSplice('getClientContextID')

    # Create a shared client that enabled us to access all the Splice data.
    client = FabricEngine.Core.createClient({'contextID':contextID})
     
    # Get the json description of all the ports. 
    portInfo = json.loads(Application.fabricSplice("getPortInfo", op))

    for portIndex in range(len(portInfo)):
      dgnodeName = str(portInfo[portIndex]['graph']) + '_'+ str(portInfo[portIndex]['node'])
      dgnode = client.DG.getNodeByName(dgnodeName)
      # Pull out the port value. From here we can quiry its value/members and call methods on it.
      portValue = dgnode.getValue(portInfo[portIndex]['member'], 0)
      print "PortValue:" + str(portValue)



Forcing nodes to store a port on disk:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default splice in maya will only store those ports that have simple types and are not arrays. 
This behavior can be overridden with a special command if a complex port needs to be persisted in the scene:

.. code-block:: kl

    var op = "null.kine.global.SpliceOp";
    fabricSplice('setPortPersistence', op, '{"portName":"myVec","persistence":true}');

Exporting Splice files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To export the ASCII representation of a SpliceOp, open the Splice Editor with the output target selected and hit :dfn:`Save Splice`. This will save a text file containing the full description of a Splice node, including it's ports and KL operators.

Importing Splice files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To load a previously saved Splice file, go the Fabric menu and choose :dfn:`Load Splice`.This will open a user interface to pick the targets for each port. You can pick each element by selecting a cell in the grid view and hitting 'Pick Target'. You may also create the default objects for particular ports through this UI.
