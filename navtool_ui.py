# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PycharmProjects/NavTool/navtool.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(602, 197)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 25))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuAnsicht = QtWidgets.QMenu(self.menubar)
        self.menuAnsicht.setObjectName("menuAnsicht")
        self.menuTabellen = QtWidgets.QMenu(self.menuAnsicht)
        self.menuTabellen.setObjectName("menuTabellen")
        self.menuLogs = QtWidgets.QMenu(self.menubar)
        self.menuLogs.setObjectName("menuLogs")
        self.menuViewer = QtWidgets.QMenu(self.menuLogs)
        self.menuViewer.setObjectName("menuViewer")
        self.menuHilfe = QtWidgets.QMenu(self.menubar)
        self.menuHilfe.setObjectName("menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_ffnen = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Test1/Downloads/icons/folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_ffnen.setIcon(icon)
        self.action_ffnen.setIconVisibleInMenu(True)
        self.action_ffnen.setObjectName("action_ffnen")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Test1/Downloads/icons/cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBeenden.setIcon(icon1)
        self.actionBeenden.setIconVisibleInMenu(True)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionHilfe_zu_den_Tools = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Test1/Downloads/icons/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHilfe_zu_den_Tools.setIcon(icon2)
        self.actionHilfe_zu_den_Tools.setIconVisibleInMenu(True)
        self.actionHilfe_zu_den_Tools.setObjectName("actionHilfe_zu_den_Tools")
        self.action_ber_das_NavTool = QtWidgets.QAction(MainWindow)
        self.action_ber_das_NavTool.setObjectName("action_ber_das_NavTool")
        self.actionLaserscanner = QtWidgets.QAction(MainWindow)
        self.actionLaserscanner.setObjectName("actionLaserscanner")
        self.actionBahnregler = QtWidgets.QAction(MainWindow)
        self.actionBahnregler.setObjectName("actionBahnregler")
        self.actionKonsistenzcheck = QtWidgets.QAction(MainWindow)
        self.actionKonsistenzcheck.setToolTip("Mit diesem Konsistenzcheck werden Reihen aus den CSV Dateien herausgefiltert, die nicht der korrekten Reihenlänge entsprechen.")
        self.actionKonsistenzcheck.setObjectName("actionKonsistenzcheck")
        self.actionSegment = QtWidgets.QAction(MainWindow)
        self.actionSegment.setObjectName("actionSegment")
        self.actionSegmente = QtWidgets.QAction(MainWindow)
        self.actionSegmente.setObjectName("actionSegmente")
        self.actionLaserscanner_2 = QtWidgets.QAction(MainWindow)
        self.actionLaserscanner_2.setObjectName("actionLaserscanner_2")
        self.actionTransponder = QtWidgets.QAction(MainWindow)
        self.actionTransponder.setObjectName("actionTransponder")
        self.actionSpeichern = QtWidgets.QAction(MainWindow)
        self.actionSpeichern.setObjectName("actionSpeichern")
        self.action_ber_den_Autor = QtWidgets.QAction(MainWindow)
        self.action_ber_den_Autor.setObjectName("action_ber_den_Autor")
        self.action_ber_QT = QtWidgets.QAction(MainWindow)
        self.action_ber_QT.setObjectName("action_ber_QT")
        self.menuDatei.addAction(self.action_ffnen)
        self.menuDatei.addAction(self.actionSpeichern)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionBeenden)
        self.menuTabellen.addAction(self.actionSegmente)
        self.menuTabellen.addAction(self.actionTransponder)
        self.menuTabellen.addAction(self.actionLaserscanner_2)
        self.menuAnsicht.addAction(self.menuTabellen.menuAction())
        self.menuAnsicht.addAction(self.actionSegment)
        self.menuViewer.addAction(self.actionLaserscanner)
        self.menuViewer.addAction(self.actionBahnregler)
        self.menuLogs.addAction(self.menuViewer.menuAction())
        self.menuHilfe.addAction(self.actionHilfe_zu_den_Tools)
        self.menuHilfe.addAction(self.action_ber_das_NavTool)
        self.menuHilfe.addAction(self.action_ber_den_Autor)
        self.menuHilfe.addAction(self.action_ber_QT)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuAnsicht.menuAction())
        self.menubar.addAction(self.menuLogs.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        self.actionBeenden.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NavTool"))
        self.menuDatei.setTitle(_translate("MainWindow", "File"))
        self.menuAnsicht.setTitle(_translate("MainWindow", "Ansicht"))
        self.menuTabellen.setTitle(_translate("MainWindow", "Tabellen"))
        self.menuLogs.setTitle(_translate("MainWindow", "Logs"))
        self.menuViewer.setTitle(_translate("MainWindow", "Viewer"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Help"))
        self.action_ffnen.setText(_translate("MainWindow", "Öffnen"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))
        self.actionHilfe_zu_den_Tools.setText(_translate("MainWindow", "Hilfe zu den Tools"))
        self.action_ber_das_NavTool.setText(_translate("MainWindow", "Über das NavTool"))
        self.actionLaserscanner.setText(_translate("MainWindow", "Laserscanner"))
        self.actionBahnregler.setText(_translate("MainWindow", "Bahnregler"))
        self.actionKonsistenzcheck.setText(_translate("MainWindow", "Konsistenzcheck"))
        self.actionSegment.setText(_translate("MainWindow", "Segmente"))
        self.actionSegmente.setText(_translate("MainWindow", "Segmente"))
        self.actionLaserscanner_2.setText(_translate("MainWindow", "Lasermarken"))
        self.actionTransponder.setText(_translate("MainWindow", "Transponder"))
        self.actionSpeichern.setText(_translate("MainWindow", "Speichern"))
        self.action_ber_den_Autor.setText(_translate("MainWindow", "Über den Autor"))
        self.action_ber_QT.setText(_translate("MainWindow", "Über QT"))

# import navrc_rc
