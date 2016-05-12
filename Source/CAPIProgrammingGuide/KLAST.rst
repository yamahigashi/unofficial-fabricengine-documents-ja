

.. c:function:: void FEC_GetKLJSONAST( FEC_ClientRef clientRef, char const *sourceCode )

  Get a JSON representation of the AST (Abstract Syntax Tree) for the given KL code.

  :param FEC_ClientRef clientRef: The client
  :param char const *fileName: The file name of the KL code
  :param char const *sourceCode: The KL code for which to return the AST
  :param int includeRequires: Also include the full AST for required extensions


