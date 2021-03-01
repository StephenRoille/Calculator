[![coverage: 46%][coverage_badge]][coverage]
[![Hypothesis; Tested][hypothesis_badge]][hypothesis]
[![License GUI: GPLv3][license_badge_gui]][license_gui]
[![PyPI: 0.1.0][pypi_badge]][pypi]
[![SemVer: 2.0.0][semver_badge]][semver]
[![style: Black][black_badge]][black]

**Calculator** is written using Python and the [**PyQt5**][pyqt5] framework.


## Installation (Python 3.6+)

The `calculator` package is available from [PyPI][pypi] and requires Python 3.6+. It
offers a simple [graphical-user interface][gui] (GUI).

We recommend using [pipx][pipx]. Follow the [pipx installation][pipx_install] guide,
then proceed to install the `calculator` package with `pipx`,

```shell
pipx install calculator
```

The `calculator` [command-line interface][cli] (CLI) utility is now globally available
to start the builtin GUI, but remains isolated and easily manageable via the excellent
`pipx` CLI.


## Links

Interested in the `calculator` project? Click one of the following links to dive deeper.

* Install the package from [**PyPI**][pypi]
* Read the official documentation on [**Read the Docs**][docs]
* Fork or contribute to the project on [**GitHub**][github]
* Learn permissions and conditions of the [**GNU GPLv3**][license_gui] license
* Follow and report [**bugs**][bugs]
* Report vulnerabilities to [stephen.roille@gmail.com][email]


## License

![][gplv3_logo]

The `calculator` project is licensed under the [**GNU GPLv3**][license_gui] license.

The dedicated GUI was designed and developed using the [**Qt**][qt] framework and the [**PyQt5**][pyqt5] library. Since [**PyQt5**][pyqt5] is licensed under [**GNU GPLv3**][license_gui], the `calculator` GUI (`calculator.gui` sub-package) MUST comply to its terms.


<!-- project links -->
[bugs]: https://github.com/StephenRoille/calculator/issues
[cite]: https://matplotlib.org/citing.html
[coverage]: coverage/index.html
[docs]: https://stephenroille.github.io/Calculator/
[doi]: https://doi.org/10.5281/zenodo.0000000
[github]: https://github.com/StephenRoille/calculator
[pypi]: https://pypi.org/project/Calculator/
[src]: https://github.com/StephenRoille/calculator
[email]: mailto:stephen.roille@gmail.com

<!-- badges links -->
[black]: https://github.com/psf/black
[black_badge]: https://img.shields.io/badge/style-Black-black.svg
[coverage_badge]: https://img.shields.io/badge/coverage-46%25-orange.svg
[doi_badge]: https://zenodo.org/badge/DOI/10.5281/zenodo.0000000.svg
[hypothesis]: https://hypothesis.readthedocs.io/en/latest/
[hypothesis_badge]: https://img.shields.io/badge/Hypothesis-tested-brightgreen.svg
[license]: https://www.gnu.org/licenses/lgpl-3.0.en.html
[license_gui]: https://www.gnu.org/licenses/gpl-3.0.en.html
[license_badge_gui]: https://img.shields.io/badge/License%20GUI-GPLv3-darkred.svg
[pypi_badge]: https://img.shields.io/badge/PyPI-0.1.0-blue.svg
[semver]: https://semver.org/spec/v2.0.0.html
[semver_badge]: https://img.shields.io/badge/SemVer-2.0.0-lightgray.svg

<!-- other libraries -->
[pipx]: https://github.com/pipxproject/pipx
[pipx_install]: https://pipxproject.github.io/pipx/installation/
[qt]: https://www.qt.io/
[pyqt5]: https://www.riverbankcomputing.com/software/pyqt/

<!-- wikis -->
[liquid-crystal]: https://en.wikipedia.org/wiki/Liquid_crystal
[slm]: https://en.wikipedia.org/wiki/Spatial_light_modulator
[cli]: https://en.wikipedia.org/wiki/Command-line_interface
[gui]: https://en.wikipedia.org/wiki/Graphical_user_interface

<!-- images -->
[gplv3_logo]: https://www.gnu.org/graphics/gplv3-88x31.png
