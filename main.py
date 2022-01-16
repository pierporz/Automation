from detectEvents import *
from automation import *
import time
import tkinter as tk
from tkinter import simpledialog
import configparser
#import pkg_resources.py2_warn


if __name__ == '__main__':

    #file configuration retrieve
    parser = configparser.ConfigParser()
    parser.read("config.txt")
    seconds = parser.get("config", "seconds")

    #variables initialization
    pressed = 0
    x = 0
    y = 0
    text =""
    r = 0
    actionArray = []

    ###########
    #Recording#
    ###########
    while (pressed != "stopRec"):
        pressed,x,y,text = detectPressOrClick()
        if pressed == "pause":
            while (pressed != "goOn"):
                pressed,x,y,text = detectPressOrClick()
        print(pressed,x,y,text)
        if (pressed,x,y,text) != (0, 0, 0, "") and  pressed != "stopRec" and pressed != "pause" and pressed != "goOn":
            time.sleep(0.2)
            if r != 0:
                if (pressed,x,y,text) != actionArray[r-1]:
                    actionArray.append((pressed,x,y,text))
                    r = r + 1
            else:
                actionArray.append((pressed,x,y,text))
                r = r + 1 
        #timesleep very low, because a click is very fast and we need to detect it
        time.sleep(0.01)
    print (*actionArray , sep = "\n")

    ############
    #Automation#
    ############
    root = tk.Tk()
    root.withdraw()
    loop = simpledialog.askstring("input", "how many times?")
    for j in range(int(loop)):
        for i in range(len(actionArray)):
            (pressed,x,y,text)=actionArray[i]
            automate(pressed,x,y,text)
            time.sleep(float(seconds))