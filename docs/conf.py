import os
import sys

sys.path.insert(0, os.path.abspath('.'))

project = 'IObit Advanced'
author = 'Adele Collins'
release = '1.0'

extensions = ['sphinx_rtd_theme']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_meta = {
    "google-site-verification": "nkfFWEaHXct0Lyzc10Hl3Dmo91U7cTPvV0aSmyH4PaA"
}
