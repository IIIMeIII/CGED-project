import pygame

class StatusBar:
    """
    This class creates a rectangle that is used to display 
    the player and enemy's stats (e.g health and mana). This rectangle
    reflects the current amount of these stats in real time

    Attributes:
        currentAmnt (int): current value of variable being represented
            maxAmnt (int): max value of variable being represented
            xPos (int): x position of the status bar
            yPos (int): y position of the status bar
            width (int): width of the status bar
            height (int): height of the status bar
            mainCol (tuple): main colour of the status bar
            bgCol (tuple): colour that appears under the status bar as it updates
    """
    def __init__(self, currentAmnt, maxAmnt, xPos, yPos, width, height, mainCol, bgCol):
        """
        StatusBar class constructor

        Parameters:
            currentAmnt (int): current value of variable being represented
            maxAmnt (int): max value of variable being represented
            xPos (int): x position of the status bar
            yPos (int): y position of the status bar
            width (int): width of the status bar
            height (int): height of the status bar
            mainCol (tuple): main colour of the status bar
            bgCol (tuple): colour that appears under the status bar as it updates
        """
        self.currentAmnt = currentAmnt
        self.maxAmnt = maxAmnt
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.mainCol = mainCol
        self.bgCol = bgCol

    def draw(self, currentAmnt, screen):
        """
        Function that displays the status bar on the window at the passed in 
        x and y coordinates. 

        Parameters:
            currentAmnt (int): current value of status bar
            surface (window): initialised display window
        """
        self.currentAmnt = currentAmnt
        updatedAmnt = self.currentAmnt / self.maxAmnt
        pygame.draw.rect(screen, self.bgCol, (self.xPos, self.yPos, self.width, self.height))
        pygame.draw.rect(screen, self.mainCol, (self.xPos, self.yPos, self.width * updatedAmnt, self.height))