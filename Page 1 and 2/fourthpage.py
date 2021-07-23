import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog
from second_page import SecondPage


Form= uic.loadUiType(os.path.join(os.getcwd(),'fourthpage.ui'))[0]

class fourthpage(QMainWindow,Form):
    def __init__(self,parent):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent=parent
        # pixmap = QPixmap(openfile)

        #events
        
        self.back4.clicked.connect(self.PrevShow)
        # self.next4.clicked.connect(self.Nextfunc)

        # def Nextfunc(self):
        # if FirstPage.flag:
        #     directory=self.ProjName.text()
        #     Path=os.path.join("F:/Image_Processing/",directory)
        #     if os.path.exists(Path):
        #         self.statusbar.showMessage("Error: A directory with the same name exists.",6000)
        #     else:
        #         os.mkdir(Path)
        #         FirstPage.ProjDir=Path
        #         self.statusbar.showMessage("New directory created: '" + Path + "'")
                
        # self.w2=SecondPage(self)
        # self.w2.show()
        # self.hide()

        def PrevShow(self):
        self.parent.show()
        self.hide()
