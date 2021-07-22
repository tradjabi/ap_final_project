import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from tkinter import Tk, filedialog
from PIL.ImageQt import ImageQt
from PyQt5.QtGui import QPixmap

Form= uic.loadUiType(os.path.join(os.getcwd(),'Pg2.ui'))[0]



class SecondPage(QMainWindow,Form):
    def __init__(self,parent):
        Form.__init__(self)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.parent=parent
        # pixmap = QPixmap(openfile)

        #events
        self.SelectFile.clicked.connect(self.SelFile)
        self.SelectFolder.clicked.connect(self.SelFolder)
        self.BackButton.clicked.connect(self.PrevShow)

    def PrevShow(self):
        self.parent.show()
        self.hide()    

    def SelFolder(self):
        root = Tk()
        root.withdraw()
        root.attributes('-topmost', True) 
        open_file = filedialog.askdirectory() 
        
        list_of_images = os.listdir(open_file)
        list_of_images = sorted(list_of_images)
        # pixmap=QPixmap(os.path.join(open_file,list_of_images[2]))
        # self.ImageLabel.setPixmap(pixmap)
        print(list_of_images[2])

        
        # for index, value in enumerate(list_of_images):
        #     list_of_images[index] = open_file + value


        # pixmap=list_of_images[0]
        # self.ImageLabel.setPixmap(list_of_images[0])
        # self.ImageLabel.setMask(list_of_images.mask())
        # self.ImageLabel.show()
        # Length of Images
        # print('Number of Images in the selected folder: {}'.format(len(self.list_of_images)))
        # # labeling

        # self.label.setPixmap(QtGui.QPixmap(input_img_raw_string))
        # self.label.show()
    
    ##show them all in a list
    # def next_button_callback(self):
        
    #     # Total Images in List
    #     total_images = len(self.list_of_images)

    #     if self.list_of_images:
    #         try:
    #             for img in self.list_of_images:
    #                 self.label.setPixmap(QtGui.QPixmap('{}\\{}'.format(self._images_dir, img)))
    #                 self.label.show()
                    
    #         except ValueError as e:
    #             print('The selected folder does not contain any images')


        print(open_file)

    def SelFile(self):
        root = Tk() 
        root.withdraw()
        root.attributes('-topmost', True)
        open_file = filedialog.askdirectory() 
        
        ImageFile = QPixmap("./test.jpg")
        ImageLable = QLabel()
        ImageLable.setPixmap(ImageFile)

        self.grid = QGridLayout()
        self.grid.addWidget(ImageLable,1,1)
        self.setLayout(self.grid)

        self.setGeometry(50,50,320,200)
        self.setWindowTitle("PyQT show image")
        self.show()

        print(open_file)
