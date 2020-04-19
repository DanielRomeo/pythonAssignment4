# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1071, 711)

      

        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(60, 70, 391, 491))

        #grid layout
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(15, 11, 15, 11)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName("gridLayout")

        #line edits
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 7, 0, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 6, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 10, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 4, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 8, 0, 1, 1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.gridLayout.addWidget(self.lineEdit_1, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 9, 0, 1, 1)

        #labels
        font = QtGui.QFont()
        font.setPointSize(22)

        #my details:
        self.labelName = QtWidgets.QLabel(self.centralWidget)
        self.labelName.setText("DANIEL MAMPHEKGO : 69044880")
        self.labelName.setGeometry(QtCore.QRect(500, 600, 600, 30))
        self.labelName.setFont(font)
        #end of details

        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 401, 51))
        
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralWidget)
        self.listWidget.setGeometry(QtCore.QRect(540, 70, 256, 256))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1071, 25))
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
        self.pushButton.setText(_translate("MainWindow", "Add to List and Sort"))
        self.pushButton.clicked.connect(self.clicked)
        self.label.setText(_translate("MainWindow", "Enter 10 Olympic sport names"))
        self.listWidget.setSortingEnabled(False)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        self.listWidget.setSortingEnabled(__sortingEnabled)

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("tuoria")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Retry)
        msg.setDefaultButton(QMessageBox.Retry)
        msg.setInformativeText("Error, Do not enter duplicate sport names") 

        x = msg.exec_()       

    #runs when button1 is clicked    
    def clicked(self):


        #create a list dataType and add data from lineEdits into it
        # useing .capitalize after each append to capitalize each first Letter
        mylist = [];
        mylist.append(self.lineEdit_1.text().capitalize())
        mylist.append(self.lineEdit_2.text().capitalize())
        mylist.append(self.lineEdit_3.text().capitalize())
        mylist.append(self.lineEdit_4.text().capitalize())
        mylist.append(self.lineEdit_5.text().capitalize())
        mylist.append(self.lineEdit_6.text().capitalize())
        mylist.append(self.lineEdit_7.text().capitalize())
        mylist.append(self.lineEdit_8.text().capitalize())
        mylist.append(self.lineEdit_9.text().capitalize())
        mylist.append(self.lineEdit_10.text().capitalize())

        #sort the list
        mylist.sort();


        ''' 
            this next section of code is concerned with the checking for duplicates and returning errors upon finding them: 
            - first copy list 1 into list 2
            - then loop through both arrays and find the duplicate
        
        '''
        mylist2 = []
        mylist2 = mylist.copy()
        for i in range(len(mylist)):
            del mylist2[0]

            if(mylist[i] in mylist2):
                #DISPLAY POPUP ERROR MESSAGE
                self.show_popup()
                exit()
            else:
                continue    
        ''' end of algorithm '''



        #check if duplicates have been entered in the list:
        for i in range(len(mylist)):
            continue;


        #now i loop through mylist and push the items to the listPanel: 
        for i in range(10):
            self.listWidget.addItem(mylist[i])

        #print(mylist)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

