.. _ARNOLD:

Splice in Arnold
=================================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Arnold Splice Procedural
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Arnold Splice
Splice Plugin load previously saved Splice files. The splice file has to contain an output PolygonMesh port, so that Arnold can retrieve the mesh provided by the operation.

.. note:: You can find the source code for SpliceArnold here: http://github.com/fabric-engine/SpliceArnold

Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Splice
Splice Arnold procedural is shipped as a standard plugin library. In order for Arnold to properly find the plugin you will need to add the installation location to the Arnold :dfn:`procedural_searchpath`. The sample which ships with the installation archive relies on the :envvar:`FABRIC_SPLICEARNOLD_ROOT` environment variable to be set. Additionally you will need to set the :envvar:`FABRIC_EXTS_PATH` variable to the Exts folder contained in the installer archive. You can find example KL operator to be used in conjunction with the FabricSplice plugin within the :dfn:`samples` folder of the archive. Depending on your operating system it might be required to add the location of the FabricCore-|FABRIC_VERSION| library to your :envvar:`PATH` or the :envvar:`LD_LIBRARY_PATH`.

Usage
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the FabricSplice procedural with Arnold, you'll need to create a procedural which loads the plugin first. The :dfn:`data` parameter of the procedural has to specify the full path to the splice file to load. For example:

.. code-block:: c++

    procedural
    {
     name splice1
     dso "FabricSpliceArnold"
     data "test.splice"
     load_at_init on
     matrix 
      1 0 0 0
      0 1 0 0
      0 0 1 0
      0 0 0 1 
    }

You may also create user parameters to change the values of input ports of the splice file. This is currently only implemented for INT and FLOAT values. To change a value you'll have to name the user parameter the same as the port within the splice file. Please see the example shipping with the Arnold FabricSplice procedural for further details.

.. note:: On linux you might have to rename the :dfn:`dso` field to :dfn:`libFabricSpliceArnold.so` to load the procedural plugin properly.

Indices and Tables
^^^^^^^^^^^^^^^^^^^^^

* :ref:`genindex`
* :ref:`search`
