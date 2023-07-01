
""" 
my camera application
author Sabbir Islam 

"""

import sys
from PyQt5.QtWidgets import*
from PyQt5.QtGui import QPixmap, QImage, QIcon
import cv2

class window(QWidget):
    """"Mine app window"""
    def __init__(self):
        super().__init__()
    
        # Variables for Window
        self.window_width = 640
        self.window_height = 400

        # Setup the window
        self.setWindowTitle("My camera application")
        self.setFixedSize(self.window_width, self.window_height)



    def ui(self):
        """""Contains all ui things"""
        pass

    def update(self):
        """"Updates frame"""
        pass

    def save_img(self):
        """"Save image from camera"""
        pass

    def record(self):
        """"record video"""
    
