import pyautogui as mouse


def up():
    mouse.click(1739, 769)
    return "UP"


def down():
    mouse.click(1739, 906)
    return "DOWN"


def left():
    mouse.click(1666, 841)
    return "LEFT"


def right():
    mouse.click(1822, 849)
    return "RIGHT"
