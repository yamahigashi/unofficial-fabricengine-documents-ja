.. _json_extension:

JSON Extension
====================================================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

.. versionadded:: 1.13.0

The :ref:`json_extension` implements a basic json encoder and parser in KL. 

Parsing JSON Text
-----------------

The following code show passing a json string to the :kl-ref:`JSONDoc` for parsing, and then extracting the relevant data.

.. kl-example::

  require JSON;

  operator entry() {

    String json = "    {\n\
      \"firstName\": \"John\",
      \"lastName\": \"Smith\",
      \"isAlive\": true,
      \"age\": 25,
      \"height_cm\": 167.64,
      \"address\": {
          \"streetAddress\": \"21 2nd Street\",
          \"city\": \"New York\",
          \"state\": \"NY\",
          \"postalCode\": \"10021-3100\"
      },
      \"phoneNumbers\": [
          { \"type\": \"home\", \"number\": \"212 555-1234\" },
          { \"type\": \"fax\",  \"number\": \"646 555-4567\" }
      ]
    }";

    JSONDoc doc();
    doc.parse(json);
    
    {
      // Now read the data back. 
      report("firstName:" + doc.root.getString("firstName"));
      report("lastName:" + doc.root.getString("lastName"));
      report("isAlive:" + doc.root.getBoolean("isAlive"));
      
      // Test casting
      report("f_age:" + doc.root.getScalar("age"));
      report("i_age:" + doc.root.getInteger("age"));

      report("f_height_cm:" + doc.root.getScalar("height_cm"));
      report("i_height_cm:" + doc.root.getInteger("height_cm"));

      JSONDictValue address = doc.root.get("address");

      JSONArrayValue phoneNumbers = doc.root.get("phoneNumbers");
      JSONDictValue num1 = phoneNumbers.get(0);
      report("number:" + num1.getString("number"));
    }
  }

Robustness
----------

The :kl-ref:`JSONDoc` parser is built to be as robust as possible, and handle parsing slightly malformed JSON strings. Dictionaries and arrays will be parsed successfully event when trailing commas are left at the end of the dictionary or array definition. 

.. kl-example::

  require JSON;

  operator entry() {

    String json = "    {\n\
      \"address\": {
          \"streetAddress\": \"21 2nd Street\",
          \"city\": \"New York\",
          \"state\": \"NY\",
          \"postalCode\": \"10021-3100\",
      },
      \"phoneNumbers\": [
          { \"type\": \"home\", \"number\": \"212 555-1234\" },
          { \"type\": \"fax\",  \"number\": \"646 555-4567\" },
      ]
    }";

    JSONDoc doc();
    doc.parse(json);

    {
      // Now read the data back. 
      JSONDictValue address = doc.root.get("address");
      report("streetAddress:" + address.getString("streetAddress"));

      JSONArrayValue phoneNumbers = doc.root.get("phoneNumbers");
      JSONDictValue num1 = phoneNumbers.get(0);
      report("number:" + num1.getString("number"));
    }

  }

Math Structs
------------

A :kl-ref:`JSONDoc` parser handles loading and saving of some of the commonly used Math types defined in the :ref:`math_extension`.

.. kl-example::

  require JSON;

  operator entry() {

    String json = " \n\n   {\n
      \"vec3\" \n
      : { 'x': 12.3, 'y': 12, 'z': 0 },\n
      \"vec2Array\"  : [ \n
          { 'x': 12.3,'y': 12 }, \n
          {  \n
          'x': 3, \n
          'y':1.2  \n
         } \n
      ], \n
      \"color\": { 'r': 12.3, 'g': 12, 'b': 0, 'a': 0 },\n
    }";

    JSONDoc doc();
    doc.parse(json);
    
    {
      // Now read the data back. 
      report("vec3:" + doc.root.getVec3("vec3"));

      JSONArrayValue vec2Array = doc.root.get("vec2Array");
      report("vec2_1:" + vec2Array.getVec2(0));
      report("vec2_2:" + vec2Array.getVec2(1));

      JSONDictValue dict = doc.root.get("color");
      report("color:" + dict.toColor());
    }

  }

Writing
-------

The :kl-ref:`JSONDoc` can be also used to encode JSON.

.. kl-example::

    require JSON;

    operator entry() {

      JSONDoc doc();    
      doc.root.setString("firstName", "John");
      doc.root.setString("lastName", "Smith");
      doc.root.setBoolean("isAlive", true);
      doc.root.setInteger("age", 25);
      doc.root.setScalar("height_cm", 167.64);

      JSONDictValue address();
      address.setString("streetAddress", "21 2nd Street");
      address.setString("city", "New York");
      address.setString("state", "NY");
      address.setString("postalCode", "10021-3100");
      doc.root.set("address", address);

      JSONDictValue num1();
      num1.setString("type", "home");
      num1.setString("number", "212 555-1234");
      JSONDictValue num2();
      num2.setString("type", "home");
      num2.setString("number", "212 555-1234");

      JSONArrayValue phoneNumbers();
      phoneNumbers.add(num1);
      phoneNumbers.add(num2);
      doc.root.set("phoneNumbers", phoneNumbers);

      JSONArrayValue vec2Array();
      vec2Array.add(JSONDictValue(Vec2( 12.3, 12 )));
      vec2Array.add(JSONDictValue(Vec2( 3, 1.2 )));
      doc.root.set("vec2Array", vec2Array);

      JSONArrayValue numbers1();
      numbers1.addInteger(1);
      numbers1.addInteger(2);
      numbers1.addInteger(3);
      numbers1.addInteger(4);
      numbers1.addInteger(5);
      numbers1.addInteger(6);
      doc.root.set("numbers1", numbers1);

      JSONArrayValue numbersAndVec();
      numbersAndVec.addInteger(1);
      numbersAndVec.addInteger(2);
      numbersAndVec.add(JSONDictValue(Vec2( 12.3, 12 )));
      doc.root.set("numbersAndVec", numbersAndVec);

      JSONArrayValue numbersAndSimpleString();
      numbersAndSimpleString.addInteger(1);
      numbersAndSimpleString.addInteger(2);
      numbersAndSimpleString.addInteger(3);
      numbersAndSimpleString.addInteger(4);
      numbersAndSimpleString.addInteger(5);
      numbersAndSimpleString.addInteger(6);
      numbersAndSimpleString.addInteger(7);
      numbersAndSimpleString.addInteger(8);
      numbersAndSimpleString.addString("Foo");
      doc.root.set("numbersAndSimpleString", numbersAndSimpleString);

      JSONArrayValue numbersAndBigString();
      numbersAndBigString.addInteger(1);
      numbersAndBigString.addInteger(2);
      numbersAndBigString.addString(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor " +
        "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud " +
        "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute " +
        "irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla " +
        "pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia " +
        "deserunt mollit anim id est laborum.");
      doc.root.set("numbersAndBigString", numbersAndBigString);

      String json = doc.write(2);
      report(json);
    }

Merging
-------

A :kl-ref:`JSONDoc` can be merged with other JSON docs to create a new Doc with the tree of data merged. 

.. kl-example::

  require JSON;

  operator entry() {

    String json1 = "{
      'firstName': 'John',
      'lastName': 'Smith',
      'isAlive': true,
      'age': 25,
      'height_cm': 167.64,
      'address': {
          'streetAddress': '54 Queen Street'
      },
      'phoneNumbers': [
          { 'type': 'cell',  'number': '514 561-6312' }
      ]
    }";

    JSONDoc doc1();
    doc1.parse(json1);

    String json2 = "{
      'firstName': 'Fred',
      'height_cm': 187.64,
      'address': {
          'streetAddress': '21 2nd Street',
          'city': 'New York',
          'state': 'NY',
          'postalCode': '10021-3100'
      },
      'phoneNumbers': [
          { 'type': 'home', 'number': '212 555-1234' },
          { 'type': 'fax',  'number': '646 555-4567' }
      ]
    }";
    

    JSONDoc doc2();
    doc2.parse(json2);

    doc1.merge(doc2);


    {
      // Now read the data back. 
      report("firstName:" + doc1.root.getString("firstName"));
      report("lastName:" + doc1.root.getString("lastName"));
      report("isAlive:" + doc1.root.getBoolean("isAlive"));
      
      // Test casting
      report("f_age:" + doc1.root.getScalar("age"));
      report("i_age:" + doc1.root.getInteger("age"));

      report("f_height_cm:" + doc1.root.getScalar("height_cm"));
      report("i_height_cm:" + doc1.root.getInteger("height_cm"));

      JSONDictValue address = doc1.root.get("address");

      JSONArrayValue phoneNumbers = doc1.root.get("phoneNumbers");
      JSONDictValue num1 = phoneNumbers.get(0);
      report("number type:" + num1.getString("type") + " number:" + num1.getString("number"));
      JSONDictValue num3 = phoneNumbers.get(2);
      report("number type:" + num3.getString("type") + " number:" + num3.getString("number"));
    }
  }

Table of Contents
-----------------

.. toctree::
  :maxdepth: 2
  
  files
  interfaces
  types

Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
