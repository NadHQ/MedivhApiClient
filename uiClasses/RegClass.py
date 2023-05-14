import typing
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtCore import QUrl
from UI_code.registration import Ui_MainWindow

class RegWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(800,600)

        self.ui.enterButton.clicked.connect(self.sendRegData)
    
    def getReply(self,reply):
        data = reply.readAll()
        response = bytes(data).decode('utf-8')
        print(response)


    def sendRegData(self):

        manager = QNetworkAccessManager()
        manager.finished.connect(self.getReply)
        url = QUrl('localhost:8000/api/v1/registration')
        request = QNetworkRequest(url=url, )
        request.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, value='application/json')

        data = {
            "username" : self.ui.login.text,
            "password" : self.ui.password.text,
            "licence" : self.ui.licence.text
        }

        manager.post(request, data=str(data).encode('utf-8'))
