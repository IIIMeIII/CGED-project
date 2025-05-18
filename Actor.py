import pygame

class Actor:
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
        self.potionHeal = 30
        
        self.abilityCooldown = 0
        self.statusEffectCooldown = 0
        self.actionTimer = 0
        self.actionWait = 60
        self.aliveStatus = True # alive status
        self.statusEffect = None
        self.resistant = False

    def draw(self, screen):
        pygame.draw.rect(screen, (self.colour), (self.xPos, self.yPos, 100, 400))  

    def dealDamage(self, attackType, baseDamage, target):
        # deal damage to target based on attack type
        if attackType == "light":
            damageDone = baseDamage * self.strength
            target.hp -= damageDone
        elif attackType == "medium":
            damageDone = baseDamage * self.strength
            target.hp -= damageDone
        elif attackType == "heavy":
            damageDone = baseDamage * self.strength
            target.hp -= damageDone
        elif attackType == "fire":
            damageDone = baseDamage * self.MStrength
            target.hp -= damageDone
        elif attackType == "blizzard":
            damageDone = baseDamage * self.MStrength
            target.hp -= damageDone
        elif attackType == "thunder":
            damageDone = baseDamage * self.MStrength
            target.hp -= damageDone

        # check if target is still alive
        if target.hp <= 0:
            target.hp = 0
            target.aliveStatus = False

    def applyStatus(self, statusType, target):
        target.statusEffect = statusType

    def updateStatus(self):
        if self.statusEffectCooldown > 0:
            self.statusEffectCooldown -= 1
            self.resistant = True
            # print("cannot have status effect")
            # print("resistance status:", self.resistant)
            # print("resistance cooldown:", self.statusEffectCooldown)

        if self.statusEffectCooldown == 0:
            self.resistant = False
            self.statusEffect = None
            # print("can have status effect")
            # print("resistance status:", self.resistant)
            # print("resistance cooldown:", self.statusEffectCooldown)