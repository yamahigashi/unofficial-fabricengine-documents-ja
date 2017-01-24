.. _fabricogl_extension:

OpenGL Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The ``FabricOGL`` extension wraps the ``OpenGL`` library and exposes the complete set of functions in KL. 

.. note:: The ``FabricOGL`` extension is not threadsafe, as OpenGL itself isn't either.

The functions in the ``FabricOGL`` extension require a proper OpenGL context to be setup. To test this you can use the :kl-ref:`cpglHaveContext` function. You can find all of the OpenGL functions in the :ref:`FabricOGL/FabricOGL.kl` file.

.. kl-example::

  require FabricOGL;

  operator entry() {
    report( cpglHaveContext() );
  }

To support better debugging you can use the :kl-ref:`cpglSetDebugTrace` function, for proper error checking on every OpenGL call you can use the :kl-ref:`cpglSetAlwaysValidateContext` function. 

.. kl-example::

  require FabricOGL;

  operator entry() {
    cpglSetDebugTrace(true);
    cpglSetAlwaysValidateContext(true);

    // since there is no context, this should fail
    glUseProgram(12);
  }

Generally the C OpenGL functions map directly to KL. For now the ``FabricOGL`` extension does not support OpenGL extensions, only the base set of OpenGL functions is available.

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  functions
  constants

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
