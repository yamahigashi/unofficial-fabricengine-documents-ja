Installation
============

The Fabric for MODO plugin is shipped as a kit and is located in the folder ``<FABRIC-LOCATION>/DCC_Integrations``.
To install the Fabric for MODO kit:

#. start MODO.

#. in the main menu choose "System -> Run Script ...".

#. use the file dialog to open the file called ``setup_script.py``. It can be found in the folder ``<FABRIC-LOCATION>/DCC_Integrations/FabricModo``.

#. a second file dialog will appear. Use it to open the same file (i.e. ``setup_script.py``) again.

#. now a message box appears informing you that Fabric has been set up.

#. close the message box and re-start MODO.

#. test the installation by loading the sample scene ``<FABRIC-LOCATION>/Samples/Modo/PolygonMesh_Push_plus_Cubes.lxo``. Once the scene is loaded select the locator called 'move_me_around' and move it around. You should see a push effect on the torus.

.. note::
  The first time the plugin is launched, all the provided extensions will be built for the target platform on multiple CPUs. This may take a few minutes.

