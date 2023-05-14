import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from UI_code import autorization
from .RegClass import RegWin
class AuthWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = autorization.Ui_AuthForm()
        self.ui.setupUi(self)
        self.setFixedSize(800,600)
        
        self.regUI = RegWin()
        self.ui.enterButton.clicked.connect(self.sendAuthData)
        self.ui.regButton.clicked.connect(self.openRegWin)
    
    def sendAuthData(self):
        print("test")

    def openRegWin(self):
        self.regUI.show()
