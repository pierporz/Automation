import pyautogui
import configparser

#file configuration retrieve
parser = configparser.ConfigParser()
parser.read("config.txt")
seconds = parser.get("config", "seconds")

def automate(pressed,x,y,text):
    if pressed == "paste":
        pyautogui.typewrite(text)
    if pressed == "Right Click":
        pyautogui.rightClick(x,y)
    if pressed == "Left Click":
        pyautogui.click(x,y)
    if pressed == "selectAll":
        pyautogui.hotkey('ctrl', 'a')
    if pressed == "backspace":
        pyautogui.press('backspace')
