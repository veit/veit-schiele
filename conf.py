# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Veit Schiele"
copyright = "2023, Veit Schiele"
author = "Veit Schiele"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_design", "sphinxext.opengraph", "sphinx_copybutton"]

templates_path = ["_templates"]
exclude_patterns = ["README.rst", "lib/*"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"

# Change default HTML title
html_title = "Veit Schiele"

html_static_path = ["_static"]
html_logo = "_static/images/logo/logo.png"
html_favicon = "_static/images/logo/favicon.ico"

# -- Furo options ------------------------------------------------------------
# https://pradyunsg.me/furo/customisation/

html_theme_options = {
    "sidebar_hide_name": True,
}
