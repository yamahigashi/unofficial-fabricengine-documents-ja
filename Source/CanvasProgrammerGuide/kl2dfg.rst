.. _canvas-programmer-guide-kl2dfg:

KL2DFG Command line utility
===============================

kl2dfg is a command line executable which allows to generate Canvas preset files for a given KL extension. If successful, it creates a log file called :dfn:`kl2dfg.log` in the destination folder which lists the complete process. To use the resulting presets in Canvas the target folder has to be on the :envvar:`FABRIC_DFG_PATH` environment variable. Alternatively you can also specify a subfolder for an extension to provide Canvas presets using the :code:`dfgPresets` member. Please see :ref:`EAG.fpm` for more information.

To try out KL2DFG, simply open a shell using the Fabric environment variables (see :ref:`GETTINGSTARTED_BASEINSTALLATION`), and type 

.. cmdline:: kl2dfg

kl2dfg supports a series of options, which can be obtained by running kl2dfg with the :dfn:`help` flag

.. cmdline:: kl2dfg --help

Available options:

list
-------
Presents the user with a list of doxygen modifiers which can be used to drive kl2dfg's behavior. Doxygen qualifiers can be used inside the doxygen style comments of a function. For example:

.. code-block:: kl

    /// \dfgPresetTitle MyPresetName
    function Boolean someFunction(Scalar a)

Will cause kl2dfg to pick a different name for the preset than the name of the function. For a full list of qualifiers please use the :dfn:`list` flag.

.. cmdline:: kl2dfg -list

polymorphism
-----------------------
kl2dfg will generate only one preset for methods with the same notation within an extension. For example:

.. code-block:: kl

    function SInt32 Vec3.getMySum() { ... }
    
    function SInt32 Vec4.getMySum() { ... }

Would result in only one Canvas preset file, called :dfn:`Func.getMySum` instead of two separate presets for :dfn:`Vec3` and :dfn:`Vec4`.

.. note:: You can find more information about the consequences of polymorphism here: :ref:`canvas-programmer-guide-polymorphism`.

inheritance
-------------------

Enables the generation of presets for inherited methods. For example:

.. code-block:: kl

  interface i {
    String getName();
  };

  object a : i {
    SInt32 index;
  };

  function a.getName() {
    return 'a'+this.index;
  }

  object b : a {
  };

  function b.reportSomething() {
    report('something');
  }

Without inheritance the presets generated would be:

.. code-block:: bash

    a.getName
    b.reportSomething

With inheritance enabled the presets generated would be:

.. code-block:: bash

    a.getName
    b.getName
    b.reportSomething

can also enable this functionality on a per preset basis by using the :dfn:`dfgUseInheritance` doxygen qualifier.

genAllArrays
-------------------
Enables the generation of array presets for given methods. This makes working with arrays inside of Canvas much easier. You can also enable this functionality on a per preset basis by using the :dfn:`dfgCreateArrayPreset` doxygen qualifier.

.. note:: This functionality might be deprecated in future version of kl2dfg.

addExecutePort
--------------------
For easier daisy chaining of Canvas presets kl2dfg supports to add an extra port as the first port of any Canvas preset.
You can also enable this functionality on a per preset basis by using the :dfn:`dfgAddExecutePort` doxygen qualifier.

Example
------------------
Generating all math presets in a temporary location:

.. cmdline:: kl2dfg $FABRIC_DIR/Exts/Builtin/Math/Math.fpm.json $TEMP
