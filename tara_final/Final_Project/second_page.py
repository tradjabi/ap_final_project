import sys
import os
import cv2
import random
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog
from thirdpage import thirdpage
from fourthpage import fourthpage

Form= uic.loadUiType(os.path.join(os.getcwd(),'Pg2.ui'))[0]

class SecondPage(QMainWindow,Form):
    def __init__(self,parent,ProjDir):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent=parent
        self.ProjDir=ProjDir
        content_widget = QWidget()
        self.ScrollArea.setWidget(content_widget)
        self._lay =QVBoxLayout(content_widget)

        #events
        self.SelectFile.clicked.connect(self.SelFile)
        self.SelectFolder.clicked.connect(self.SelFolder)
        self.BackButton.clicked.connect(self.PrevShow)
        self.AugmentationB.clicked.connect(self.Aug)
        self.PreprocessingB.clicked.connect(self.Preprop)

    def Aug(self):
        self.w3=thirdpage(self,self.ProjDir)
        self.w3.show()

    def Preprop(self):
        self.w4=fourthpage(self,self.ProjDir)
        self.w4.show()

    def PrevShow(self):
        self.parent.show()
        self.hide()    

    def SelFile(self):
        # root = Tk()
        # root.withdraw()
        # root.attributes('-topmost', True) 
        # open_file = filedialog.askdirectory() 
        # print(open_file) 

        root = Tk()
        root.withdraw()
        tempdir = filedialog.askopenfilename()
        if bool(tempdir):
            img = cv2.imread(tempdir, cv2.IMREAD_UNCHANGED)    
            scale_percent = 100*(100/img.shape[1])
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            n = random.randint(0,500)
            cv2.imwrite("F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+ f"modified//{n}.jpg", resized)
            cv2.imwrite("F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+ f"//Dataset//{n}.jpg", resized)
            new_file="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//modified"
            for file in os.listdir(new_file):
                pixmap = QPixmap(os.path.join(new_file, file))
                if not pixmap.isNull():
                    label =QLabel(pixmap=pixmap)
                    self._lay.addWidget(label)
            for f in os.listdir(new_file):
                os.remove(os.path.join(new_file,f))


    def SelFolder(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True) 
        open_file = filedialog.askdirectory() 
        
        # open_file = r"C:\Users\user\opencv-image-preprocessing-master\images\output"
        # list_of_images = os.listdir(open_file)
        # list_of_images = sorted(list_of_images)
        i=0
        if bool(open_file):
            for file in os.listdir(open_file):
                i+=1           
                img = cv2.imread(os.path.join(open_file, file), cv2.IMREAD_UNCHANGED)    
                scale_percent = 100*(100/img.shape[1])
                width = int(img.shape[1] * scale_percent / 100)
                height = int(img.shape[0] * scale_percent / 100)
                dim = (width, height)
                resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
                cv2.imwrite("F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+ f"//modified//{i}.jpg", resized)
                cv2.imwrite("F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+ "//Dataset//%s"% file, resized)
            new_file="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//modified"
            for file in os.listdir(new_file):
                pixmap = QPixmap(os.path.join(new_file, file))
                if not pixmap.isNull():
                    label =QLabel(pixmap=pixmap)
                    self._lay.addWidget(label)
            for f in os.listdir(new_file):
                os.remove(os.path.join(new_file,f))     






        # root = Tk() 
        # root.withdraw()
        # root.attributes('-topmost', True)
        # open_file = filedialog.askdirectory() 
        # list_of_images = os.listdir(open_file)
        # list_of_images = sorted(list_of_images)
        # pixmap=QPixmap(os.path.join(open_file,list_of_images[2]))
        # self.ImageLabel.setPixmap(pixmap)
        # self.ImageLabel.pixmap.save()
        
        # self.ImageLabel.setMask(list_of_images.mask())
        # self.ImageLabel.show()
