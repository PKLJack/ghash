""" 
For promoting wdiget
"""
from pathlib import Path

from PySide6.QtCore import Signal
from PySide6.QtGui import QDragEnterEvent, QDropEvent
from PySide6.QtWidgets import QLabel, QMessageBox

from .utils import flatten_dirs


class DNDLabel(QLabel):

    accepted = Signal(list)

    def dragEnterEvent(self, e: QDragEnterEvent):

        # if e.mimeData().hasFormat("text/plain"):
        if e.mimeData().hasFormat("text/uri-list"):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QDropEvent):
        qt_urls = e.mimeData().urls()

        filepaths = [Path(x.toLocalFile()) for x in qt_urls]
        filepaths = flatten_dirs(filepaths)

        for fp in filepaths:
            if not fp.exists():
                QMessageBox.warning(self, "File Not Found", f"Cannot locate\n{str(fp)}")
                return

        self.accepted.emit(filepaths)
