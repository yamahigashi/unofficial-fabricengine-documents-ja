.. _LG:

Licensing Guide
=========================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

Overview
========

Fabric uses the Reprise License Manager (RLM) to manage its licensing. |FABRIC_PRODUCT_NAME| verifies on startup if there is a valid license and notifies the user of its status.

How it works
------------

When a Fabric application starts it will check for a valid license. If a license it not found it will display a window allowing individuals to input their RLM node-locked Evaluation license. If the user does not have a valid license then Fabric will continue to run but will force a hard 15-second pause in the application every 15 minutes and will display the licensing window again.

Studios making use of the Fabric Fifty program as well as Commercial and Educational customers will receive an RLM floating license. Floating licenses allow an organization to run an RLM server in a central location and have their users validate licensing against this server rather than requiring each user to have their own license. With floating licenses the server holds a fixed number of licenses and will allow up to that many users to run the software at any given time. The number of actual users may be higher, floating licenses only allow for a fixed number of licenses to be "checked out" at any given time. Once a user finishes using the software the license is "checked in" again and can be used by someone else. More information on managing floating licenses can be found in :ref:`LG.floating`.

Using floating licenses requires that all users have access to the RLM server in order to validate licensing, whether this be via a local network or over a VPN from home.

Plugin licensing
-----------------

Fabric plugins such as Fabric for Maya only check out a license once they start performing computations. This means that a plugin that is "idle", i.e. the plugin is loaded but not being used, will not use a license. Once a license is checked out though it will remain in use until the Fabric plugin is unloaded.

Types of licenses
-----------------

For more information on the types of licenses available please refer to the LICENSE.txt file found in the root Fabric folder after unpacking the installation .zip file.

License file paths
-------------------

Normally a user running with a node-locked Evaluation license should not need to worry about where the Fabric license is stored as the licensing windows should allow updating it as necessary, however for users who may need access to the license file for any reason it can be found here on Linux and OSX:

.. code-block:: bash

  $HOME/.fabric-engine/rlm/

And here on Windows:

.. code-block:: bash

  %APPDATA%\Fabric Engine\rlm\

.. _LG.floating:

Floating licenses with an RLM server
=====================================================

Preparing the RLM server
--------------------------------------------

In order to use an RLM server if you do not already have one you will need to download the RLM server package appropriate to your system from:

  http://dist.fabricengine.com/rlm/

This server package contains three files, the :command:`rlm` and :command:`rlmutil` binaries, as well as the :file:`fabricinc.set` file that enables licensing of |FABRIC_PRODUCT_NAME| via the RLM server.

If you already have an RLM server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you already have an RLM server running on your network then you will only need to add the :file:`fabricinc.set` file to your RLM server directory and then add the .lic license file after you get one (described below).

Installing a new RLM server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you do not already have an RLM license server running you can install one using the :command:`rlm` binary in the package supplied above. Copy the files in the package into a folder on the license server system where you would like to keep them. Once you have your .lic license file as described below copied into this same folder, simply running the :command:`rlm` binary will launch the RLM server. If you have not modified any settings the server will by default run on port 5053.

In Windows you may get a notification asking to open a port in the firewall. This is required for the RLM server to be accessible by other machines on the network.

If you have trouble installing the RLM server please see :ref:`help`. 

Getting your floating license
--------------------------------------------

In order to request your Fabric Fifty licenses you will need to supply the "Host ID" of your license server in order for the Fabric Engine team to create your license. You can get your system's "Host ID" using the :command:`rlmutil` binary supplied in the server package above. From the folder where you extracted the package binaries, open a command prompt and run:

.. parsed-literal::
  
  ./rlmutil *rlmhostid*

This should give a result that resembles this:

.. code-block:: none
  
  user@host~/fabric-rlm$ ./rlmutil rlmhostid
  rlmutil v9.4
  Copyright (C) 2006-2012, Reprise Software, Inc. All rights reserved.
  
  Hostid of this machine: e0e0e0e0e0e0 a0a0a0a0a0a0

Depending on your machine configuration there may be one or multiple "Host ID" values displayed. These can all be copied and entered as the "Host ID" value in the |FABRIC_PRODUCT_NAME| licensing request form here along with the other required data:

  http://fabricengine.com/request-fabric-fifty/

You will receive a license from the Fabric Engine team once your request has been processed which can be copied into a file with a .lic extension (fabric.lic, for example). This file needs to be copied into the folder where your RLM server is installed. Once the server is restarted you should have a valid RLM server running that is ready to validate |FABRIC_PRODUCT_NAME| licenses.

Using the RLM server for licensing
--------------------------------------------

Once your RLM server is running you'll need to point your clients of |FABRIC_PRODUCT_NAME| to this server.

You can use the general RLM environment variable:

.. code-block:: none

  RLM_LICENSE=port@host

Or the Fabric-specific RLM variable:

.. code-block:: none

  fabricinc_LICENSE=port@host

RLM also supports to define the server in a license file. This license file is stored in the same place as a nodelocked license, can take any name (with the .lic extension) and tells the license system to look into an specific server. 
The following is an example of this file. 

.. code-block:: none
  
  HOST 192.168.1.221 any 5053

If the licensing server is running and you have entered its host and port correctly then your copy of |FABRIC_PRODUCT_NAME| should now be licensed.

Running Fabric 2 licenses alongside 1.x
--------------------------------------------

Some user sites may wish to run licenses for both Fabric 2 and previous Fabric 1.x simultaneously. Doing this only requires ensuring that the .lic files have different names and that both are available in the RLM server folder.

Custom server configuration
--------------------------------------------

RLM allows end-user configuration of some licensing parameters via the :dfn:`ISV Options File`. The options file should be named :file:`fabricinc.opt` and placed in the same directory as the :file:`fabricinc.set` file. Full documentation on available options can be seen here:

  http://www.reprisesoftware.com/RLM_Enduser.html

Reserving licenses by group
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some users may wish to permanently allocate a number of server licenses to a particular group while leaving the remaining floating licenses available to anyone. This can be achieved using the GROUP, HOST_GROUP, and RESERVE options in the options file.

A group must first be created in the options file to specify the usernames or hostnames that belong to it. A list of usernames is created using the GROUP option, while a list of hostnames is created using HOST_GROUP.

.. code-block:: none
  
  GROUP <groupname> [ <user> <user> ... ]
  HOST_GROUP <groupname> [ <host> <host> ... ]

For example:

.. code-block:: none
  
  GROUP developers steve joe david
  HOST_GROUP devhosts myhost joesbox davepc


Once the group has been created, licenses can be allocated to that group by creating a RESERVE line in the options file.

.. code-block:: none
  
  RESERVE <number> fabric [ GROUP | HOST_GROUP ] <groupname>


For example:

.. code-block:: none
  
  RESERVE 5 fabric GROUP developers
  RESERVE 10 fabric HOST_GROUP devhosts

Once the RLM server is restarted, the specified number of licenses will be available only to that group while remaining licenses will be free to anyone.
.. _help:

Getting Help
============

For further information regarding RLM licensing you can consult the RLM End-User Manual available here:

  http://www.reprisesoftware.com/RLM_Enduser.html

For additional inquiries regarding licensing and |FABRIC_PRODUCT_NAME| please contact ``support@fabricengine.com``.
