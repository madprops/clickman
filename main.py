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


def gh_cmd(cmd, confirm=False):
    press("ctrl")
    sleep(0.1)
    press("ctrl")
    sleep(0.5)
    write(cmd)
    sleep(0.5)
    press("enter")
    sleep(0.5)

    if confirm:
        press("enter")


def grasshopper_1():
    # Focus edge
    gh_edge()

    # Focus 3rd tab
    ctrl("3")
    sleep(0.5)

    # Remove debug extension
    click(1315, 581)
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

    # Focus edge
    gh_edge()

    # Run command
    gh_cmd("madprops", True)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    arg = sys.argv[1]

    if arg == "grasshopper":
        grasshopper_1()