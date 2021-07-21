import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

Form = uic.loadUiType(os.path.join(os.getcwd(),"first_window.ui"))[0]


class IntroWindow(QMainWindow,Form):
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        #event
        self.nextButton.clicked.connect(self.next_callback)
        self.enterPNButton.clicked.connect(self.enterPN_callback)
        # self.enterSPButton.clicked.connect(self.enterSN_callback)

        

    def next_callback():
        print("welcome to seconde page...")

    def enterPN_callback(self):
        projectName = self.lineEditProjectname.text()
        print(projectName)
        print(" you have enterd project name")

    # def enterSN_callback(self):
    #     projactType = self.lineEditProjectType.text()
    #     print(projactType)
    #     print(" you have enterd project type")


if __name__ =="__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    

    w = IntroWindow()
    


    w.show()

    app.exec_()