"""
Author: Lukas Müller
Date: 7.1.2021
"""
import tkinter as tk
from random import randint

counter = 1  # control variable to set the new target and delete the old one
counterClicks = 0  # counts the clicks in general to show the number to the user
counterHits = 0  # counts the hits
counterMiss = 0  # counts the misses
hitrate = 0  # calculates the hit percentage
targets = 20  # control variable for the number of targets


# Main application class
class App:

    def __init__(self, master):
        self.master = master
        # member variables
        self.counter = counter
        self.counterClicks = counterClicks
        self.counterHits = counterHits
        self.counterMiss = counterMiss
        self.hitrate = hitrate
        # create canvas
        self.canvas = tk.Canvas(master, bg='#A9E2F3')
        self.canvas.place(x=10, y=10, width=680, height=420)
        # create frame
        self.frameButtons = tk.Frame(master)
        self.frameButtons.place(x=5, y=440, width=690, height=50)
        # create labels
        self.labelHits = tk.Label(master=self.frameButtons, anchor='w', text=f'Hits: {self.counterHits}',
                                  font='Arial 14')
        self.labelHits.place(x=5, y=5, width=80, height=40)
        self.labelMiss = tk.Label(master=self.frameButtons, anchor='w', text=f'Misses: {self.counterMiss}',
                                  font='Arial 14')
        self.labelMiss.place(x=90, y=5, width=100, height=40)
        self.labelHitrate = tk.Label(master=self.frameButtons, anchor='w', text=f'{self.hitrate}%', font='Arial 14')
        self.labelHitrate.place(x=195, y=5, width=80, height=40)
        # create buttons
        self.buttonStart = tk.Button(master=self.frameButtons, bg='#B1B0B0', bd=1, text='Start', font='Arial 14',
                                     command=self.startGame)
        self.buttonStart.place(x=350, y=5, width=80, height=40)
        self.buttonSettings = tk.Button(master=self.frameButtons, bg='#B1B0B0', bd=1, text='Settings', font='Arial 14',
                                        command=self.openWindow)
        self.buttonSettings.place(x=435, y=5, width=80, height=40)
        self.buttonReset = tk.Button(master=self.frameButtons, bg='#B1B0B0', bd=1, text='Reset', font='Arial 14',
                                     command=self.reset)
        self.buttonReset.place(x=520, y=5, width=80, height=40)
        self.buttonQuit = tk.Button(master=self.frameButtons, bg='#B1B0B0', bd=1, text='Quit', font='Arial 14',
                                    command=self.quitGame)
        self.buttonQuit.place(x=605, y=5, width=80, height=40)
        # events
        self.canvas.bind('<Button-1>', self.remove)

    # starts the game and places the first target
    def startGame(self):

        # calls reset function
        self.reset()
        # disables the settings button
        self.buttonSettings.config(state=tk.DISABLED)
        # creates random coordinates for the circle
        self.randX = randint(5, 655)
        self.randY = randint(5, 395)
        # creates the first circle -> random position
        self.id_circle = self.canvas.create_oval(self.randX, self.randY, self.randX + 20, self.randY + 20, fill='red')

    # places a new circle -> called by remove function
    def place(self):
        # new random coordinates
        (x, y) = (randint(5, 655), randint(5, 395))

        if self.counter % 2:
            # takes the old coordinates
            (x0, y0, x1, y1) = tuple(self.canvas.coords(self.id_circle))
            # creates a new target at an different position
            self.id_circle2 = self.canvas.create_oval(x, y, x + (x1 - x0), y + (y1 - y0), fill='red')

        else:
            (x0, y0, x1, y1) = tuple(self.canvas.coords(self.id_circle2))
            self.id_circle = self.canvas.create_oval(x, y, x + (x1 - x0), y + (y1 - y0), fill='red')

    # calls place function and removes the old circle
    def remove(self, event):
        (x, y) = (event.x, event.y)

        try:
            if self.counter % 2:
                (x0, y0, x1, y1) = tuple(self.canvas.coords(self.id_circle))
                if x0 <= x <= x1 and y0 <= y <= y1:
                    self.place()
                    self.canvas.delete(self.id_circle)
                    self.counter += 1
                    self.counterHitUpdate()
                else:
                    self.counterMissUpdate()

            else:
                (x0, y0, x1, y1) = tuple(self.canvas.coords(self.id_circle2))
                if x0 <= x <= x1 and y0 <= y <= y1:
                    self.place()
                    self.canvas.delete(self.id_circle2)
                    self.counter += 1
                    self.counterHitUpdate()
                else:
                    self.counterMissUpdate()

            self.counterClicks += 1
            self.hitrateUpdate()
            self.finishGame()

        except:
            pass

    # counts the number of targets the user hit
    def counterHitUpdate(self):
        self.counterHits += 1
        self.labelHits.config(text=f'Hits: {self.counterHits}')

    # counts the number of missed clicks by the user
    def counterMissUpdate(self):
        self.counterMiss += 1
        self.labelMiss.config(text=f'Misses: {self.counterMiss}')

    # calculates the hitrate
    def hitrateUpdate(self):
        self.hitrate = str((self.counterHits / self.counterClicks) * 100)
        self.labelHitrate.config(text=f'{self.hitrate[:5]}%')

    # runs when the number of targets is reached
    def finishGame(self):

        if self.counterHits == targets:
            self.labelEndscreen = tk.Label(master=self.canvas,
                                           text=f'Hitrate: {self.hitrate[:5]}%, Clicks: {self.counterClicks}',
                                           font='Arial 14')
            self.labelEndscreen.pack()
            self.canvas.delete(self.id_circle, self.id_circle2)
            self.buttonSettings.config(state=tk.NORMAL)

    # resets the counters
    def reset(self):

        if self.counterHits == targets:
            self.labelEndscreen.destroy()

        self.counter = counter
        self.counterClicks = counterClicks
        self.counterHits = counterHits
        self.counterMiss = counterMiss
        self.hitrate = hitrate

        self.labelHits.config(text=f'Hits: {self.counterHits}')
        self.labelMiss.config(text=f'Misses: {self.counterMiss}')
        self.labelHitrate.config(text=f'{self.hitrate}%')

        try:
            self.buttonSettings.config(state=tk.NORMAL)
            self.canvas.delete(self.id_circle)
            self.canvas.delete(self.id_circle2)

        except:
            pass

    # opens the settings window
    def openWindow(self):
        # calls reset function
        self.reset()
        # creates the new window
        self.settingWindow = tk.Toplevel(self.master)
        self.settingWindow.maxsize(200, 140)
        self.settingWindow.title('Settings')
        self.app = Settings(self.settingWindow)

    # destroys the main window
    def quitGame(self):
        self.master.destroy()


# window to change the settings
class Settings:

    def __init__(self, master):
        self.master = master
        self.valueDict = {'5': 5,
                          '10': 70,
                          '20': 135,
                          '30': 5,
                          '35': 70,
                          '50': 135}
        self.radioButtonList = []
        # label for the text
        self.labelSettings = tk.Label(master, text=f'Hit {targets} targets to finish.', font='Arial 14')
        self.labelSettings.place(x=5, y=5, width=190, height=40)
        # frame for the buttons
        self.frameSettingButton = tk.Frame(master)
        self.frameSettingButton.place(x=0, y=50, width=200, height=90)
        # variable to handle the value
        self.targetValue = tk.StringVar()
        # buttons to change the number of targets
        for (value, coords) in self.valueDict.items():
            self.button = tk.Radiobutton(master=self.frameSettingButton, bg='#B1B0B0', bd=1, indicator=0, text=value,
                                         value=value, variable=self.targetValue, font='Arial 14',
                                         command=self.changeSetting)
            if len(self.radioButtonList) <= 2:
                self.button.place(x=coords, y=0, width=60, height=40)
            if len(self.radioButtonList) >= 3:
                self.button.place(x=coords, y=45, width=60, height=40)
            self.radioButtonList.append(self.button)

    # function to change the number of targets
    def changeSetting(self):
        global targets
        # get the value of the button
        self.newTargets = self.targetValue.get()
        targets = int(self.newTargets)
        # change the value
        self.labelSettings.config(text=f'Hit {targets} targets to finish.')
        # calls the function to deselect the button
        self.cleanButton()

    # function to clean the buttons
    def cleanButton(self):
        for i in range(6):
            self.radioButtonList[i].deselect()


# global code
def main():
    root = tk.Tk()
    root.minsize(700, 500)
    root.title('Aimtrainer')
    app = App(root)
    root.mainloop()


if __name__ == '__main__':
    main()
