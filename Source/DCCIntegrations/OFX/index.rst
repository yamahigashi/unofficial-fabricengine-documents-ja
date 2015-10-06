.. _OFX:

Splice through OpenFX
=======================================

.. image:: /images/Splice/Splice_logo.png
   :width: 360px
   :height: 57px

| Splice version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The OpenFX Fabric:Splice Plugin can perform per pixel operations using KL.

.. note:: You can find the source code for SpliceOFX here: http://github.com/fabric-engine/SpliceOFX

Installation / Usage
^^^^^^^^^^^^^^^^^^^^^^^^

The Splice OFX plugin is shipped as a standard plugin library. In order for a OFX host to properly find the plugin the environment variable :envvar:`OFX_PLUGIN_PATH` needs to be set to the parent folder of the install location before the host app is launched. Once in the host app you can should see plugin. Depending on the host app you should then be able to create an effect or a node called "FabricSplice". The OFX plugin doesn't support a procedural UI for now, so it's limited to 5 Scalar ports and 5 Color ports. Additionally you will need to set the :envvar:`FABRIC_EXTS_PATH` variable to the Exts folder contained in the installer archive. You can find example KL operator to be used in conjunction with the Splice plugin within the :dfn:`samples` folder of the archive.

Indices and Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* :ref:`genindex`
* :ref:`search`
