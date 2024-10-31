#!/usr/bin/env python3
# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use pl.Path.resolve to make it absolute, like shown here.
#
import os
import sys
import pathlib as pl
sys.path.insert(0, pl.Path('../').resolve())

# (Relative to this file):
templates_path   = ['_templates']
html_static_path = ['_static']

# Relative to static dir, or fully qualified urls
html_css_files = ["custom.css"]
html_js_files  = []
# html_style = "custom.css"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['**/flycheck_*.py', "**/__tests/*"]

# -- Project information -----------------------------------------------------

project   = 'Mostly Harmless'
copyright = '2022, jgrey'
author    = 'jgrey'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx.ext.extlinks',
    'sphinx_rtd_theme',
    'myst_parser',
    "autoapi.extension",
    "sphinx.ext.coverage",
    "sphinx.ext.imgconverter",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    ]

maximum_signature_line_length = 50
toc_object_entries            = True
master_doc                    = "index"
show_warning_types            = True

html_theme          = "sphinx_rtd_theme"
html_theme_options  = {}
html_sidebars       = {}
html_domain_indices = True
html_use_index      = True


html_theme_options.update({
    'logo_only'                   : False,
    'display_version'             : True,
    'prev_next_buttons_location'  : 'bottom',
    'style_external_links'        : False,
    'vcs_pageview_mode'           : '',
    'style_nav_header_background' : 'grey',
    # TOC options:
    'collapse_navigation'         : True,
    'sticky_navigation'           : True,
    'navigation_depth'            : 4,
    'includehidden'               : True,
    'titles_only'                 : False

})


# -- Python Options -------------------------------------------------
add_module_names                   = False
modindex_common_prefix             = ["doot."]
python_display_short_literal_types = True


# -- Extension Options -------------------------------------------------
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html
autoapi_generate_api_docs = True
autoapi_add_toctree_entry = True
autoapi_type              = "python"
autoapi_template_dir      = "_templates"
autoapi_root              = "autoapi"
autoapi_dirs              = ['../doot']
autoapi_file_patterns     = ["*.py", "*.pyi"]
autoapi_ignore            = ['*/__tests', '*/test_*.py', '/obsolete/*']
autoapi_options           = [
    'imported-members',
    'members',
    # 'undoc-members',
    'private-members',
    'special_members',
    'show-inheritance',
    # 'show-inheritance-diagram',
    # 'show-module-summary',
]

# -- Imports --------------------------------------------------
