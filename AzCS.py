import pyautogui
import numpy as nm
import numpy as nm
import pytesseract
import pytesseract
import cv2
from PIL import ImageGrab
import time
import clipboard

def work():
    pass

if __name__ == '__main__':

    #pyautogui.click(972, 1050)
    #pyautogui.click(221, 52)

    #pyautogui.hotkey('ctrl', 'c')

    #link = clipboard.paste()

    #print(link)

    domain = "https://www.amazon.in/dp/"
    stringend = "/ref=sr_1_3?crid=SCG952C2DPZ0&keywords=tv&qid=1642942576&sprefix=t%2Caps%2C220&sr=8-3&th=1"
    asin = "B08D11DZ2W"

    newlink = domain + asin + stringend;

    pyautogui.click(972, 1050)
    pyautogui.click(221, 52)

    pyautogui.write(newlink)
    pyautogui.press('enter')    
