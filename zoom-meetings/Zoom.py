#! python3
# Zoom.py - opens up zoom and login the meeting session.

import subprocess
import pyautogui
import time

'''
This is a sample code. To use this sample code:
1. Replace the path of zoom application on your machine
2. Replace the coordinates of where each mouse click will be
** Note that this depends on the screen resolution of your machine.
3. Replace the 'meeting ID' placeholder
4. Replace the 'password' placeholder

The times are added because pyautogui runs too fast before the 
GUI is loaded.
'''
subprocess.Popen('C:\\Users\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
time.sleep(1)
pyautogui.click((1300, 713))
time.sleep(1)
pyautogui.typewrite('meeting ID')
time.sleep(1)
pyautogui.click((1305, 908))
time.sleep(2)
pyautogui.typewrite('password')
time.sleep(1)
pyautogui.click((1295, 906))
