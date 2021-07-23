import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog
from second_page import SecondPage

Form= uic.loadUiType(os.path.join(os.getcwd(),'Pg1.ui'))[0]

class FirstPage(QMainWindow,Form):
    ProjDir=0
    def __init__(self):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        #events    
        self.CancelButton.clicked.connect(self.Cancelfunc)
        self.FindButton.clicked.connect(self.Openfunc)
        self.NextButton.clicked.connect(self.Nextfunc)
    def Nextfunc(self):
        directory=self.ProjName.text()
        FirstPage.ProjDir=directory
        Path=os.path.join(r"F:/term 8/advanced_programing/FINAL/tara_final/Final_Project",directory)
        if os.path.exists(Path) or not bool(directory):
            self.statusbar.showMessage("Error: A directory with the same name exists or no name entered.",6000)
        else:
            os.mkdir(Path)
            os.mkdir(os.path.join(Path,"modified"))
            os.mkdir(os.path.join(Path,"Dataset"))
            os.mkdir(os.path.join(Path,"Processed"))
            self.statusbar.showMessage("New directory created: '" + Path + "'")
        self.w2=SecondPage(self,FirstPage.ProjDir)
        self.w2.show()
        self.hide()
    def Openfunc(self):
        root = Tk()
        root.withdraw() 
        root.attributes('-topmost', True) 
        open_file = filedialog.askdirectory() 
        if open_file!="":
            print(open_file) 
            self.statusbar.showMessage("Directory '" + open_file + "' is chosen.")
            # self.NewProjBox.setEnabled(False)     
    def Cancelfunc(self):
        self.close()

if __name__=="__main__":
    app=QApplication(sys.argv)      
    w=FirstPage()
    w.show()
    sys.exit(app.exec_())
