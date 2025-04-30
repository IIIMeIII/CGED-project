import pygame

class StatusBar():
    """
    This class creates a rectangle that is used to display 
    the player and enemy's stats (e.g health and mana)

    Attributes:
        currentAmnt (int)
        maxAmnt (int)
        xPos (int)
        yPos (int)
        width (int)
        height (int)
        mainCol (tuple)
        bgCol (tuple)
    """
    def __init__(self, currentAmnt, maxAmnt, xPos, yPos, width, height, mainCol, bgCol):
        """
        StatusBar class constructor

        params:
            currentAmnt (int)
            maxAmnt (int)
            xPos (int)
            yPos (int)
            width (int)
            height (int)
            mainCol (tuple)
            bgCol (tuple)
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

        Params:
            currentAmnt (int): 
            surface (window): initialised display window
        """
        self.currentAmnt = currentAmnt
        updatedAmnt = self.currentAmnt / self.maxAmnt
        pygame.draw.rect(screen, self.bgCol, (self.xPos, self.yPos, self.width, self.height))
        pygame.draw.rect(screen, self.mainCol, (self.xPos, self.yPos, self.width * updatedAmnt, self.height))