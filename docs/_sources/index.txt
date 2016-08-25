.. _TOP:

|FABRIC_PRODUCT_NAME| Unofficial Documentation 日本語版
=======================================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_COPYRIGHT|


日本語版翻訳について
---------------------
このドキュメントは `Fabric Engine Documentation 
<http://docs.fabric-engine.com/FabricEngine/latest/HTML/index.html>`_ の和訳です。
この日本語に翻訳された文書は Fabric Software社公式のものではありません。
和訳に関する質問、問い合わせは Fabric Softwawe ではなく
`この和訳プロジェクト
<https://github.com/yamahigashi/unofficial-fabricengine-documents-ja/>`_ の
`issues
<https://github.com/yamahigashi/unofficial-fabricengine-documents-ja/issues>`_ 迄お願いします。
この文書の和訳は完璧な翻訳ではなく、誤りを含む可能性があります。あくまで概略を示すものとしてお使いください。また当該翻訳の正確性の欠如、および翻訳結果から生じるいかなる損害に対しても翻訳者は一切の責任を負わないものとします。またこの文書のすべての権利は Fabric Software社にあります。

また各ページの翻訳前のオリジナルページへは、サイドバーこのページセクション『原文公式ページへ移動』のリンクからたどることができます。


Welcome!
---------------------

This is the documentation for |FABRIC_PRODUCT_NAME| |FABRIC_VERSION|, last updated |today|.

The documentation can also be downloaded as a zip from here: |DOCS_ZIP|

:strong:`Parts of the documentation:`

.. rst-class:: indexblocka

|    |RELNOTES-FABRIC_VERSION|
|        What's new in |FABRIC_PRODUCT_NAME| |FABRIC_VERSION|

.. rst-class:: indexblockb

|    :strong:`Completely fresh to the product? Looking for installation help?`
|
|        :ref:`GETTINGSTARTED_INDEX`
|            For help installing, licensing and starting to use |FABRIC_PRODUCT_NAME| please consult this guide.
|

.. rst-class:: indexblocka

|    :strong:`Looking for information about Canvas, the visual programming system?`
|
|        :ref:`CANVASUSERGUIDE`
|            A user's guide to the Canvas visual programming system.
|
|        :ref:`CANVASPROGRAMMERGUIDE`
|            A guide for Canvas for Programmers.

.. rst-class:: indexblockb

|    :strong:`Looking for information about the Fabric DCC integrations?`
|
|        :ref:`MAYA`
|            The Fabric for Maya integration
|
|        :ref:`MODO`
|            The Fabric for MODO integration
|
|        :ref:`SOFTIMAGE`
|            The Fabric for Softimage integration

.. rst-class:: indexblocka

|    :strong:`New to KL? An existing KL user? Here are the KL programming guides:`
|
|        :ref:`KLPG`
|            An introduction for the KL programming language
|
|        :ref:`KLSTYLEGUIDE`
|            How to write well styled KL
|
|        :ref:`KLEXTENSIONSGUIDE`
|            An overview of all available KL extensions
|
|        :ref:`KLTOOLGUIDE`
|            How to use the KL Tool to develop and debug KL extensions
|
|        :ref:`MRPG`
|            An overview now to use Map Reduce in KL

.. rst-class:: indexblockb

|    :strong:`Searching for low level information, such as the Core or GPU Compute?`
|
|        :ref:`CO`
|            An overview of the inner workings of the Fabric Core
|
|        :ref:`DG`
|            Information about how to debug KL
|
|        :ref:`INSTG`
|            A guide introducing the instrumentation functionality for KL
|
|        :ref:`GPUCompute`
|            An introduction into GPU compute - how to use KL on the GPU

.. rst-class:: indexblocka

|    :strong:`Are you a programmer and interested in the various APIs?`
|
|        :ref:`CAPIPG`
|            The C/C++ Fabric Core programming guide
|
|        :ref:`CAPIPG.canvas`
|            The C/C++ Fabric Canvas programming guide
|
|        :ref:`RTVPG`
|            The C/C++ API for accessing KL data types explained
|
|        :ref:`PYTHONPG`
|            The Python Fabric Core and FabricUI programming guide
|
|        :ref:`EXTRG`
|            An introduction to writing your own KL extensions
|
|        :ref:`DOCSYSTEM`
|            The Fabric documentation system based on sphinx

Table of contents
---------------------------------

.. toctree::
  :maxdepth: 1

  GettingStartedGuide/index
  CanvasUserGuide/index
  CanvasProgrammerGuide/index
  KLProgrammingGuide/index
  KLStyleGuide/index
  KLExtensionsGuide/index
  KLToolGuide/index
  MapReduceProgrammingGuide/index
  CoreOverview/index
  DebuggingGuide/index
  InstrumentationGuide/index
  GPUCompute/index
  CAPIProgrammingGuide/index
  RTValProgrammingGuide/index
  PythonGuide/index
  ExtensionAuthoringGuide/index
  Installation/index
  LicensingGuide/index
  DocSystem/index
  DCCIntegrations/index
  DCCIntegrations/thirdpartylicenses
