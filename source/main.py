# Created By VictorTheDuck https://youtube.com/c/victortheduck

from time import sleep
import pyautogui 
import pydirectinput 
import random

print('starting')

total_made = 0

while True:
    sleep(10)
    pydirectinput.press('space')

    map_title = pyautogui.locateCenterOnScreen('map_title.jpg', confidence=.9)
    if map_title != None:
        total_made += 50000
        print('starting new map, total made so far is ' + str(total_made))
        pydirectinput.press('up')
        pydirectinput.press('enter')
        sleep(2)
        pydirectinput.press('up')
        pydirectinput.press('enter')
        sleep(.3)
        pydirectinput.press('enter')
        

