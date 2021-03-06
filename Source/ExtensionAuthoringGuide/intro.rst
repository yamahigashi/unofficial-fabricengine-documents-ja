Introduction
=======================================

What is a |FABRIC_PRODUCT_NAME| Extension?
------------------------------------------------

An :dfn:`extension` is a set of files that add functionality to |FABRIC_PRODUCT_NAME|.  Extensions are often used to expose the functionality of third-party libraries to |FABRIC_PRODUCT_NAME| applications, but can also be used to provide a library of custom code written in C++ and/or KL.

Types of Extensions
---------------------------------------

There are two primary types of extensions that we will refer to in this guide:

Native code extension
  A native code extension contains compiled native code that is made available to KL operators.  It necessarily also contains KL code that is used to provide the names of types, methods and functions that made available.  Native code extensions are written in C++ and use a header file automatically generated by the :command:`kl2edk` utility.

KL-only extension
  A KL-only extension only contains KL types, methods and functions; no native code is provided.  Packaging up functionality as a KL-only extension is an elegant way of providing a library of KL types and functions.

There is no fundamental difference between native code extensions and KL-only extensions, and in fact a given extension can be an arbitrary mixture of KL and native code.

Limitations
---------------------------------------

The extension mechanism of |FABRIC_PRODUCT_NAME| is a very powerful way of providing external functionality to the KL language.  However, there are several limitations that you must be aware of when working with extensions.

If functionality is provided through native code then all of the usual limitations of native code also apply to the extension.  These include:

- The KL mechanisms that protect the programming from errors, such as guarded array access, are not available in native code; it is entirely the responsibility of the extension author to ensure that the native code is correct.  In particular, the extension author needs to carefully ensure that memory is managed correctly, including the allocation and freeing of objects.

- Native code cannot be optimized into KL code; as such, providing a native code function that does very little will often incur an overhead just for calling the function.  It is usually a good idea to write such functions in KL instead of native code to ensure that the KL optimizer is able to optimize the code as much as possible.

- Native code cannot be executed on the GPU; a call to native code in an extension will automatically made code that would otherwise execute on the GPU fall back on CPU execution.  This may result in severe performance degradation in the case that the KL code would otherwise run on the GPU.

