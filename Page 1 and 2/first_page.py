import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog
from second_page import SecondPage


Form= uic.loadUiType(os.path.join(os.getcwd(),'test.ui'))[0]

class FirstPage(QMainWindow,Form):
    ProjDir=0
    flag=True
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)

        #events
        
        self.CancelButton.clicked.connect(self.Cancelfunc)
        self.FindButton.clicked.connect(self.Openfunc)
        self.NextButton.clicked.connect(self.Nextfunc)
    def Nextfunc(self):
        if FirstPage.flag:
            directory=self.ProjName.text()
            Path=os.path.join("F:/Image_Processing/",directory)
            if os.path.exists(Path):
                self.statusbar.showMessage("Error: A directory with the same name exists.",6000)
            else:
                os.mkdir(Path)
                FirstPage.ProjDir=Path
                self.statusbar.showMessage("New directory created: '" + Path + "'")
        self.w2=SecondPage(self)
        self.w2.show()
        self.hide()
    def Openfunc(self):
        root = Tk() # pointing root to Tk() to use it as Tk() in program.
        root.withdraw() # Hides small tkinter window.
        root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
        open_file = filedialog.askdirectory() # Returns opened path as str
        if open_file!="":
            print(open_file) 
            FirstPage.ProjDir=open_file
            self.statusbar.showMessage("Directory '" + open_file + "' opened.")
            self.NewProjBox.setEnabled(False)
            FirstPage.flag=False      
    def Cancelfunc(self):
        self.close()

if __name__=="__main__":
    app=QApplication(sys.argv)      
    w=FirstPage()
    w.show()
    sys.exit(app.exec_())
