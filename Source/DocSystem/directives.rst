Documentation System Sphinx Directives
==========================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

* :ref:`kl_example_directive`: A kl example which can be executed directly in sphinx
* :ref:`kl_fileexample_directive`: A kl file based example which can be executed directly in sphinx
* :ref:`kl_css_directive`: A nestable css directive for overriding the look and feel of sphinx per directive while auto-creating refs.
* :ref:`kl_constant_directive`: Doc-Gen for a KL constant.
* :ref:`kl_function_directive`: Doc-Gen for a free KL function
* :ref:`kl_interface_directive`: Doc-Gen for a KL interface
* :ref:`kl_inheritance_directive`: Doc-Gen for a KL inheritance diagram
* :ref:`kl_type_directive`: Doc-Gen for a KL type (struct or object)
* :ref:`kl_method_directive`: Doc-Gen for a single KL method
* :ref:`kl_methodlist_directive`: Doc-Gen for a list of KL methods (all for a type, or a category of methods)
* :ref:`kl_ext_constantlist_directive`: Doc-Gen for a list of all constants within an extension.
* :ref:`kl_ext_interfacelist_directive`: Doc-Gen for a toctree of all interfaces within an extension.
* :ref:`kl_ext_typelist_directive`: Doc-Gen for a toctree of all types within an extension.
* :ref:`kl_ext_functionlist_directive`: Doc-Gen for a all free functions within an extension.

.. _kl_example_directive:
The kl-example directive
---------------------------
The kl-example directive is used to embed a snipped of KL code into the page. This snipped is actually invoked and the output is collected. You may also use the nooutput option to disable the kl output.

.. code-block:: rst

    .. kl-example:: Math-Test

      require Math;

      operator entry() {
        Vec3 a(1,2,3);
        Vec3 b(4,5,6);
        report(a + b);
      }

.. _kl_fileexample_directive:
The kl-fileexample directive
----------------------------------
The kl-fileexample is the same as the kl-example directive, just that it uses an input filepath. You can use ${ENVVAR} notations to express environment variables.

.. code-block:: rst

    .. kl-fileexample:: ${FABRIC_SCENE_GRAPH_DIR}/Tests/Singletons/Singletons_Test1.kl

.. _kl_css_directive:
The kl-css directive
--------------------------
The kl-css directive embeds another block into a paragraph with a css class applied. The css can be implemented in :dfn:`_static/custom.css`. The only allowed and required argument is the name of the css class to apply. The kl-css directive will also auto generate kl-ref directives for any types found within the content, so that KL types become clickable.

.. code-block:: rst

    .. kl-css:: plaintext

      In this example we are mentioning a Vec3 as well as a Mat44.

.. _kl_constant_directive:
The kl-constant directive
-------------------------------
The kl-constant directive is used to reference the documentation generation for a KL constant.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* createrefs: (0(default) or 1): when enabled the sphinx reference for this constant is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* brief: (0 or 1(default)): include the brief description of the element
* plaintext: (0 or 1(default)): include the plain text description of the element
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst)
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample)

.. code-block:: rst

    .. kl-constant:: MAX_NAME_LENGTH
      title=0;
      createrefs=1;

.. _kl_function_directive:
The kl-function directive
---------------------------------
The kl-function directive is used to reference the documentation generation for a KL free function.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* createrefs: (0(default) or 1): when enabled the sphinx reference for this function is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* params: (0(default) or 1): include the documentation of all function parameters
* brief: (0 or 1(default)): include the brief description of the element
* plaintext: (0 or 1(default)): include the plain text description of the element
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst)
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample)

.. code-block:: rst

    .. kl-function:: radToDeg
      params=1;
      createrefs=1;

.. _kl_interface_directive:
The kl-interface directive
-----------------------------
The kl-interface directive is used to reference the documentation generation for a KL interface.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* createrefs: (0(default) or 1): when enabled the sphinx reference for this interface is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* methods: (0 or 1(default)): include the documentation of all interface methods
* brief: (0 or 1(default)): include the brief description of the element
* plaintext: (0 or 1(default)): include the plain text description of the element
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst)
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample)

.. code-block:: rst

    .. kl-interface:: MyInterface
      methods=1;
      createrefs=0;

.. _kl_inheritance_directive:
The kl-inheritance directive
-----------------------------------
The kl-inheritance directive is used to generate an inheritance graph.

.. code-block:: rst

    .. kl-inheritance:: MySpecializedObject

.. _kl_method_directive:
The kl-method directive
------------------------------
The kl-method directive is used to reference the documentation generation for a KL method.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* createrefs: (0(default) or 1): when enabled the sphinx reference for this method is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* params: (0(default) or 1): include the documentation of all method parameters
* brief: (0 or 1(default)): include the brief description of the element
* plaintext: (0 or 1(default)): include the plain text description of the element
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst)
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample)

.. code-block:: rst

    .. kl-method:: MyObject.getS

.. _kl_methodlist_directive:
The kl-methodlist directive
--------------------------------
The kl-methodlist directive is used to reference the documentation generation for a list of KL methods.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* createrefs: (0(default) or 1): when enabled the sphinx reference for each method is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* compact: (0(default) or 1): compact version of the method list, without any additional documentation (example or such).
* includeinherited: (0 or 1(default)): when enabled all inherited methods are shown
* includeprivate: (0(default) or 1): when enabled private methods are also shown
* category: (String): the category of methods to list (operators for operators, empty string for all)
* brief: (0 or 1(default)): include the brief description for each method
* plaintext: (0 or 1(default)): include the plain text description for each method
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst) for each method
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample) for each method

.. code-block:: rst

    .. kl-methodlist:: MyStruct
      category=operators;
      example=0;
      brief=0;
      plaintext=1;

Compact list for Vec4 methods:

.. code-block:: rst

    .. kl-methodlist:: Vec4
      compact=1;

.. _kl_type_directive:
The kl-type directive
----------------------------
The kl-type directive is used to reference the documentation generation for a KL type (struct or object).

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* createrefs: (0(default) or 1): when enabled the sphinx reference for this type is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* inheritancegraph: (0 or 1(default)): enables showing an inheritance graph
* members: (0 or 1(default)): include data type members
* methods: (0 or 1(default)): include the documentation of all interface methods
* brief: (0 or 1(default)): include the brief description of the element
* plaintext: (0 or 1(default)): include the plain text description of the element
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst)
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample)

.. code-block:: rst

    .. kl-type:: Bone
      members=1;
      methods=0;
      createrefs=0;

.. _kl_ext_constantlist_directive:
The kl-ext-constantlist directive
--------------------------------------
The kl-ext-constantlist is used list of all constants within an extension.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* includeprivate: (0(default) or 1): when enabled private interfaces are also shown
* createrefs: (0(default) or 1): when enabled the sphinx reference for each constant is created. this should only happen in the main page for the extension.
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* brief: (0 or 1(default)): include the brief description of the element
* plaintext: (0 or 1(default)): include the plain text description of the element
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst)
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample)

.. code-block:: rst

    .. kl-ext-constantlist:: Alembic
      includeprivate=1;

.. _kl_ext_interfacelist_directive:
The kl-ext-interfacelist directive
-----------------------------------
The kl-ext-interfacelist is used to create a toc tree listing all interfaces within an extension.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* includeprivate: (0(default) or 1): when enabled private interfaces are also shown

.. code-block:: rst

    .. kl-ext-interfacelist:: Geometry
      includeprivate=1;

.. _kl_ext_typelist_directive:
The kl-ext-typelist directive
-----------------------------------------
The kl-ext-typelist is used to create a toc tree listing all types within an extension. (it will only show the ones which have a proper label and reference. in this case we haven't implemented all of them.)

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* includeprivate: (0(default) or 1): when enabled private interfaces are also shown
* compact: (0(default) or 1): compact version of the function list, without any additional documentation (example or such).
* createrefs: (0(default) or 1): when enabled the sphinx reference for each function is created. this should only happen in the main page for the extension.

.. code-block:: rst

    .. kl-ext-typelist:: Math

.. _kl_ext_functionlist_directive:
The kl-ext-functionlist directive
---------------------------------------
The kl-ext-functionlist is used to create a list similar to the kl-methodlist, but for free functions.

* title: (0(default) to 7): define the level of title to generate (0 == off, 1 first level title etc)
* includeprivate: (0(default) or 1): when enabled private interfaces are also shown
* compact: (0(default) or 1): compact version of the function list, without any additional documentation (example or such).
* createrefs: (0(default) or 1): when enabled the sphinx reference for each function is created. this should only happen in the main page for the extension.
* category: (String): the category of functions to list (empty string for all)
* userefs: (0 or 1(default)): enables or disables the auto generation of refs for all known KL types.
* brief: (0 or 1(default)): include the brief description for each function
* plaintext: (0 or 1(default)): include the plain text description for each function
* customrst: (0 or 1(default)): include custom rst (defined by \rst and \endrst) for each function
* example: (0 or 1(default)): include any KL examples (defined by \example and \endexample) for each function

.. code-block:: rst

    .. kl-ext-functionlist:: Math
      compact=1;

    .. kl-ext-functionlist:: FabricTEEM
      compact=0;

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
