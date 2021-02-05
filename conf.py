#!/usr/bin/python3

from typing import Dict, List


def setup(sphinx):
    pass


project = "Maidenlane"
copyright = "2021, Manifold Finance"
author = "Manifold Finance"


# The full version, including alpha/beta/rc tags
with open(
    os.path.join(
        os.path.dirname(__file__), "..", "sphinxcontrib", "soliditydomain", "VERSION"
    )
) as version_file:
    release = version_file.read().strip()
# The short X.Y version
(major, _, rest_of_version) = release.partition(".")
(minor, _, _) = rest_of_version.partition(".")
version = major + "." + minor


# The full version, including alpha/beta/rc tags
release = "v1.0.0"


# -- General configuration ---------------------------------------------------

extensions: List = [
    "sphinx.ext.intersphinx" "sphinx.ext.autodoc",
    "sphinxcontrib.soliditydomain",
]

# source_suffix = ['.rst', '.md']
source_suffix = ".md"

# The master toctree document.
master_doc = "toctree"


templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

pygments_style = "sphinx"


html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# html_theme_options = {}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["css/toggle.css", "css/dark.css"]

html_js_files = ["js/toggle.js"]

html_logo = "logo.svg"

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.


# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Manifold"


# -- Options for LaTeX output ------------------------------------------------

latex_elements: Dict = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, "Manifold.tex", "Manifold Documentation", "manifold.finance", "manual")
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "Maidenlane", "Manifold Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, "Manifold", "Manifold Documentation", author, "Manifold", "", "Vyper",)
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ["search.html"]

intersphinx_mapping = {
    "hypothesis": ("https://hypothesis.readthedocs.io/en/latest", None),
    "pytest": ("https://docs.pytest.org/en/latest/", None),
    "python": ("https://docs.python.org/3.8/", None),
    "web3py": ("https://web3py.readthedocs.io/en/stable/", None),
}

# -- Options for Solidity domain ---------------------------------------------

autodoc_lookup_path = "."

# -- Add Solidity lexer

from sphinx.highlighting import lexers
from pygments_lexer_solidity import SolidityLexer

lexers["solidity"] = SolidityLexer()
