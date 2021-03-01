import functools
import pathlib
from typing import Callable

from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5 import uic


IMG_PATH = (pathlib.Path(__file__).parent / "img").resolve()
UI_PATH = (pathlib.Path(__file__).parent / "uis").resolve()


class Calculator(QtWidgets.QMainWindow):
    """Calculator user interface."""

    # =======
    # DUNDERS
    # =======
    def __init__(self) -> None:
        """Class constructor."""
        QtWidgets.QMainWindow.__init__(self)
        self.setWindowIcon(QtGui.QIcon(str(IMG_PATH / "pypi.svg")))
        self.init_layout("calculator.ui")
        self.init_events()
        self.res = []

    # ============
    # INIT METHODS (by order of execution)
    # ============
    def init_layout(self, filepath: str) -> None:
        """Initialize user interface layout from ``.ui`` file.

        Parameters
        ----------
        filepath : str
            filepath relative to the ``uic`` directory

        Raises
        ------
        TypeError
            if ``filepath`` is not :class:`str`
        FileNotFoundError
            if ``filepath`` does not exist
        """
        from . import metadata

        if not isinstance(filepath, str):
            raise TypeError(f"'ui_layout' must be {str}, got {type(filepath)}.")

        filepath = UI_PATH / filepath
        if not filepath.is_file():
            raise FileNotFoundError(f"'ui_layout' not Found:\n  {filepath}.")

        uic.loadUi(UI_PATH / str(filepath), self)
        self.setWindowTitle(metadata["project"].title() + " " + metadata["version"])

    def init_events(self) -> None:
        """Bind widgets to callbacks."""
        self.num_0.clicked.connect(functools.partial(self.store, "0"))
        self.num_1.clicked.connect(functools.partial(self.store, "1"))
        self.num_2.clicked.connect(functools.partial(self.store, "2"))
        self.num_3.clicked.connect(functools.partial(self.store, "3"))
        self.num_4.clicked.connect(functools.partial(self.store, "4"))
        self.num_5.clicked.connect(functools.partial(self.store, "5"))
        self.num_6.clicked.connect(functools.partial(self.store, "6"))
        self.num_7.clicked.connect(functools.partial(self.store, "7"))
        self.num_8.clicked.connect(functools.partial(self.store, "8"))
        self.num_9.clicked.connect(functools.partial(self.store, "9"))
        self.op_add.clicked.connect(functools.partial(self.store, "+"))
        self.op_sub.clicked.connect(functools.partial(self.store, "-"))
        self.op_div.clicked.connect(functools.partial(self.store, "/"))
        self.op_mul.clicked.connect(functools.partial(self.store, "*"))
        self.op_eq.clicked.connect(self.calculate)
        self.op_reset.clicked.connect(self.reset)

    # =======
    # GETTERS
    # =======
    @property
    def clsname(self) -> str:
        """Class name (:class:`str`, read-only).

        This attribute is a wrapper around ``self.__class__.__name__``,
        """
        return self.__class__.__name__

    @property
    def qualname(self) -> str:
        """Fully qualified name (:class:`str`, read-only)

        This attribute represents the import name and includes package, sub-package(s)
        (if any), and the class name.
        """
        pkg, subpkg, *_ = __name__.split(".")
        return f"{pkg}.{subpkg}.{self.clsname}"

    # ===============
    # CORE OPERATIONs
    # ===============
    def update_display(f) -> Callable:
        """Update the calculator display to reflect the character pressed."""

        @functools.wraps(f)
        def inner(self, *args, **kwargs) -> None:
            result = f(self, *args, **kwargs)
            if result is None:
                result = "".join(self.res)
            self.display.setText(result)

        return inner

    @update_display
    def reset(self, *arg) -> None:
        """Reset the calculator state.

        Parameters
        ----------
        *arg
            any argument forwarded by the Qt framework when instantiating the object
        """
        self.res = []

    @update_display
    def store(self, char: str, *args) -> None:
        """Store character pressed.

        Parameters
        ----------
        char : :class:`str`
            character among (``0``, ``1``, ``3``, ``3``, ``4``, ``5``, ``6``, ``7``,
            ``8``, ``9``, ``+``, ``-``, ``/``, and ``*``)
        *args
            any argument forwarded by the Qt framework when instantiating the object
        """
        is_op = char in ("+", "-", "*", "/")
        first_valid_char = (*[str(_) for _ in range(1, 10)], "-", "+")
        # stay idle if first character is invalid
        if len(self.res) == 0 and char not in first_valid_char:
            return

        # replace last operation with new operation
        elif is_op and len(self.res) > 0 and self.res[-1] in ("+", "-", "*", "/"):
            self.res[-1] = char
            if len(self.res) == 1 and char in ("/", "*"):
                self.res = []
        else:
            self.res.append(char)
        return "".join(self.res)

    @update_display
    def calculate(self, *args) -> None:
        """Perform arithmetic operation based on the characters pressed since last
        calculation or last reset.

        Parameters
        ----------
        *args
            any argument forwarded by the Qt framework when instantiating the object
        """
        res_string = "".join(self.res)
        if res_string != "" and res_string[-1] not in ("+", "-", "*", "/"):
            res = str(eval(res_string))  # nosec
            self.res = [res]
            return res
