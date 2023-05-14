from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from uiClasses import AuthClass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = AuthClass.AuthWin()
    myapp.show()
    sys.exit(app.exec_())