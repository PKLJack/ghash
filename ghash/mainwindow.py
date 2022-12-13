import json
from pathlib import Path
from pprint import pprint as pp

from PySide6.QtCore import QSortFilterProxyModel, Slot
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QHeaderView,
    QMainWindow,
    QMessageBox,
    QTableView,
    QWidget,
)

from .hasher import FileHasher
from .models import TableModel
from .ui_mainwindow import Ui_MainWindow
from .utils import dict_unnest


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, app: QApplication) -> None:
        super().__init__()
        self.setupUi(self)
        self.app = app

        self.checkboxes_sha: list[QCheckBox] = [
            self.checkbox_sha1,
            self.checkbox_sha224,
            self.checkbox_sha256,
            self.checkbox_sha384,
            self.checkbox_sha512,
        ]

        self.checkboxes_others: list[QCheckBox] = [
            self.checkbox_md5,
            self.checkbox_crc32,
        ]

        self.enabled_hashes = {
            "sha1": True,  # Keep this
            "sha224": False,
            "sha256": False,
            "sha384": False,
            "sha512": False,
            "md5": False,
            "crc32": False,
        }
        self.dic_of_hashes: dict[str, dict[str, str]]

        self.checkbox_sha1.setChecked(True)  # Keep this
        self.connect_checkboxes()
        self.connect_buttons()
        self.label_drag_and_drop.accepted.connect(self.handle_accepted)

        self.table_model_all: TableModel
        self.filepaths: list[Path] = []
        # self.table_view_all.setSortingEnabled(True)  # TODO maybe not
        self.table_view_all.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeToContents
        )
        self.table_view_all.horizontalHeader().setStretchLastSection(True)

    def connect_checkboxes(self):
        """Connect signals for checkboxes"""

        def make_toggle_hash(algo: str):
            assert algo in self.enabled_hashes, f"Wrong algo: {algo}"

            @Slot(int)
            def inner(x: int):
                self.enabled_hashes[algo] = x == 2  #  2 means checked

            return inner

        self.checkbox_sha1.stateChanged.connect(make_toggle_hash("sha1"))
        self.checkbox_sha224.stateChanged.connect(make_toggle_hash("sha224"))
        self.checkbox_sha256.stateChanged.connect(make_toggle_hash("sha256"))
        self.checkbox_sha384.stateChanged.connect(make_toggle_hash("sha384"))
        self.checkbox_sha512.stateChanged.connect(make_toggle_hash("sha512"))
        self.checkbox_md5.stateChanged.connect(make_toggle_hash("md5"))
        self.checkbox_crc32.stateChanged.connect(make_toggle_hash("crc32"))

    def connect_buttons(self):
        """ """
        self.button_calculate.clicked.connect(self.handle_calculate)
        self.button_copy_json.clicked.connect(self.to_clipboard_json)
        self.button_copy_tsv.clicked.connect(self.to_clipboard_tsv)
        self.button_clear.clicked.connect(self.clear_tabs)

    # def resizeEvent(self, event):
    #     """Intercept resize event"""
    #     print(repr(event))
    #     return super().resizeEvent(event)

    @Slot()
    def handle_calculate(self):
        """ """
        self.run_hash()

    @Slot()
    def handle_accepted(self, filepaths: list[Path]):
        """ """
        self.filepaths = filepaths
        self.run_hash()

    def run_hash(self):
        """ """
        if not self.filepaths:
            QMessageBox.information(
                self, "Files required", "Please provide at least 1 file."
            )
            return

        retval: dict[str, dict[str, str]] = dict()

        for algo, enabled in self.enabled_hashes.items():
            if not enabled:
                continue

            retval[algo] = dict()

            for fp in self.filepaths:
                hasher = FileHasher(file_path=fp, algorithm=algo)
                retval[algo][str(fp)] = hasher.run()

        if not retval:
            QMessageBox.information(
                self, "Algorithm required", "Please select at least 1 algorithm."
            )
            return

        self.dic_of_hashes = retval
        self.spawn_tabs(self.dic_of_hashes)

    def clear_tabs(self):
        """Remove all tabs except first tab and clear first tab."""
        for i in range(self.tab_widget.count() - 1, 0, -1):
            self.tab_widget.widget(i).deleteLater()
            self.tab_widget.removeTab(i)

            try:
                self.table_model_all.clear_all()
            except Exception as e:
                print(e)
                pass  # TODO: rewrite

    def spawn_tabs(self, dic: dict[str, dict[str, str]]):
        """Refresh the TabWidget."""
        self.clear_tabs()

        list1 = dict_unnest(dic, keep_algo=True)

        # Tab: All
        self.table_model_all = TableModel(hashes=list1)
        self.table_view_all.setModel(self.table_model_all)

        for i in range(self.tab_widget.count() - 1, 0, -1):
            self.tab_widget.widget(i).deleteLater()
            self.tab_widget.removeTab(i)

        for algo in dic.keys():

            proxy_model = QSortFilterProxyModel(self)
            proxy_model.setSourceModel(self.table_model_all)
            proxy_model.setFilterKeyColumn(1)
            proxy_model.setFilterFixedString(algo)

            table_view = QTableView(self)
            table_view.setModel(proxy_model)

            table_view.horizontalHeader().setSectionResizeMode(
                QHeaderView.ResizeToContents
            )
            table_view.horizontalHeader().setStretchLastSection(True)

            table_view.hideColumn(1)

            shim_widget = QWidget()
            horizontalLayout = QHBoxLayout(shim_widget)
            horizontalLayout.addWidget(table_view)

            # self.tab_widget.addTab(table_view, algo)
            self.tab_widget.addTab(shim_widget, algo)

    @Slot()
    def to_clipboard_json(self):
        """ """
        clipboard = self.app.clipboard()

        algo = self.tab_widget.tabText(self.tab_widget.currentIndex())

        if algo.lower() == "all":
            clipboard.setText(json.dumps(self.dic_of_hashes))
        else:
            clipboard.setText(json.dumps(self.dic_of_hashes[algo]))

    @Slot()
    def to_clipboard_tsv(self):
        """ """
        clipboard = self.app.clipboard()

        algo = self.tab_widget.tabText(self.tab_widget.currentIndex())

        lines = []

        if algo.lower() == "all":
            for row in dict_unnest(self.dic_of_hashes, True):
                lines.append("\t".join(row) + "\n")

            clipboard.setText("".join(lines))

        else:
            for k, v in self.dic_of_hashes[algo].items():  # k is file, v is hash
                lines.append(f"{k}\t{v}\n")

            clipboard.setText("".join(lines))
