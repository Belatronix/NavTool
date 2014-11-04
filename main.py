import sys
from PySide import QtGui
from navtool_ui import Ui_MainWindow


class MyApplication(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyApplication, self).__init__(parent)
        self.setupUi(self)

    def newwindow(self):
        self.wid = QtGui.QWidget()
        self.wid.resize(250, 150)
        self.wid.setWindowTitle('NewWindow')
        self.wid.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec_())
