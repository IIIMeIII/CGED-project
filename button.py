import pygame

class Button():
    """
    This class creates a button that is used to complete actions

    Attributes:
        image (file): the image that will act as the button
        rect (object): stores the rectangular coordinates of the image
        clicked (boolean): flag used to evaluate if the button has been pressed
    """
    def __init__(self, x_pos, y_pos, image, hoverImage = None, getActionState = None):
        """
        Button class constructor

        Params:
            x_pos (int): x position of the button rect
            y_pos (int): y position of the button rect
            image (file): image used for the graphics of the button
            hasHover (boolean): used to determine whether the relevant variables for the hover image need to be initialised
            hoverImage (image): image used for the graphics of the button when the mouse is in contact with the button rect
            getActionState (int): represents the current state of the game and used to make sure actions only occur in the
            correct state
        """
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_pos, y_pos)
        self.getActionState = getActionState

        if hoverImage:
            self.hoverImage = pygame.image.load(hoverImage)
            self.hoverRect = self.hoverImage.get_rect()
            self.hoverRect.topleft = (x_pos, y_pos)
        else:
            self.hoverImage = None

        self.clicked = False

    def draw(self, surface):
        """
        Function that displays the button on the window at the passed in 
        x and y coordinates

        Params:
            surface (window): initialised display window
        """
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos) and self.hoverImage:
            surface.blit(self.hoverImage, (self.rect.x, self.rect.y))
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
    
    def getAction(self, state):
        """
        Function that gets the current mouse position and evaluates if it
        is currently inside the button rect. clicked is only set to True
        when the left mouse button is clicked to prevent collidepoint()
        from running more than once

        Params:
            state (int): current state of the game
        Returns:
            action: A boolean that can be used to trigger certain events when
                    the button is pressed
        """
        action = False

        if self.getActionState and state != self.getActionState:
            return action
        
        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False;

        return action