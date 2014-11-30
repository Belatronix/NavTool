import sys
import platform
import PySide
from PySide import QtGui
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QDialog
from navtool_ui import Ui_MainWindow
from dialog_options_ui import Ui_Dialog

__version__ = '0.0.1'

class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)
        self.action_ber_das_NavTool.triggered.connect(self.about)
        self.action_ffnen.triggered.connect(self.openfile)
        self.action_ber_den_Autor.triggered.connect(lambda: self.opendialog("Was ist denn hier los?"))
        self.action_ber_QT.triggered.connect(self.about_qt)
        self.actionHilfe_zu_den_Tools.triggered.connect(self.text)

    def about(self):
        QMessageBox.about(self, "Ueber das Programm",
                          """<b>About this Program Version %s</b>
                <p align="center">Copyright 2014 Axel Beierlein.
               <p align="center">All rights reserved in accordance with
               GPL v2 or later - NO WARRANTIES!
               <p align="center">This application can be used for
               displaying OS and platform details.
               <p align="center">Python %s -  PySide version %s - Qt version %s on %s""" % \
                (__version__, platform.python_version(), PySide.__version__,\
                 PySide.QtCore.__version__, platform.system()))

    def about_qt(self):
        QMessageBox.aboutQt(self)

    def text(self):
        QMessageBox.warning(self, "Warnung", "Hups, da ist jetzt was schief gegangen!")

    def openfile(self):
        fname, _ = QtGui.QFileDialog.getOpenFileName(self, 'Log File oeffnen',  '/home')

    def opendialog(self, text=""):
        dialog = QtGui.QDialog(self)
        dialogUI = Ui_Dialog()
        dialogUI.setupUi(dialog)
        dialog.show()
        dialogUI.label.setText(text)
        dialogUI.buttonBox.button(QtGui.QDialogButtonBox.Cancel).clicked.connect(dialog.reject)
        dialogUI.buttonBox.button(QtGui.QDialogButtonBox.Ok).clicked.connect(self.about)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
