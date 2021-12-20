import cv2
import numpy as np
from PIL import ImageGrab


class Redungeon:
    def __init__(self, x=int, y=int, sizex=int, sizey=int, slicer=int, frames=int, debug=False):
        """
        :param x: The screen x-axis where the screenshot starts.
        :param y: The screen y-axis where the screenshot starts.
        :param sizex: Defines how long row will be.
        :param sizey: Defines how long a column will be.
        :param slicer: Reduce image size by index.
        :param frames: Defines how many arrays will be stacked.
        :param debug: It will show the images if it's True, size = 500x500
        """
        self.__x = x
        self.__y = y
        self.__sizex = sizex
        self.__sizey = sizey

        self.__slicer = slicer

        self.__frames = frames
        self.__stacks = []

        self.__debug = debug

    def pixel(self):
        screen = ImageGrab.grab(bbox=(self.__x, self.__y, self.__sizex, self.__sizey))
        screen = cv2.cvtColor(np.array(screen), cv2.COLOR_BGR2RGB)

        reshape = screen[::self.__slicer, ::self.__slicer]

        if self.__debug:
            debug = cv2.resize(reshape, (500, 500), interpolation=cv2.INTER_NEAREST)

            cv2.imshow("Medusa Vision", debug)
            cv2.moveWindow("Medusa Vision", 450, 10)
            cv2.waitKey(25)
        # Need to create a delay when debug is off, 25ms
        # Need to create a delay when debug is off, 25ms
        # Need to create a delay when debug is off, 25ms

        return reshape

    def stacker(self):
        self.__stacks.clear()

        for loop in range(self.__frames):
            frames = self.pixel()
            self.__stacks.append(frames)

        return np.array(self.__stacks)
