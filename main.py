from detectEvents import *
from automation import *
import time
import tkinter as tk
from tkinter import simpledialog
import configparser
import os
import PySimpleGUI as sg



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

pauseButton = parser.get('config', 'pause')
print("Pause with: " +pauseButton)
pause = retrieveCode(pauseButton)


goOnButton = parser.get('config', 'goOn')
print("GoOn with: " +goOnButton)
goOn = retrieveCode(goOnButton)

pasteButton = parser.get('config', 'paste')
print("Paste with: " +pasteButton)
paste = retrieveCode(pasteButton)

stopRecButton = parser.get('config', 'stopRec')
print("Stop Recording with: " +stopRecButton)
stopRec = retrieveCode(stopRecButton)

separator = parser.get('config', 'separator')
print("Separator for multi-paste: "+separator)

def automation():
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
                    print (pressed,x,y,text)
            else:
                actionArray.append((pressed,x,y,text))
                r = r + 1
                print (pressed,x,y,text) 
        #timesleep very low, because a click is very fast and we need to detect it
        time.sleep(0.01)
    #print (*actionArray , sep = "\n")

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
                    automate(pressed,x,y,text[j%len(text)])
            else:
                automate(pressed,x,y,text)
            time.sleep(float(seconds))





if __name__ == '__main__':

    #############
    #GUI Opening#
    #############
    layout = [[sg.Text("Pause with: "+pauseButton)],
                [sg.Text("Continue with: "+goOnButton)],
                [sg.Text("Paste with CTRL + V or : "+pasteButton)],
                [sg.Text("Stop Recording with: "+stopRecButton)],
                [sg.Text("Separator for multi-paste will be: "+separator)],
                [sg.Button("Start Recording")]]
    #create the window
    window = sg.Window("Automation",layout)
    while True:
        event,values = window.read()
        if event == "Start Recording":
            window.close()
            automation()
            break
                        
        if event == sg.WIN_CLOSED:
            window.close()
            break   