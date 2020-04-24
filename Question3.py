# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 591)

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 331, 51))
        font = QtGui.QFont()
        font.setPointSize(22)

        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(0, 0, 127);\n" "color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 90, 441, 271))
        self.listWidget.setObjectName("listWidget")
        self.buttonDelete = QtWidgets.QPushButton(self.centralWidget)
        self.buttonDelete.setGeometry(QtCore.QRect(480, 100, 161, 27))
        self.buttonDelete.setStyleSheet("color: rgb(255, 0, 0);")

        icon = QtGui.QIcon.fromTheme("ASA")
        self.buttonDelete.setIcon(icon)
        self.buttonDelete.setObjectName("buttonDelete")
        self.buttonAdd = QtWidgets.QPushButton(self.centralWidget)
        self.buttonAdd.setGeometry(QtCore.QRect(130, 480, 449, 27))
        self.buttonAdd.setObjectName("buttonAdd")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 440, 449, 27))
        self.lineEdit.setObjectName("lineEdit")

        #label error:
        self.label_error = QtWidgets.QLabel(self.centralWidget)
        self.label_error.setGeometry(QtCore.QRect(480, 150, 250, 17))
        self.label_error.setObjectName("label_error")
        self.label_error.setStyleSheet("color: rgb(255, 0, 0);")

        #label displayCount - this label displays the count of items in list
        self.label_DisplayCount = QtWidgets.QLabel(self.centralWidget)
        self.label_DisplayCount.setGeometry(QtCore.QRect(20, 362, 300, 17))
        self.label_DisplayCount.setObjectName("label_DisplayCount")
        self.label_DisplayCount.setStyleSheet("color: blue;")

        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(130, 410, 181, 17))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 665, 25))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "LIST MANAGEMENT APP"))
        self.listWidget.setSortingEnabled(False)
        self.buttonDelete.setText(_translate("MainWindow", "DELETE"))
        self.buttonAdd.setText(_translate("MainWindow", "ADD TO LIST"))
        self.label_2.setText(_translate("MainWindow", "ENTER ITEMS INTO LIST"))
        self.label_error.setText(_translate("MainWindow", ""))
        self.label_DisplayCount.setText(_translate("MainWindow", "There are currently 0 items in the list"))
        self.buttonAdd.clicked.connect(self.addList)
        self.buttonDelete.clicked.connect(self.delItem)
        #initialize the count variable 
        self.count = 0

    def delItem(self):
        self.label_error.setText("")
        # check to see if the user has selected an item, if not display an error:
        row = self.listWidget.currentRow()

        if(row != -1):
            self.listWidget.takeItem(self.listWidget.currentRow())
            self.count = self.count -1
            self.updateCount()
        else:
            #else if row is not found:: set an error
            self.label_error.setText("Error, Select an item before deleting!")

    def addList(self):
        self.listWidget.addItem(self.lineEdit.text())
        self.lineEdit.setText('')
        self.lineEdit.setFocus()
        self.label_error.setText("")
        self.count = self.count +1
        self.updateCount()

    #this method is called by the addList() and delItem(), and returns the label that displays the count
    def updateCount(self):
        count = str(self.count)
        self.label_DisplayCount.setText("There are currently "+ count + " items in the list.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

