import sys
import platform
import PySide
import numpy as np
import matplotlib
#matplotlib.use('Qt4Agg')
from PySide import QtGui

from PySide.QtGui import QApplication, QMainWindow, QMessageBox
import matplotlib.backends.backend_qt4agg
from matplotlib.figure import Figure

from navtool_ui import Ui_MainWindow
from dialog_options_ui import Ui_Dialog


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
                           '            <p align="center">Python %s -  PySide version %s - Qt version %s on %s') % (
                              __progname__, __version__, platform.python_version(), PySide.__version__, PySide.QtCore.__version__,
                              platform.system()))

    def text(self):
        QMessageBox.warning(self, "Waning", "Oh no!\nThere is something going wrong!")

    def openfile(self):
        try:
            fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Open Log File', '/home')
        except IOError:
            QMessageBox.warning(self, "Error" "While opening the File")

    def opendialog(self, text=""):
        dialog = QtGui.QDialog(self)
        dialogui = Ui_Dialog()
        dialogui.setupUi(dialog)
        dialog.show()
        dialogui.label.setText(text)
        dialogui.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(dialog.reject)
        dialogui.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.about)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())  # exec_ instead of 'exec' cause this is an keyword in Python
