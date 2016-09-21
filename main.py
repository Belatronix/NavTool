import platform
import sys
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDialog, QFileDialog, QDialogButtonBox
from PyQt5.QtCore import *
from dialog_options_ui import Ui_Dialog
from navtool_ui import Ui_MainWindow

__version__ = '0.0.4'
__progname__ = 'NavTool'


class MyApplication(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.dat = pd.DataFrame()
        self.setupUi(self)
        self.setWindowTitle('NavTool')
        self.action_ber_das_NavTool.triggered.connect(self.about)
        self.filename = self.action_ffnen.triggered.connect(self.getfile)
        self.action_ber_den_Autor.triggered.connect(lambda: self.opendialog("What's up here?"))
        self.action_ber_QT.triggered.connect(self.about_qt)
        self.actionBahnregler.triggered.connect(self.open_cu_logfile)
        self.actionLaserscanner.triggered.connect(self.open_ls_logfile)
        self.actionHilfe_zu_den_Tools.triggered.connect(self.text)

    def getfile(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Open Log File', '/home')
        return self.filename

    def open_cu_logfile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open Control Unit Log File', '/home')
        try:
            self.dat = pd.read_csv(file, delimiter=';', low_memory=False)
        except ValueError:
            self.dat = pd.read_csv(file, delimiter=';', encoding='Latin-1', low_memory=False)
        if ('Counter' in self.dat.columns):
            print("Altes Logfile")
            f, ax = plt.subplots(3, sharex=True)
            ax[0].plot(self.dat['Actual Pos X'], "k", color='green', label="Actual")
            ax[1].plot(self.dat['Actual Pos Y'], "k--", color='blue', label="Target")
            ax[2].plot(self.dat['Abweichung 2'], "k", color='red', label="Abw")

            plt.grid()
            plt.legend(loc="best", shadow=True)
            plt.show()
        elif ('Time' in self.dat.columns):
            print("Neues Logfile")
            plt.plot(self.dat['Actual Pos X'], self.dat['Actual Pos Y'], "k", color='green', label="Actual")
            plt.plot(self.dat['Actual Pos X'], self.dat['Abweichung 1'], "k", color='red', label="dX")
            plt.plot(self.dat['Target Pos X'], self.dat['Target Pos Y'], "k--", color='blue', label="Target")
            plt.legend(loc="best", shadow=True, fontsize='x-large')
            plt.grid()
            plt.show()

    def open_ls_logfile(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open Laserscanner Log File', '/home')
        try:
            self.dat = pd.read_csv(file, delimiter=';')
        except IOError as e:
            pass

    def opendialog(self, text=""):
        dialog = QDialog(self)
        dialogui = Ui_Dialog()
        dialogui.setupUi(dialog)
        dialogui.label.setText(text)
        dialogui.radioButton.setChecked(True)
        dialogui.lineEdit.setText("Das ist ein Testtext")
        dialogui.buttonBox.button(QDialogButtonBox.Cancel).clicked.connect(dialog.reject)
        dialogui.buttonBox.button(QDialogButtonBox.Ok).clicked.connect(self.about)
        dialog.exec_()

    def about_qt(self):
        QMessageBox.aboutQt(self)
        print(window.filename)

    def about(self):
        QMessageBox.about(self, "About the Program",
                          ('<b>%s - Ver.%s</b>\n'
                           '            <p align="center">Copyright 2016 Axel Beierlein.\n'
                           '            <p align="center">All rights reserved in accordance with\n'
                           '            GPL v2 or later - NO WARRANTIES!\n'
                           '            <p align="center">This application can be used to\n'
                           '            analyze Log Files.\n'
                           '            <p align="center">Python %s -  PyQt5 version %s - Qt version %s on %s') % (
                              __progname__, __version__, platform.python_version(), PYQT_VERSION, QT_VERSION,
                              platform.system()))

    def text(self):
        QMessageBox.warning(self, "Warning", "Oh no!\nThere is something going wrong!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())  # exec_ instead of 'exec' cause this is an keyword in Python
