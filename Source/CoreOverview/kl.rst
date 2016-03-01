The KL Language
=======================

KL is the custom language used to define operators in |FABRIC_PRODUCT_NAME|. KL combines the benefits of high performance languages like C++ with the benefits of dynamic languages like JavaScript and Python. ÅeKLÅf stands for ÅeKernel LanguageÅf and refers to the scope of the language: writing operators. Kernels are small stateless blocks of code with an entry function. The syntax of KL is similar to the syntax of JavaScript and C.

Ease of Use
---------------------

KL is a language intended to be used by developers of all levels, particularly those comfortable with dynamic languages. Developers familiar with dynamic languages like Python and JavaScript can quickly learn the rules of KL. Developers familiar with static languages will find KL easy to pick up.

Dynamic Compilation
---------------------

|FABRIC_PRODUCT_NAME| integrates the LLVM compiler and uses it to compile the KL source code used in operators. The KL source code is compiled by |FABRIC_PRODUCT_NAME| as the dynamic language constructs each operator. There are no custom IDE tools required to work with |FABRIC_PRODUCT_NAME|, so developers can continue to use their normal editors. Applications can use dynamic compilation to create applications that have self-modifying behavior.

Cross Platform
---------------------

|FABRIC_PRODUCT_NAME| applications are completely dynamic and portable across operating systems, CPU architectures and devices. This is because |FABRIC_PRODUCT_NAME| dynamically compiles KL source code on target, which ensures that there is no compromise on performance. |FABRIC_PRODUCT_NAME| currently supports all major operating systems on x86 architectures, and support for a wider range of CPU architectures is in development.

Performance
---------------------

KL is a strongly typed language like C, and therefore can be optimized in the same way during compilation. The resulting native machine code executes as fast as C/C++ and is integrated into the application dynamically. A benefit of dynamic compilation is that the compilation process generates optimal machine code for the target CPU architecture.

Security
---------------------

|FABRIC_PRODUCT_NAME| can be run in a range of client and server environments. The KL language is constrained in such a way that it makes it impossible for malicious applications to hijack a running application using |FABRIC_PRODUCT_NAME|. This makes it safe to run |FABRIC_PRODUCT_NAME| in either client-side applications or in online web services. 

Documentation
---------------------

Complete documentation for the KL language is provided in the :ref:`KLPG`.

