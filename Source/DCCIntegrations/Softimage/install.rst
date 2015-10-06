Installation
============

The Fabric for Softimage plugin is shipped as a standard workgroup. To load the workgroup simply copy the Fabric for Softimage folder to a location of your choice. Then open the Plugin Manager, click on the Workgroups Tab, and connect to the Workgroup to the chosen location.

.. note::
  Fabric for Softimage contains *Fabric Canvas* as well as the legacy *Fabric Splice*.

Splice (legacy)

To make use of the python client (which is able to access the same splice data through the python interface) the :envvar:`PYTHONPATH` has to include :dfn:`Python/PYTHON_VERSION` subfolder of the Splice Softimage workgroup. Depending on your operating system it might be required to add the location of the FabricCore-|FABRIC_VERSION| library to your :envvar:`PATH` or the :envvar:`LD_LIBRARY_PATH`.
