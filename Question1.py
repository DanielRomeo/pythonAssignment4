from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.setGeometry(2000,200,800,500)
        self.setWindowTitle("Assignment 4 Python")

    def initUI(self):

        #essentials:
        font = QtGui.QFont()
        font.setPointSize(55)


        #UI DISPLAY MY INFORMATION:
        self.labelName = QtWidgets.QLabel(self)
        self.labelName.setText("DANIEL MAMPHEKGO : 69044880")
        self.labelName.setGeometry(500,470, 600, 30)

        #label1 component:
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Enter Olympic sport")
        self.label.setGeometry(50,50, 400, 25)

        #labe2 component:
        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Enter single Charector")
        self.label2.setGeometry(50, 100, 400,25) 


        #Display Label
        self.labelDisplay = QtWidgets.QLabel(self)
        self.labelDisplay.setText("0")
        self.labelDisplay.setGeometry(250, 200, 150,100) 
        self.labelDisplay.setFont(font)
        # =======================================================

        #linetext1
        self.lineText = QtWidgets.QLineEdit(self)
        self.lineText.setGeometry(250,50, 400, 25)

        #linetText2
        self.lineText2 = QtWidgets.QLineEdit(self)
        self.lineText2.setGeometry(250,100, 400, 25)

        # =======================================================
        
        #display button
        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Count")
        self.b1.clicked.connect(self.clicked)
        self.b1.setGeometry(250,150, 250, 25)

    #runs when button1 is clicked    
    def clicked(self):
        #get value of label1 and label2 and count chars:
        olympicSportName = self.lineText.text()
        charector = self.lineText2.text()

        #convert the input to lowercase:
        olympicSportName =  olympicSportName.lower();
        charector = charector.lower();

        #initialize the count:
        count = 0

        #loop through the string and increment count
        for i in range(len(olympicSportName)):
            if charector == olympicSportName[i]:
                count = count + 1
                #print(str(charector))
            self.labelDisplay.setText(str(count))    
        self.update()

        

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()