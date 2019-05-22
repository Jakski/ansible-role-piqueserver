# -*- coding: utf-8 -*-

# -- Path setup --------------------------------------------------------------

import re


def get_latest_version(changelog):
    '''Retrieve latest version of package from changelog file.'''
    # Match strings like "## [1.2.3] - 2017-02-02"
    regex = r'^##\s*\[(\d+.\d+.\d+)\]\s*-\s*\d{4}-\d{2}-\d{2}$'
    with open(changelog, 'r') as changelog:
        content = changelog.read()
        return re.search(regex, content, re.MULTILINE).group(1)


autoyaml_root = '.'

# -- Project information -----------------------------------------------------

project = 'ansible-role-piqueserver'
copyright = '2019, Jakub Pieńkowski'
author = 'Jakub Pieńkowski'
version = get_latest_version('CHANGELOG')
release = ''

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinxcontrib.autoyaml',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'docs'
language = None
exclude_patterns = ['docs', 'Thumbs.db', '.DS_Store', 'molecule']
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for manual page output ------------------------------------------

man_pages = [
    (master_doc, 'ansible-role-piqueserver', '',
     [author], 1)
]
