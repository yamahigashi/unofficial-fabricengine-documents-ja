Introduction
============

|FABRIC_PRODUCT_NAME| provides functionality to aid in debugging applications written using |FABRIC_PRODUCT_NAME| and KL. The Fabric Engine debugger (called zBug and pronounced zee-bug) is based on `LLDB <http://lldb.llvm.org/>`_ and as such aims to provide all of the functionality found in exiting debugging software such as the Visual Studio debugger or gdb while adding support for debugging KL code. With zBug a user should be able to debug the full spectrum of code involved in a KL application, including debugging C/C++ extensions. Because of the support provided by LLDB zBug can also be used to debug pure C or C++ applications or extensions using the same UI.

How Debugging Works
-------------------

In broad strokes debugging a KL application is no different than debugging a compiled C or C++ application. In both cases the compiled code will have some information included in it to pass information to the debugger about file names, line numbers, variable names, types, and other information. The most common open format for this debug info is Dwarf, this is the format used by most open compilers (with Microsoft's Visual Studio compiler being the big exception) and this is the debug info format used by KL as well.

When getting ready to debug a typical C++ application, a developer will usually tell the compiler to include this debug info in the resulting output. Debug info isn't included by default in all compiled code because it takes additional time to produce and requires additional memory when running the application.

A developer will also normally tell the compiler to avoid running optimization passes on the resulting code. Optimizing compiled code can result in much faster execution times, however as the optimizer may change the code significantly in order to achieve this it can make it harder to debug as line numbers may change and variables that the developer wrote into the code may be optimized away and replaced.

Both of these ideas also hold true when debugging KL code. While a developer can independently choose whether or not to run optimization on their KL code and also whether or not to include debug info, in the general case for debugging you will want to include debug info and disable optimizations. Once your code has been written, debugged, and determined to work correctly though you will usually want to disable debug info output to save on memory and enable optimizations to allow the KL compiler to change your code as necessary in order to make it as fast as possible.

