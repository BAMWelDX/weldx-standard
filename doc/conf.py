# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Local build command ------------------------------------------------------------------

# sphinx-build -W -n -b html -d build/doctrees doc build/html --keep-going

# -- Path setup --------------------------------------------------------------
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import datetime
import os
import shutil
from pathlib import Path

SCHEMA_PATH = Path("../resources")

# -- copy manifest files to schema folder ----------------------------------------------
manifest_dir = SCHEMA_PATH / "schemas/manifests/"
manifest_dir.mkdir(parents=True, exist_ok=True)
manifest_files = (SCHEMA_PATH / "manifests").glob("*.yaml")
for f in manifest_files:
    shutil.copy(f, manifest_dir)

# -- Project information -----------------------------------------------------
_now = datetime.datetime.now().year

project = "weldx-standard"
copyright = f"2020 - {_now}, BAM"
author = "BAM"

# The full version, including alpha/beta/rc tags
release = "0.0.1"

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_copybutton",
    "sphinx_asdf",
    "sphinx.ext.intersphinx",
]


# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = "index"


# -- sphinx-asdf configuration -------------------------------------------------
# This variable indicates the top-level directory containing schemas.
# The path is relative to the location of conf.py in the package
asdf_schema_path = os.path.relpath(str(SCHEMA_PATH))
# This variable indicates the standard prefix that is common to all schemas
# provided by the package.
asdf_schema_standard_prefix = "schemas/"

# enable references to the ASDF Standard documentation
asdf_schema_reference_mappings = [
    (
        "tag:stsci.edu:asdf",
        "http://asdf-standard.readthedocs.io/en/latest/generated/stsci.edu/asdf/",
    ),
    (
        "asdf://weldx.bam.de/weldx/tags/",
        "http://weldx.readthedocs.io/en/latest/generated/weldx.bam.de/weldx/",
    ),
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# The name of an image file (relative to html_static_path) to place at the top
# of the sidebar.
html_logo = "_static/WelDX_notext.svg"
html_favicon = "_static/WelDX_notext.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_theme_options = {
    "external_links": [
        {"url": "https://weldx.readthedocs.io/", "name": "WelDX"},
        {"url": "https://asdf.readthedocs.io/", "name": "ASDF"},
    ],
    "github_url": "https://github.com/BAMWelDX/weldx-standard",
    "twitter_url": "https://twitter.com/BAMweldx",
    "use_edit_page_button": False,
    "show_prev_next": False,
    "collapse_navigation": True,
    "navigation_depth": 4,
}

html_context = {
    "github_user": "BAMWelDX",
    "github_repo": "weldx-standard",
    "github_version": "main",
    "doc_path": "doc",
}


intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "asdf": ("https://asdf.readthedocs.io/en/latest/", None),
    "weldx": ("https://weldx.readthedocs.io/en/latest/", None)
}

# Enable better object linkage ---------------------------------------------------------

# This option basically turns every Markdown like inline code block into a sphinx
# reference
default_role = "py:obj"

# see:
# https://stackoverflow.com/questions/34052582/how-do-i-refer-to-classes-and-methods-in-other-files-my-project-with-sphinx
