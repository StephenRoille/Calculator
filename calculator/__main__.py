"""Lauch a simple graphical user interface to perform arithmetic operations.

Usage
-----
calculator [-h|--help]

Options
-------
-h, --help    Show this help message

Notes
-----
This script is executed by running one of the following command:
- $ python -m calculator
- $ calculator
"""
import sys

from PyQt5 import QtWidgets

from calculator import Calculator


def open() -> None:
    """Display the graphical user interface to the user."""
    app = QtWidgets.QApplication([])
    win = Calculator()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if "-h" in sys.argv or "--help" in sys.argv:
            print(__doc__)
        else:
            args = "\n - ".join(sys.argv[1:])
            print(f"Unknown arguments:\n - {args}")
        exit(1)

    open()
