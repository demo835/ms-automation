import pyautogui
import time
from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    {keyboard.Key.alt_l, keyboard.KeyCode(char='a')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='A')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='f')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='F')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='d')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='D')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='q')},
    {keyboard.Key.alt_l, keyboard.KeyCode(char='Q')}
]

# The currently active modifiers
current = set()

# def init():

def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute(current)

def execute(current):
    # print("Combo is ", current)
    for c in current:
        # print("Pressed ", c)
        # c == keyboard.Key.alt_l and 
        if c == keyboard.KeyCode(char='f'):
            print("f is pressed")
        if c == keyboard.KeyCode(char='q'):
            exit()
        if c == keyboard.KeyCode(char='d'):
            print("d is pressed")
    # autoGUI()

def on_release(key):
    # if key == keyboard.Key.shift:
    #     print("4th if works")
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

def autoGUI():

    width, height = pyautogui.size()
    print('Width is ', width, ' and Height is ', height)

    time.sleep(5)

    pyautogui.moveTo(200, 50)

    pyautogui.click(clicks=3, button='left')

    # Open Data Objects
    pyautogui.typewrite('https://ncua1.cloud.metricstream.com/ui/report/AppStudio-Data Objects')
    pyautogui.press('enter')

    # Open Infolets
    # pyautogui.typewrite('https://ncua1.cloud.metricstream.com/ui/admin/infolets')
    # pyautogui.press('enter')

    # # Open Forms
    # pyautogui.typewrite('https://ncua1.cloud.metricstream.com/ui/upgrade/forms')
    # pyautogui.press('enter')

# if __name__ == "__main__":
#     init()

# id = "settings"
# id = "Configurations"
# https://ncua1.cloud.metricstream.com/ui/report/AppStudio-Data Objects
# pyautogui.typewrite('\t')
# print(pyautogui.getAllWindows())

# ul, div, div, div, id=Configurations, ul, li

# time.sleep(2)
# for a in range(8):
#     pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')

# pyautogui.typewrite('\n')

# for b in range(4):
#     pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')
# pyautogui.typewrite('\t')

# pyautogui.typewrite('\n')

# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# pyautogui.typewrite('tab')
# # Move down to keep Settings menu open
# pyautogui.moveTo(1200, 215)

# # Move to Configuration button
# pyautogui.moveTo(650, 215)
# pyautogui.click(610, 215, button='left')
# pyautogui.moveTo(700, 215)

# pyautogui.moveTo(1100, 100, duration=1.25)
# pyautogui.moveTo(1200, 100, duration=1.25)
# pyautogui.moveTo(1300, 100, duration=1.25)

#document.getElementById("settings").getElementsByTagName("ul")[5].getElementsByTagName("li")[0]
