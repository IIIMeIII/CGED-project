from actor import Actor 
import random

class Enemy(Actor):
    def __init__(self, xPos, yPos, colour, role):
        super().__init__(xPos, yPos, colour, role)

    def attack(self, currentActor, target):
        if self.aliveStatus and currentActor == 2:
            # starts timer
            self.actionTimer += 1
            if self.actionTimer >= self.actionWait:
                chance = random.randint(0, 1)
                # check if potion use is available
                if self.hp / self.maxHP < 0.5 and self.potions > 0 and chance == 1:
                    if self.hp + self.potionHeal < self.maxHP:
                        healAmnt = self.potionHeal
                    else:
                        healAmnt = self.maxHP - self.hp
                    self.hp += healAmnt
                    self.potions -= 1
                    self.actionTimer = 0
                    return True
                else:
                    # assign all of the role's attacks to one variable
                    allRoleAttacks = self.role.physicalAtks + self.role.magicAtks
                    attack = allRoleAttacks[random.randint(0, len(allRoleAttacks) - 1)]
                    # enemy cannot keep using heavy attack
                    if attack["name"] == "heavy" and self.abilityCooldown > 0:
                        # print("tried to use heavy attack")
                        attack = allRoleAttacks[1]
                    elif attack["name"] == "heavy":
                        self.abilityCooldown = 5
                    self.dealDamage(attack["name"], attack["baseDamage"], target)
                    # magic attack
                    if attack["statusEffect"] != "none":
                        # apply status effect to target if they are not resistant
                        if not target.resistant:
                            self.applyStatus(attack["statusEffect"],  target)
                            # print("player status effect:", target.statusEffect)
                            # start target's resistance cooldown
                            target.statusEffectCooldown = 3 
                        self.mp -= attack["mpCost"]

                    self.actionTimer = 0
                    self.abilityCooldown -= 1
                    # print("enemy cooldown:", self.abilityCooldown)
                    # print("enemy used:", attack)
                    return True