Documentation System Hello World
======================================

.. image:: /images/FE_logo_345_60.*
   :width: 345px
   :height: 60px

| |FABRIC_PRODUCT_NAME| version |FABRIC_VERSION|
| |FABRIC_COPYRIGHT|

For this example we'll create an extension which we want to document. We'll call it HelloWorld. Let's put the extension in a folder called HelloWorld as well, add these two files:

HelloWorld.fpm.json :

.. code-block:: json

    {
      "version": "1.0.0",
      "code": [
        "HelloWorld.kl"
      ]
    }

HelloWorld.kl :

.. code-block:: kl

    /// A function to print out HelloWorld
    /// \example
    ///   // prints out hello world
    ///   printHelloWorld();
    /// \endexample
    function printHelloWorld() {
      report('Hello World!');
    }

Of course we'll need a :dfn:`conf.py` file for sphinx, you may use this as a reference (please see the sphinx docs for more details):

.. code-block:: python

    import os
    import FabricEngine.Sphinx.KL

    # Add any Sphinx extension module names here, as strings. They can be extensions
    # coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
    extensions = [
      'sphinx.ext.autodoc',
      'sphinx.ext.graphviz',
      'FabricEngine.Sphinx.KL',
      'FabricEngine.Sphinx.DFG'
    ]

    # Find exectuable in PATH
    def which(program):
        def is_exe(fpath):
            return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

        fpath, fname = os.path.split(program)
        if fpath:
            if is_exe(program):
                return program
        else:
            for path in os.environ["PATH"].split(os.pathsep):
                path = path.strip('"')
                exe_file = os.path.join(path, program)
                if is_exe(exe_file):
                    return exe_file

        return None

    # location of the graphviz dot file
    buildOS = os.environ['FABRIC_BUILD_OS']
    if buildOS == 'Windows':
      graphviz_dot = which("dot.exe")
    else:
      graphviz_dot = which("dot")

    if not graphviz_dot:
      raise Exception("Missing 'dot' executable. Check that GraphViz is installed and that dot.exe cam be found. Define an environment variable GRAPHVIZ_DOT_BIN which points to dot.exe")
    graphviz_output_format = 'svg'

    # The suffix of source filenames.
    source_suffix = '.rst'

    # The master toctree document.
    master_doc = 'index'

    # General information about the project.
    project = u'My project'
    copyright = u'My company copyright'

    # The short X.Y version.
    version = '1.0.0'
    # The full version, including alpha/beta/rc tags.
    release = '1.0.0'

    # The name of the Pygments (syntax highlighting) style to use.
    pygments_style = 'sphinx'

    # The theme to use for HTML and HTML Help pages.  See the documentation for
    # a list of builtin themes.
    html_theme = 'default'

    # Theme options are theme-specific and customize the look and feel of a theme
    # further.  For a list of options available for each theme, see the
    # documentation.
    fabric_color_sky_blue = "#21a8e0"
    fabric_color_greenish = "#73992b"
    fabric_color_aubergine = "#2e1a2e"
    fabric_color_33pct_gray = "#a8a8a8"
    fabric_color_15pct_gray = "#dadada"
    fabric_color_black = "#000000"
    html_theme_options = {
      "headbgcolor": fabric_color_15pct_gray,
      "headtextcolor": fabric_color_aubergine,
      "sidebarbgcolor": fabric_color_aubergine,
      "sidebartextcolor": fabric_color_33pct_gray,
      "sidebarlinkcolor": fabric_color_15pct_gray,
      "relbarbgcolor": fabric_color_greenish,
      "relbartextcolor": fabric_color_15pct_gray,
      "relbarlinkcolor": fabric_color_aubergine,
      "footerbgcolor": fabric_color_black,
      "footertextcolor": fabric_color_33pct_gray,
    }

    # The name for this set of Sphinx documents.  If None, it defaults to
    # "<project> v<release> documentation".
    html_title = "My project Documentation"

Also we'll need an :dfn:`index.rst` file for our documentation:

.. code-block:: rst

    .. _TOP:

    My project Documentation
    =========================================

    Welcome!
    ---------------------

    This is the documentation for My project.


    Table of contents
    ---------------------------------

    .. toctree::
      :maxdepth: 1

      extensions/index

As you can see I've referenced another :dfn:`index.rst` file in a subfolder called :dfn:`extensions`. That's where we'll generate all extension docs. This way you can use other sections of the docs to embed more things. Here's the :dfn:`extensions/index.rst`:

.. code-block:: rst

    My project Extensions
    ==================================

    Table of Contents
    -----------------

    .. kl-extlist:: extensions

As you can see, we are already using a custom KL directive. This directive will automatically generate a table of contents for all found extensions.

Finally, you can use this helper script below to generate the docs. You'll need to adapt the paths in the script, of course.

.. code-block:: python

    import os
    import sphinx

    from ASTWrapper import *

    # note: the extsDir also has to be on the FABRIC_EXTS_PATH env var
    extsDir = 'c:\\temp\\exts'
    tmpDir = 'c:\\temp\\build'
    srcDir = 'c:\\temp\\source'
    extSrcDir = os.path.join(srcDir, 'Extensions')
    stageDir = 'c:\\temp\\docs'


    for d in [tmpDir, srcDir, stageDir]:
      if not os.path.exists(d):
        os.makedirs(d)

        os.environ['RST_DOC_SOURCE_EXTS_DIR'] = os.path.join(stageDir, 'Extensions')
    os.environ['RST_DOC_TARGET_EXTS_DIR'] = extSrcDir

    # create the ast manager
    manager = KLManager(paths = [extsDir], header = [])

    # create all extension rst files
    extensions = manager.getKLExtensions()
    for extension in extensions:
      extSrcDir = os.path.join(extSrcDir, extension.getName())
      if not os.path.exists(extSrcDir):
        os.makedirs(extSrcDir)
      extTmpDir = os.path.join(tmpDir, extension.getName())
      if not os.path.exists(extTmpDir):
        os.makedirs(extTmpDir)
      manager.generateKLExtensionRST(extension, extSrcDir, extTmpDir)

    # invoke sphinx
    sphinx.main(['-b html', '-E', '-a', srcDir, stageDir])


Indices and Tables
------------------

* :ref:`genindex`
* :ref:`search`
