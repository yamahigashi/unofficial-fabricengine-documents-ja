Documentation System KL Doxygen Qualifiers
==========================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

The KL AST embedded docs are created following the doxygen notation, headed by /// or /**. Additionally you can use the standard doxygen qualifiers + some special qualifiers.

* \\brief : A brief description
* \\param : A single parameter description
* \\category : The category of this method / function
* \\internal : Marks this function / method / type as internal. Internal elements won't show up in the documentation.
* \\versionadded : Generates a versionadded directive in sphinx
* \\note : Creates a proper note directive in sphinx of the following text
* \\seealso : Creates a proper see-also directive in sphinx for each of the comma-separated values
* \\example and \\endexample : A bracket of two qualifiers containing a KL example. This does not have to include the operator entry code. Also the require * statement for the extension will be added automatically.
* \\rst and \\endrst : A bracket of two qualifiers containing any additional custom rst code.

Example:

.. code-block:: kl

    require Math;

    /// The maximum number of characters for a name. 
    /// The MyStruct type will obey this length for its name.
    /** \example
        String s;
        if(s.length() > MAX_NAME_LENGTH)
          setError("Invalid String Length");
        report(MAX_NAME_LENGTH);
        \endexample
    */
    const Integer MAX_NAME_LENGTH = 256;

    /**
      Converts radian angles to degree angles.
      \param rad The radian value to convert.
      \example
        report(PI);
        report(radToDeg(PI));
      \endexample
    */
    function Scalar radToDeg(Scalar rad) {
      return rad * 180.0 / PI;
    }

    /** An internal struct, it won't show up in the doc
      \internal
    */
    struct MyStructWorkData {
      Integer numbers[];
    };

    /** \brief A custom data structure.
      The MyStruct datastructure can be used to express a named structure. The name member stores the string data of that name.
    */
    struct MyStruct : Vec3
    {
      /// The name of the struct
      String name; 
    };

    /// A constructor taking a preset value for the name.
    /// \param name The initial name of the MyStruct
    function MyStruct(String name)
    {
      /// The new value for the name.
      this.name = name;
    }

    /// A comparison op, useful for checking strings
    function Boolean == (MyStruct a, String b)
    {
      return a.name == b;
    }

    /// An assignment from string
    function MyStruct.=(String other)
    {
      this.name = other;
    }

    /// A concentation op
    function MyStruct + (MyStruct a, MyStruct b)
    {
      return MyStruct(a.name + '.' + b.name);
    }

    /// An interface ensuring the protocol required to get and set a MyStruct
    interface MyInterface
    {
      /** \brief A getter for the MyStruct data
        \category getter
      */
      MyStruct getS();

      /// The MyStruct setter
      /// \category setter
      /// \param s The new value for the MyStruct
      /// \example
      /// MyInterface i = MyObject();
      /// i.setS(MyStruct("test"));
      /// report(i);
      /// \endexample
      setS!(MyStruct s);
    };

    /// An object implementing the MyInterface interface
    object MyObject : MyInterface
    {
      /// The current version of the MyObject
      Integer version;
      /** 
        The (private) MyStruct content.
        \internal
      */
      MyStruct s;
    };

    // The documentation of the method will be inherited from the interface
    function MyStruct MyObject.getS()
    {
      return this.s;
    }

    // The documentation of the method will be inherited from the interface
    function MyObject.setS!(MyStruct s)
    {
      this.s = s;
    }

    /// A specialized object of MyObject, which returns a MyStruct with the "dummy" content
    object MySpecializedObject : MyObject
    {
    };

    /** Overload of the getS method, which always returns "dummy" as the MyStruct's name.
      \category getter
      \rst
      .. note::

            This is just an example of how to overload a method.
      \endrst
    */
    function MyStruct MySpecializedObject.getS()
    {
      return MyStruct("dummy");
    }

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
