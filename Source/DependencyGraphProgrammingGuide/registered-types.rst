.. _DGPG.registered-types:

Registered Types
================

|FABRIC_PRODUCT_NAME| supports a :dfn:`registered types` system whereby user-defined compound types (ie. structures) are defined through JavaScript.  Once a type has been registered, it can be used to define members of Nodes and EventHandlers (see below) as well as used in KL code.

Registering a New Type
----------------------

To register a new type, call the ``fabricClient.RT.registerType`` function with the name of the type as the first parameter and the :dfn:`specification` object as the second parameter.  The specification object has the following members:

``members``
  
  An object containing the members to be contained in the type.  The key names are the member names for the type and the key values are the names of already-registered types or built-in KL types (see the :ref:`KLPG` for more information on atomic types).
  
  .. note:: It is possible to append brackets to obtain variable- or fixed-length arrays as members, eg. ``Scalar[2][2]``, ``Scalar[][]`` and ``Scalar[2][][4]``.

``constructor``
  
  A JavaScript or Python constructor that is used to provide the JavaScript or Python "prototype" for objects values returned from the |FABRIC_PRODUCT_NAME| core, as well as to provide a default value if none is given.

``defaultValue``
  
  (optional) The default value for the type.

klBindings
  
  (optional) KL code to include which provides operations involving the type, such as :ref:`constructors <KLPG.constructor>`, methods and operators

To get an object containing information about all the currently-registered types, call ``fabricClient.RT.getRegisteredTypes()``.

Example of Type Registration
----------------------------

The following code registers a new |FABRIC_PRODUCT_NAME| type ``Vec3`` and associates it with a Python type of the same name:

.. code-block:: none
  
  >>> # Registered types
  class Vec3():
    def __init__( self, x = None, y = None, z = None ):
      if type( x ) is float and type( y ) is float and type( z ) is float:
        self.x = x
        self.y = y
        self.z = z
      elif x is None and y is None and z is None:
        self.x = 0
        self.y = 0
        self.z = 0
      else:
        raise Exception( 'Vec3: invalid arguments' )
  
  >>> vec3KLBindings = """
  // Construct a Vec3 from three Scalars
  function Vec3(Scalar x, Scalar y, Scalar z) {
    this.x = x;
    this.y = y;
    this.z = z;
  }
  // Add two Vec3s
  function Vec3 + (Vec3 a, Vec3 b) {
    return Vec3(a.x + b.x, a.y + b.y, a.z + b.z);
  }
  """
  
  >>> vec3TypeDesc = {
    'members': [{'x': 'Scalar'}, {'y': 'Scalar'}, {'z': 'Scalar'}],
    'constructor': Vec3,
    'klBindings': {
      'filename': "(inline)",
      'sourceCode': vec3KLBindings
     }
  }
  
  >>> fabricClient.RT.registerType('Vec3', vec3TypeDesc)
  
  >>> fabricClient.RT.getRegisteredTypes()['Vec3']
  {u'defaultValue': <__main__.Vec3 instance at 0x7f73df6955f0>, u'internalType': u'struct', u'name': u'Vec3', u'members': [{u'type': u'Scalar', u'name': u'x'}, {u'type': u'Scalar', u'name': u'y'}, {u'type': u'Scalar', u'name': u'z'}], u'size': 12}
  >>> 
