from detectEvents import *
from automation import *
import time
import tkinter as tk
from tkinter import simpledialog
import configparser
import os



#file configuration retrieve dimension cmd window

length = parser.get("config", "length")
width = parser.get("config", "width")

os.system("mode con cols="+str(width) +"lines=" +str(length))

#file configuration retrieve
parser = configparser.ConfigParser()
parser.read("config.txt")
seconds = parser.get("config", "seconds")

parser = configparser.ConfigParser()
parser.read('config.txt')

pause = parser.get('config', 'pause')
print("Pause with: " +pause)
pause = retrieveCode(pause)


goOn = parser.get('config', 'goOn')
print("GoOn with: " +goOn)
goOn = retrieveCode(goOn)

paste = parser.get('config', 'paste')
print("Paste with: " +paste)
paste = retrieveCode(paste)

stopRec = parser.get('config', 'stopRec')
print("Stop Recording with: " +stopRec)
stopRec = retrieveCode(stopRec)

separator = parser.get('config', 'separator')
print("Separator for multi-paste: "+separator)

if __name__ == '__main__':
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
        #print(pressed,x,y,text)
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
            if type(text) is list:
                #check that len of text is greater than iteration. If not begin from start.
                if len(text) > j:
                    automate(pressed,x,y,text[j])
                else:
                    automate(pressed,x,y,text[j%len(text)])
            else:
                automate(pressed,x,y,text)
            time.sleep(float(seconds))