.. _GETTINGSTARTED_DCCINSTALLATION:

Installing the Fabric DCC Integrations
=========================================================

As mentioned in the :ref:`GETTINGSTARTED_BASEINSTALLATION` section, |FABRIC_PRODUCT_NAME| relies on several environment variables. These have to be set up differently for each DCC in order to ensure a seamless integration of |FABRIC_PRODUCT_NAME|. This document assumes that the :envvar:`FABRIC_DIR` main environment variable is set to the location of the |FABRIC_PRODUCT_NAME| archive extraction folder. On Windows you can also set these environment variables through the `Control Panel (see this link) <https://www.microsoft.com/resources/documentation/windows/xp/all/proddocs/en-us/sysdm_advancd_environmnt_addchange_variable.mspx?mfr=true>`_. 

.. note:: On Windows, with the standard prompt, use set instead of export. 

Installing Fabric for 3ds Max
---------------------------------------------------------------

Fabric for 3ds Max is distributed as a .dlu plugin and is located in the folder ``<FABRIC-LOCATION>/DCC_Integrations``. Fabric for 3ds Max expects certain environment variables to be set. To simplify the process, a batch file is included in each Fabric3dsmax* folder. Running the batch file should set-up the plugin and launch 3ds Max.


Installing Fabric for Maya
-----------------------------------------------------

The Fabric for Maya plugin is shipped as a standard plugin module. In order for Maya to find the plugin module, the environment variable :envvar:`MAYA_MODULE_PATH` needs to be set before Maya is launched and it should point to the folder which contains the FabricMaya.mod file (which contains the relative paths to the KL Types (RT), Extensions (Exts) and UI files). You can manually set this variable like this:

.. code-block:: bash

  export MAYA_MODULE_PATH=$FABRIC_DIR/DCCIntegrations/FabricMaya<version>

Where `<version>` is the version of Maya being used.

You may of course also use an absolute path, for example:

.. code-block:: bash

  export MAYA_MODULE_PATH=c:/Users/MyUser/Download/FabricEngine-pablo-Windows-x86_64/DCCIntegrations/FabricMaya<version>

.. note:: The absolute path above may not apply to your installation. Also, on Windows, there should be no trailing slash on the MAYA_MODULE_PATH, otherwise Maya may fail to properly locate the plugin.

You can also use the `Maya.env <http://download.autodesk.com/global/docs/maya2014/en_us/index.html?url=files/Environment_Variables_Setting_environment_variables_using_Maya.env.htm,topicNumber=d30e149076>`_ file to set up the MAYA_MODULE_PATH.

Once in Maya, go to Window > Settings/Preferences > Plug-in Manager window to load the FabricMaya plugin.

To make use of the python client the :envvar:`PYTHONPATH` is automatically extended with the :dfn:`Python/PYTHON_VERSION` subfolder of the Maya module. 

.. note:: Maya comes with its own version of PySide (or PySide2 starting in Maya 2017). When launching maya from the console after source the fabric environment this might cause issues. If you experience any hick-ups concerning PySide inside of Maya when launching maya from the console please make sure that the Fabric folders are listed ``after`` the Maya related python folders in the :envvar:`PYTHONPATH`.

Installing Fabric for MODO
---------------------------------------------------------------

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

The 'FABRIC' environment variables (optional):

If the 'FABRIC' environment variables are not set on your system then the plugin will automatically set them temporarily for you.
You might however wish to set them manually, in which case you need to define them as following;

.. code-block:: bash

    export FABRIC_EXTS_PATH=$FABRIC_DIR/Exts
    export FABRIC_DFG_PATH=$FABRIC_DIR/Presets

Most importantly this will also allow you to specify more than one path for extensions and presets, separated by semicolons (Windows) or colons (unix). For example you might have some own Fabric extension that you wish to use as well as some own preset folders to save presets into. Example (Windows):

.. code-block:: bash

    export FABRIC_EXTS_PATH=$FABRIC_DIR/Exts;D:/StudioXYFabric/Exts;C:/Temp/Tests/
    export FABRIC_DFG_PATH=$FABRIC_DIR/Presets;D:/StudioXYFabric/Presets;C:/RnDPresets

Installing Fabric for Softimage
---------------------------------------------------------------

The Fabric for Softimage plugin is shipped as a standard workgroup. To load the workgroup simply open the Plugin Manager, click on the Workgroups Tab, and connect to the Workgroup extracted location.

The 'FABRIC' environment variables (optional):

If the 'FABRIC' environment variables are not set on your system then the plugin will automatically set them temporarily for you.
You might however wish to set them manually, in which case you need to define them as following;

.. code-block:: bash

    export FABRIC_EXTS_PATH=$FABRIC_DIR/Exts
    export FABRIC_DFG_PATH=$FABRIC_DIR/Presets

Most importantly this will also allow you to specify more than one path for extensions and presets, separated by semicolons (Windows) or colons (unix). For example you might have some own Fabric extension that you wish to use as well as some own preset folders to save presets into. Example (Windows):

.. code-block:: bash

    export FABRIC_EXTS_PATH=$FABRIC_DIR/Exts;D:/StudioXYFabric/Exts;C:/Temp/Tests/
    export FABRIC_DFG_PATH=$FABRIC_DIR/Presets;D:/StudioXYFabric/Presets;C:/RnDPresets

To make use of the python client (which is able to access the same data through the python interface) the :envvar:`PYTHONPATH` has to include the :dfn:`Python/PYTHON_VERSION` subfolder of the Fabric for Softimage workgroup. Depending on your operating system it might be required to add the location of the FabricCore-|FABRIC_VERSION| library to your :envvar:`PATH` or the :envvar:`LD_LIBRARY_PATH`.

