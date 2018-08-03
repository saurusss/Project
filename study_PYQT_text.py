import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 300, 150)

        # Label
        label = QLabel("종목코드", self)
        label.move(20, 20)

        # LineEdit
        self.lineEdit = QLineEdit("", self)
        self.lineEdit.move(80, 20)
        # self.lineEdit.textChanged.connect(self.lineEditChanged) # character 입력시 statusbar update
        self.lineEdit.returnPressed.connect(self.lineEditChanged) # return 입력시 statusbat update

        # StatusBar
        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def lineEditChanged(self):
        self.statusBar.showMessage(self.lineEdit.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()