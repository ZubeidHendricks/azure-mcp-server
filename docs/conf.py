# Configuration file for the Sphinx documentation builder.

import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

# Project information
project = 'Azure DevOps MCP Server'
copyright = '2024, Zubeid Hendricks'
author = 'Zubeid Hendricks'
release = '0.1.0'

# General configuration
extensions = [
    'sphinx.ext.autodoc',  # Auto-generate documentation from docstrings
    'sphinx.ext.viewcode', # Add source code links
    'sphinx.ext.napoleon', # Support for Google and NumPy docstring styles
]

# Path settings
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# HTML output settings
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
