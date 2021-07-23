import sys
import os
import cv2
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog


Form= uic.loadUiType(os.path.join(os.getcwd(),'fourthpage.ui'))[0]

class fourthpage(QMainWindow,Form):
    def __init__(self,parent,ProjDir):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent=parent
        self.ProjDir=ProjDir

        #events
        
        self.doneButton.clicked.connect(self.done)
        self.graypushButton.clicked.connect(self.grayfunc)
        self.resizepushButton.clicked.connect(self.resizefunc)

    def done(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset//"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed"
        for file in os.listdir(Path1):
            img = cv2.imread(os.path.join(Path1,file),cv2.IMREAD_UNCHANGED)
            n=random.randint(0,10000)
            cv2.imwrite(Path + f"{n}" + ".jpg", img)
        for f in os.listdir(Path1):
            os.remove(os.path.join(Path1,f))     
        self.close()    

    def grayfunc(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            im_gray = cv2.imread(os.path.join(Path,file), cv2.IMREAD_GRAYSCALE)
            (thresh, im_bw) = cv2.threshold(im_gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            thresh = 127
            im_bw = cv2.threshold(im_gray, thresh, 255, cv2.THRESH_BINARY)[1]
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", im_bw)

    def resizefunc(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            img = cv2.imread(os.path.join(Path,file), cv2.IMREAD_UNCHANGED)
            scale_percent = 100*(100/img.shape[1]) # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", resized)
