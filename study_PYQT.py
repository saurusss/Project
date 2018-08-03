# import sys
# from PyQt5.QtWidgets import *

# app = QApplication(sys.argv)
# label = QLabel("Hello, PyQt")
# label.show()

# print("Before event loop")
# app.exec_()
# print("After event loop")
#==================================
# import sys
# from PyQt5.QtWidgets import *

# def clicked_slot():
#     print('clicked')

# app = QApplication(sys.argv)

# btn = QPushButton("Hello, PyQt")
# btn.clicked.connect(clicked_slot)
# btn.show()

# app.exec_()

#==================================
# import sys
# from PyQt5.QtWidgets import *

# class MyWindow(QMainWindow):  # QMainWindow 상속 
#         super().__init__()
#         self.setupUI()
    
#     def setupUI(self):
#         self.setWindowTitle("Review")

#         btn1 = QPushButton("Click Me", self)
#         btn1.move(20, 20)
#         btn1.clicked.connect(self.btn1_clicked)

#     def btn1_clicked(self):
#         QMessageBox.about(self, "message", "CLICKED")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mywindow = MyWindow()
#     mywindow.show()
#     app.exec_()


#========================================
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# from_class = uic.loadUiType("main_window.ui")[0]

# class MyWindow(QMainWindow, from_class):
#         def __init__(self):
#             super().__init__()
#             self.setupUi(self)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

#========================================
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5 import uic

# from_class = uic.loadUiType("main_window.ui")[0]

# class MyWindow(QMainWindow, from_class):
#         def __init__(self):
#             super().__init__()
#             self.setupUi(self)
#             self.pushButton.clicked.connect(self.btn_clicked)
#         def btn_clicked(self):
#             QMessageBox.about(self, "message", "clicked")
            
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     myWindow = MyWindow()
#     myWindow.show()
#     app.exec_()

#========================================
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *

# class MyWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUI()

#     def setupUI(self):
#         btn1 = QPushButton("닫기", self)
#         btn1.move(20, 20)
#         btn1.clicked.connect(QCoreApplication.instance().quit)

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     mywindow = MyWindow()
#     mywindow.show()
#     app.exec_()

#========================================
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 400, 400, 150)

        textLabel = QLabel("Message: ", self)
        textLabel.move(20, 20)

        self.label = QLabel("", self)
        self.label.move(80, 20)
        self.label.resize(150, 30)

        btn1 = QPushButton("Click", self)
        btn1.move(20, 60)
        btn1.clicked.connect(self.btn1_clicked)

        btn2 = QPushButton("Clear", self)
        btn2.move(140, 60)
        btn2.clicked.connect(self.btn2_clicked)

    def btn1_clicked(self):
        self.label.setText("버튼이 클릭되었습니다.")

    def btn2_clicked(self):
        self.label.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()