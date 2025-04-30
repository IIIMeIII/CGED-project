import pygame

class Actor():
    def __init__(self, xPos, yPos, colour, role):
        self.xPos = xPos
        self.yPos = yPos
        self.colour = colour
        self.role = role

        self.hp = role.baseHP
        self.maxHP = self.hp

        self.mp = role.baseMP
        self.maxMP = self.mp

        self.strength = role.baseStrength
        self.MStrength = role.baseMStrength
        self.speed = role.baseSpeed

        self.potions = 3

        self.aliveStatus = True # alive status
        self.statusEffect = None
        self.resistant = False

    def draw(self, screen):
        pygame.draw.rect(screen, (self.colour), (self.xPos, self.yPos, 100, 400))  

    def attack(self, attackType, target):
        # deal damage to target based on attack type
        if attackType == "light":
            damageDone = 2 * self.strength
            target.hp -= damageDone
        elif attackType == "medium":
            damageDone = 4 * self.strength
            target.hp -= damageDone
        elif attackType == "heavy":
            damageDone = 6 * self.strength
            target.hp -= damageDone
        elif attackType == "fire":
            damageDone = 5 * self.MStrength
            target.hp -= damageDone
        elif attackType == "blizzard":
            damageDone = 5 * self.MStrength
            target.hp -= damageDone
        elif attackType == "thunder":
            damageDone = 5 * self.MStrength
            target.hp -= damageDone

        # check if target is still alive
        if target.hp <= 0:
            target.hp = 0
            target.aliveStatus = False

    def applyStatus(self, statusType, target):
        target.statusEffect = statusType