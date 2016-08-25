.. _GETTINGSTARTED_BASEINSTALLATION:

Installing the |FABRIC_PRODUCT_NAME| license
============================================================

Once you run Fabric via the standalone or a DCC integration without a license, you will get a Fabric Licensing dialog:

.. image:: /images/GettingStarted/licensing1.png

If you are an individual and want a node-locked license, please go to www.fabricengine.com for more information. For other type of licenses please contact sales@fabricengine.com
In any case, you will need a MAC address of the machine. You can easily find and copy it within the Fabric Licensing dialog.

If you already have your node-locked license, you can click in the "Enter Node-Locked License" button.

.. image:: /images/GettingStarted/licensing2.png

In this dialog you can paste the license text that you got. Clicking Ok will install the license in the correct directory. On windows the license will be located in %AppData%/Fabric Engine/rlm whereas on Linux and OS X it will be in ~/.fabric-engine/rlm
You can also bypass the "Enter Node-Locked License" dialog and just copy the .lic file in the aforementioned directories. Restarting Fabric will read the license file.

Fabric can also run unlicensed. If you decide to continue unlicensed, Fabric will pause for 15 seconds every 15 minutes, resuming automatically after each pause. 

.. image:: /images/GettingStarted/licensing3.png

.. note:: If you are looking for a more technical explanation on licenses, please check the :ref:`Licensing Guide <_LG>` for more information.