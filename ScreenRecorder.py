import numpy as np
import pyautogui
from mss import mss
from PIL import Image
import cv2


class ScreenRecorder:
    def __init__(self, id):
        self.id = id

        self.screenWidth, self.screenHeight = pyautogui.size()

        # define the codec
        # fourcc = cv2.VideoWriter_fourcc(*"XVID")

        self.running = False

    def __str__(self):
        return_str = ""
        for i in [self.id, self.screenWidth, self.screenHeight]:
            return_str += str(i) + " "
        return return_str

    def run(self):
        bounding_box = {'top': 110, 'left': 20, 'width': 440, 'height': 295}  # smallest window in top left corner
        sct = mss()
        while self.running:
            sct_img = sct.grab(bounding_box)
            cv2.imshow('screen', np.array(sct_img))

            if (cv2.waitKey(1) & 0xFF) == ord('q'):
                cv2.destroyAllWindows()
                break

        while True:
            setrunning = input("Do you want to start up the program? (Y/N): ")
            if setrunning.upper() == "Y":
                break
            elif setrunning.upper() == "N":
                print("Goodbye! ^_^")
                quit()

        self.startup()

    def startup(self):
        self.running = True
        print("Welcome! :)")
        self.run()
