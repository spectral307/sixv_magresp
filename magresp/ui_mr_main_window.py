# Form implementation generated from reading ui file 'mr_main_window.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MrMainWindow(object):
    def setupUi(self, MrMainWindow):
        MrMainWindow.setObjectName("MrMainWindow")
        MrMainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MrMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MrMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MrMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MrMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MrMainWindow)
        self.statusbar.setObjectName("statusbar")
        MrMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MrMainWindow)
        QtCore.QMetaObject.connectSlotsByName(MrMainWindow)

    def retranslateUi(self, MrMainWindow):
        _translate = QtCore.QCoreApplication.translate
        MrMainWindow.setWindowTitle(_translate("MrMainWindow", "АХ"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MrMainWindow = QtWidgets.QMainWindow()
    ui = Ui_MrMainWindow()
    ui.setupUi(MrMainWindow)
    MrMainWindow.show()
    sys.exit(app.exec())
