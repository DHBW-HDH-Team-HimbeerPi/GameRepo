from output_framework.output_framework import OutputFramework as oF
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode
import os
import time

class gameChooser:

    def __init__(self):
        self.mainPath = "./"
        self.gamePathes = ["FLAPPA", "PACCA", "Pong", "sidescroller", "SnakeGameClaim"]
        self.gameNames = ["Flappy Dot", "Pacman", "Pong", "Sidescroller", "Snake"]
        self.check = 0
        self.currentGame = 0
        self.run()

    def inputToDirection(self, direc: int):
        global direction
        direction = direc

    def run(self):
        rotationTreshold = 0.2
        self.inputToDirection(0)
        try:
            controller = IMUController(TriggerMode.CALL_CHECK)
            controller.register_trigger(self.inputToDirection, {'direc': 1}, controller.mov_x, rotationTreshold,
                                        ThresholdType.HIGHER)
            controller.register_trigger(self.inputToDirection, {'direc': 2}, controller.mov_x, -rotationTreshold,
                                        ThresholdType.LOWER)
            controller.register_trigger(self.inputToDirection, {'direc': 3}, controller.mov_y, -rotationTreshold,
                                        ThresholdType.LOWER)

            controller.register_trigger(self.inputToDirection, {'direc': 4}, controller.mov_y, rotationTreshold,
                                        ThresholdType.HIGHER)
        except NameError:
            print("could NOT find controller")
        while True:
            while self.check == 0:
                oF.showText(self.gameNames[self.currentGame], 255, 255, 255, 12, 0.001, 0)
                controller.check_triggers()
                self.checkInput()
                time.sleep(0.5)

            os.chdir('..')
            os.chdir('./raspberry-cementary/')
            if self.currentGame == 0:
                os.chdir('./' + self.gamePathes[0])
            elif self.currentGame == 1:
                os.chdir('./' + self.gamePathes[1])
            elif self.currentGame == 2:
                os.chdir('./' + self.gamePathes[2])
            elif self.currentGame == 3:
                os.chdir('./' + self.gamePathes[3])
            elif self.currentGame == 4:
                os.chdir('./' + self.gamePathes[4])
            os.system('python3 main.py')
            self.check = 0
            os.chdir('..')



    def checkInput(self):
        global direction

        if direction == 2:
            self.check = 1
        elif direction == 3:
            if self.currentGame < 4:
                self.currentGame = self.currentGame + 1
        elif direction == 4:
            if self.currentGame > 0:
                self.currentGame = self.currentGame - 1
        print(direction)
        direction = 0


if __name__ == "__main__":
    gameChooser()
