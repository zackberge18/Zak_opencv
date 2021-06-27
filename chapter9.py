import cv2
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt

import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image

def upload():
    ImagePath=easygui.fileopenbox()
    cartoonify(ImagePath)


def cartoonify(ImagePath):
    #read the image
    img=cv2.imread(ImagePath)
    img1=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)


    imgGray=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    imgBlur=cv2.medianBlur(imgGray,5)
    getEdge = cv2.adaptiveThreshold(imgBlur, 255,
                                    cv2.ADAPTIVE_THRESH_MEAN_C,
                                    cv2.THRESH_BINARY, 9, 9)

    cv2.imshow("result", getEdge)
    cv2.waitKey(0)
upload()