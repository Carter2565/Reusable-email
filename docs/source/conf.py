# Configuration file for the Sphinx documentation builder.

import os
import sys
# sys.path.insert(0, os.path.abspath('../../'))  # Adjust the path as needed
# sys.path.insert(0, os.path.abspath('..'))
# -- Project information

print(sys.path)

project = 'Reusable.email'
author = 'Carter2565'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# Path to static files
html_static_path = ['_static']

# Include DarkReader CSS
# html_css_files = [
#     'dark_mode.css',
# ]


# -- Options for EPUB output
epub_show_urls = 'footnote'
