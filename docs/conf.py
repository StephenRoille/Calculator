import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

import calculator  # noqa: E402

# ======================================================================
#                             PROJECT INFO
# ======================================================================

project = calculator.__package__.title()
copyright = calculator.__copyright__
author = calculator.__author__
version = calculator.__version__

# ======================================================================
#                               GENERAL
# ======================================================================

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
extensions = []
modindex_common_prefix = ["calculator."]
pygments_style = "friendly"  # https://help.farbox.com/pygments.html
templates_path = ["_templates"]
# rst_epilog = (pathlib.Path.cwd() / "_utils" / "links.txt").read_text()
rst_prolog = f"""
.. |version| replace:: {version}
"""

# ======================================================================
#                                 HTML
# ======================================================================

html_css_files = []
html_favicon = "_static/svg/pypi.svg"
html_logo = "_static/svg/pypi.svg"
html_static_path = ["_static"]
html_theme = "sphinx_materialdesign_theme" or "sphinx_rtd_theme"
html_use_index = True  # alphabetical objects list

# ======================================================================
#                                THEMES
# ======================================================================

# material design theme
# ---------------------
# url https://github.com/myyasuda/sphinx_materialdesign_theme
# pip install sphinx_materialdesign_theme
if html_theme == "sphinx_materialdesign_theme":
    html_css_files.append("material_design/custom-admonition.css")
    html_css_files.append("material_design/custom-rubric.css")
    html_theme_options = {
        "header_links": [
            ("Home", "index", False, "home"),
            ("API", "api/toc", False, "fingerprint"),
            ("PyPI", calculator.__pypi__, True, "link"),
            ("GitHub", calculator.__repo__, True, "link"),
        ],
        "primary_color": "blue",
        "accent_color": "pink",
        "fixed_drawer": True,
        "fixed_header": True,
        "header_waterfall": True,
        "header_scroll": False,
        "show_header_title": False,
        "show_drawer_title": True,
        "show_footer": True,
    }

# ======================================================================
#                               EXTENSIONS
# ======================================================================

# sphinx.ext.autosectionlabel
# ----------------------
extensions.append("sphinx.ext.autosectionlabel")
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# sphinx.ext.autosummary
# ----------------------
extensions.append("sphinx.ext.autosummary")
autosummary_generate = True

# sphinx.ext.coverage
# -------------------
extensions.append("sphinx.ext.coverage")

# sphinx.ext.doctest
# ------------------
extensions.append("sphinx.ext.doctest")

# sphinx.ext.extlinks
# -------------------
extensions.append("sphinx.ext.extlinks")
extlinks = {
    # project
    "github": ("https://github.com/StephenRoille/%s/", " "),
    "issue": ("https://github.com/StephenRoille/calculator/issues/%s", " "),
    # dynamic
    "pypi": ("https://pypi.org/project/%s/", " "),
}

# sphinx.ext.mathjax
# ------------------
extensions.append("sphinx.ext.mathjax")

# sphinx.ext.napoleon
# -------------------
extensions.append("sphinx.ext.napoleon")
napoleon_google_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
napoleon_numpy_docstring = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = False
napoleon_use_rtype = False

# sphinx.ext.todo
# ---------------
extensions.append("sphinx.ext.todo")
todo_include_todos = True

# sphinx.ext.viewcode
# -------------------
extensions.append("sphinx.ext.viewcode")

# sphinxcontrib.spelling
# ----------------------
# url https://github.com/sphinx-contrib/spelling
# pip install sphinxcontrib-spelling
extensions.append("sphinxcontrib.spelling")
spelling_word_list_filename = "_utils/spelling_wordlist.txt"
spelling_show_suggestions = True
