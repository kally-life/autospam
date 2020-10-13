import pyautogui
import time
import ctypes
from time import sleep
from pynput.keyboard import *

delay = 0.3
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc

pause = True
running = True

def on_press(key):
    global running, pause
    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def main():
    lis = Listener(on_press=on_press)
    lis.start()
    while running:
        if not pause:
            f = open("spam.txt", 'r')
            for word in f:
                pyautogui.typewrite(word)
                pyautogui.press("enter")
                pyautogui.PAUSE = delay
        else:
            sleep(delay)
    lis.stop()

if __name__ == "__main__":
    main()
