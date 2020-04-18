from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
        self.setGeometry(2000,200,500,500)
        self.setWindowTitle("Assignment 4 Python")

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label")
        self.label.move(50,50)

        self.lineText = QtWidgets.QLineEdit(self)
        # self.label.setText("my first label")
        self.lineText.move(200,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("HELLO")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        #get value of lineText :
        value = self.lineText.text()
        self.label.setText(str(value));
        #print(value)
        
        #self.label.setText("You pressed the button broski")
        self.update()

        

    def update(self):
        self.label.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())
window()