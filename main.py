import platform
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog, QDialogButtonBox
from PyQt5.QtCore import *
from dialog_options_ui import Ui_Dialog
from navtool_ui import Ui_MainWindow

__version__ = '0.0.3'
__progname__ = 'NavTool'


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)
        self.action_ber_das_NavTool.triggered.connect(self.about)
        self.action_ffnen.triggered.connect(self.openfile)
        self.action_ber_den_Autor.triggered.connect(lambda: self.opendialog("What's up here?"))
        self.action_ber_QT.triggered.connect(self.about_qt)
        self.actionHilfe_zu_den_Tools.triggered.connect(self.text)

    def about_qt(self):
        QMessageBox.aboutQt(self)

    def about(self):
        QMessageBox.about(self, "About the Program",
                          ('<b>%s - Ver.%s</b>\n'
                           '            <p align="center">Copyright 2015 Axel Beierlein.\n'
                           '            <p align="center">All rights reserved in accordance with\n'
                           '            GPL v2 or later - NO WARRANTIES!\n'
                           '            <p align="center">This application can be used for\n'
                           '            displaying OS and platform details.\n'
                           '            <p align="center">Python %s -  PyQt5 version %s - Qt version %s on %s') % (
                              __progname__, __version__, platform.python_version(), PYQT_VERSION, QT_VERSION,
                              platform.system()))

    def text(self):
        QMessageBox.warning(self, "Warning", "Oh no!\nThere is something going wrong!")

    def openfile(self):
        try:
            fname, _ = QFileDialog.getOpenFileName(self, 'Open Log File', '/home')
        except IOError:
            QMessageBox.warning(self, "Error" "While opening the File")

    def opendialog(self, text=""):
        dialog = QDialog(self)
        dialogui = Ui_Dialog()
        dialogui.setupUi(dialog)
        dialog.show()
        dialogui.label.setText(text)
        dialogui.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(dialog.reject)
        dialogui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.about)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())  # exec_ instead of 'exec' cause this is an keyword in Python
