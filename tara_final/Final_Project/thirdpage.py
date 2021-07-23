import sys
import os
import cv2
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog
import numpy as np
import random

Form= uic.loadUiType(os.path.join(os.getcwd(),'thirdpage.ui'))[0]

class thirdpage(QMainWindow,Form):
    def __init__(self,parent,ProjDir):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent=parent
        self.ProjDir=ProjDir
        #pixmap = QPixmap(openfile)

        #events
        
        self.doneButton.clicked.connect(self.done)
        self.blurpushButton.clicked.connect(self.blurfunc)
        self.cropedpushButton.clicked.connect(self.cropfunc)
        self.rotationpushButton.clicked.connect(self.rotatefunc)
        self.flippushButton.clicked.connect(self.flipfunc)
        self.filterpushButton.clicked.connect(self.filter)

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

    def filter(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            img = cv2.imread(os.path.join(Path,file),cv2.IMREAD_UNCHANGED)
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv
            for x in range(0, len(hsv)):
                for y in range(0, len(hsv[0])):
                    hsv[x, y][2] += 80
            image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)    
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", image)   

    def blurfunc(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            img = cv2.imread(os.path.join(Path,file),cv2.IMREAD_UNCHANGED)
            blurred = cv2.blur(img,(5,5))
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", blurred)
    
    def cropfunc(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            img = cv2.imread(os.path.join(Path,file),cv2.IMREAD_UNCHANGED)
            cropped = img[200:500 , 200:500]
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", cropped)

    def rotatefunc(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            img = cv2.imread(os.path.join(Path,file),cv2.IMREAD_UNCHANGED)
            (h, w) = img.shape[:2]
            center = (w / 2, h / 2)

            #random rotation 0-360
            n = random.randint(0,360)

            M = cv2.getRotationMatrix2D(center, n, 1.0)
            rotated = cv2.warpAffine(img, M, (w, h))
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", rotated)

    def flipfunc(self):
        Path="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Dataset"
        Path1="F:/term 8/advanced_programing/FINAL/tara_final/Final_Project//"+self.ProjDir+"//Processed//"
        for file in os.listdir(Path):
            img = cv2.imread(os.path.join(Path,file), cv2.IMREAD_UNCHANGED)
            #random filp(vertically and horizentally)
            t= random.randint(-1,1)

            img_flip_lr = cv2.flip(img, t)
            n=random.randint(0,10000)
            cv2.imwrite(Path1 + f"{n}" + ".jpg", img_flip_lr)


    # def Nextfunc(self):
    # # if FirstPage.flag:
    # #     directory=self.ProjName.text()
    # #     Path=os.path.join("F:/Image_Processing/",directory)
    # #     if os.path.exists(Path):
    # #         self.statusbar.showMessage("Error: A directory with the same name exists.",6000)
    # #     else:
    # #         os.mkdir(Path)
    # #         FirstPage.ProjDir=Path
    # #         self.statusbar.showMessage("New directory created: '" + Path + "'")
            
    #     self.w2=SecondPage(self)
    #     self.w2.show()
    #     self.hide()

    # def PrevShow(self):
    #     self.parent.show()
    #     self.hide()
