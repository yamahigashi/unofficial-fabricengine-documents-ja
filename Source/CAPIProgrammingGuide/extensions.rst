

.. c:function::
  void FEC_RegisterKLExtension( FEC_ClientRef clientRef, char const *nameCString, char const *versionCString, uint32_t numSourceFiles, FEC_KLSourceFile const *sourceFiles, int reload )

  Create a new extension that consists of KL code in the form of one or more KL source files.
  The source file contents are provided along with their filenames (used for diagnostics).

  This function will set an exception is there was some failure
  creating the extension.

  :param FEC_ClientRef clientRef: The client
  :param char const *nameCString: The name of the new extension
  :param char const *versionCString: The version of the new extension
  :param char const *overrideCString: The override for the version of the new extension
  :param uint32_t numSourceFiles: The number of KL source files provided
  :param FEC_KLSourceFile *sourceFiles: The filename and source code for each source file
  :param int load: Load the extension once it is registered.
  :param int reload: If the extension already exists setting this to true will update its source code.


