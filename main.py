import cv2
import cv2 as cv
import easygui
import numpy as np
import imageio
import sys
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image


def cartoonify(ImagePath):
    ogimage = cv.imread(ImagePath)
    ogimage = cv.cvtColor(ogimage, cv.COLOR_BGR2RGB)
    if ogimage is None:
        print("Please choose a correct formt")
        sys.exit()
    resized = cv.resize(ogimage, (960, 540))
    grayScaleImage = cv.cvtColor(ogimage, cv.COLOR_BGR2GRAY)
    Resized2 = cv.resize(grayScaleImage, (960, 540))
    smoothing = cv.medianBlur(grayScaleImage, 5)
    Resized3 = cv.resize(smoothing, (960, 540))
    getEdge = cv.adaptiveThreshold(smoothing, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    Resized4 = cv.resize(getEdge, (960, 540))
    colorimg = cv.bilateralFilter(ogimage, 9, 300, 300)
    Resized5 = cv.resize(smoothing, (960, 540))
    cartoonimg = cv.bitwise_and(colorimg, colorimg, mask=getEdge)
    Resized6 = cv.resize(cartoonimg, (960, 540))
    images = [resized, Resized2, Resized2, Resized4, Resized5, Resized6]
    fig, axes = plt.subplots(3, 2, figsize=(8, 8), subplot_kw={'xticks': [], 'yticks': []},
                             gridspec_kw=dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(images[i], cmap='gray')
    plt.show()

    def save(Resized6, ImagePath):
        newName = 'cartoonfifiedImage'
        path1 = os.path.dirname(ImagePath)

    extensions = os.path.splittext(ImagePath)
    path = os.path.splittext(ImagePath)
    path = os.path.join(path1, newName + extensions)
    cv2.imwrite(path, cv2.cvtColor(Resized6, cv2.COLOR_RGB2BGR))
    I = "Image saved by name " + newName + " at " + path
    tk.messagebox.showinfo(title=None, message=I)


def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)
top=tk.Tk()
top.geometry('400x400')
top.title('Cartoonify Your Image !')
top.configure(background='white')
label=Label(top,background='#CDCDCD', font=('calibri',20,'bold'))
upload=Button(top,text="Cartoonify an Image",command=upload,padx=10,pady=5)
upload.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
upload.pack(side=TOP,pady=50)
save1=Button(top,text="Save cartoon image",command=lambda: save(ImagePath, ReSized6),padx=30,pady=5)
save1.configure(background='#364156', foreground='white',font=('calibri',10,'bold'))
save1.pack(side=TOP,pady=50)
top.mainloop()
