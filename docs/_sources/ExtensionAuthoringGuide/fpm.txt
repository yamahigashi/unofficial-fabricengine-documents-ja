.. _EAG.fpm:

The Extension Manifest File
=======================================

Every |FABRIC_PRODUCT_NAME| must include an extension manifest file.  This file must have the filename :file:`{ExtensionName}.fpm.json`; the name of the extension is, by definition, the first part of the manifest file's filename.

As the filename suggests, the extension manifest file is in JSON format; for more information on JSON format, see http://json.org/.  The contents of the file are a JSON object with two members, :code:`libs` and :code:`code`.  The value of each of these members must be either an array of strings or a single string; in the latter case, it is interpreted as an array of strings containing the single given string.  The :code:`libs` member is optional and if omitted it will be treated as if it were an empty list of strings.  The :code:`code` member is required.

The following is an example :file:`{ExtensionName}.fpm.json` extension manifest file:

.. code-block:: json
  
  {
    "version": "1.0.0",
    "libs": ["OneLib", "SecondLib"],
    "code": ["OneSourceFile.kl", "AnotherSourceFile.kl", "ThirdSourceFile.kl"],
    "dfgPresets": {
      "dir": "DFG",
      "presetPath": "MyCompany.Exts.MyExtension"
      }
  }

.. _EXTS_VERSIONING:

The :code:`version` Extension Versioning Specification (optional)
------------------------------------------------------------------

The :code:`version` member specifies the version of the extension using a major, minor and revision number.

For more information on how to load a specific version in KL please refer to :ref:`KLPG.require.versioning`.

.. note:: You can find a unit test shipped with Fabric Engine which demonstrate this in :code:`Test/Core/Python/ext-versions.py`.

The :code:`override` Extension Versioning Override (optional)
------------------------------------------------------------------

The :code:`override` member optionally specifies an override key for this extension which is used to determine which version of a given extension takes priority over others at runtime. For more information please refer to :ref:`KLPG.require.versioning`.

.. note:: You can find a unit test shipped with Fabric Engine which demonstrate this in :code:`Test/Core/Python/ext-versions-override.py`.

The :code:`dfgPresets` Canvas Presets Specification (optional)
-----------------------------------------------------------------

The :code:`dfgPresets` member can be used to specify a directory and namespace for Canvas presets shipped with an extension. The directory needs to specify a folder relative to the folder of the manifest file. The resulting absolute path will be added the Canvas preset search under the given presetPath. The presetPath is used as a namespace within Canvas, so in the example above all presets will show up below :code:`MyCompany.Exts.MyExtension`.

The :code:`libs` Compiled Library Specification
----------------------------------------------------

The :code:`libs` member specifies a list of shared libraries (ie. DLLs) that include compiled code that provides functionality needed by the extension.  When the extension is loaded, these libraries are loaded in the given order.

The |FABRIC_PRODUCT_NAME| core tries multiple filenames when attempting the load the given shared library.  For a given string :samp:`{LibName}` in the array of libraries, the filenames attempted are:

#. The file :file:`{LibName}-Windows-{ARCH}.DLL` (Windows), :file:`lib{LibName}-Linux-{ARCH}.so` (Linux) or :file:`lib{LibName}-Darwin-{ARCH}.dylib` (Mac OS X); :samp:`{ARCH}` is the system architecture, either ``x86`` or ``x86_64``.

#. The file :file:`{LibName}.DLL` (Windows), :file:`lib{LibName}.so` (Linux) or :file:`lib{LibName}.dylib` (Mac OS X)

#. The file :file:`{LibName}` without any prefix or suffix.

In each case, the |FABRIC_PRODUCT_NAME| core attempts to load the shared library from the directory that contains the :file:`{ExtensionName}.fpm.json` extension manifest file.

The :code:`code` KL Source Code Specification
----------------------------------------------------

The :code:`code` member specifies a list of KL source code files that should be provided by the extension.  These provide the source code included when the KL statement :samp:`require {ExtensionName};` is used in other KL source files.

The KL source files are loaded from the directory containing the :file:`{ExtensionName}.fpm.json` extension manifest file.  The are loaded and compiled in the order given in the :code:`code` array; therefore, it is important that if the contents of one source file depends on the contents of another, the former should follow the latter.  For example, if one source file defines a type and a second uses the type in another type or function declaration, the second file should follow the first.
