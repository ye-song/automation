#! python3
# formfilling.py - formfilling on eventbrite

import pyautogui
import time

formData = [{'firstname':'placeholder', 'surname':'placeholder', 'email':'placeholder@gmail.com', 'mobile':'012345678'}]

pyautogui.PAUSE = 1


for person in formData:
    # Click 'register'
    coordinates = pyautogui.locateOnScreen('register.png', confidence = 0.8)
    center = pyautogui.center((coordinates))
    pyautogui.click((center))

    # Select '1 Church Family Ticket'
    time.sleep(2)
    pyautogui.typewrite('\t')
    time.sleep(1)
    pyautogui.typewrite(['down'])

    # Click 'register'
    time.sleep(1)
    coordinates = pyautogui.locateOnScreen('registerRed.png', confidence = 0.8)
    center = pyautogui.center((coordinates))
    pyautogui.click((center))

    # Fill in particulars
    time.sleep(2)
    pyautogui.typewrite('\t')
    pyautogui.typewrite(person['firstname'] + '\t')
    pyautogui.typewrite(person['surname'] + '\t')
    pyautogui.typewrite(person['email'] + '\t')
    pyautogui.typewrite(person['email'] + '\t')
    pyautogui.typewrite(person['firstname'] + '\t')
    pyautogui.typewrite(person['surname'] + '\t')
    pyautogui.typewrite(person['email'] + '\t')
    pyautogui.typewrite(person['mobile'] + '\t')
    pyautogui.typewrite(['down', '\t'])
    pyautogui.typewrite([' ', '\t', '\t'])
    pyautogui.typewrite(['\t',' '])

    # Click 'register'
    time.sleep(1)
    coordinates = pyautogui.locateOnScreen('registerRed.png', confidence = 0.8)
    center = pyautogui.center((coordinates))
    pyautogui.click((center))
