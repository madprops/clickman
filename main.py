import sys
import time
import pyautogui


def sleep(t):
    time.sleep(t)


def click(x, y, button="left"):
    pyautogui.moveTo(x, y)
    sleep(0.5)
    pyautogui.click(button=button)


def write(text):
    pyautogui.typewrite(text)


def press(key):
    pyautogui.press(key)


def ctrl(key):
    pyautogui.hotkey("ctrl", key)


def gh_edge():
    click(2, 242)
    sleep(0.5)


def gh_cmd():
    press("ctrl")
    sleep(0.1)
    press("ctrl")
    sleep(0.5)


def grasshopper_1():
    gh_edge()
    ctrl("3")
    sleep(0.5)

    # Remove debug extension
    click(1309, 602)
    sleep(0.5)

    # Right click extension icon
    click(132, 51, "right")
    sleep(0.5)

    # Click manage
    click(210, 69)

    # Check for updates
    click(1338, 166)
    sleep(0.5)
    click(1374, 202)
    sleep(3)

    gh_edge()
    gh_cmd()

    # Apply settings
    write("madprops")
    sleep(0.5)
    press("enter")
    sleep(0.5)
    press("enter")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "grasshopper":
        grasshopper_1()