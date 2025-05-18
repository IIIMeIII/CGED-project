from actor import Actor

class Player(Actor):
    def __init__(self, xPos, yPos, colour, role):
        super().__init__(xPos, yPos, colour, role)

        self.money = 30

    def normalAttack(self, currentActor, currentState, target, physicalAttacks):
        if self.aliveStatus and currentActor == 1:
            # starts timer
            self.actionTimer += 1
            # function does not run until timer is greater than the wait time
            # prevents player from mashing attack buttons
            if self.actionTimer < self.actionWait:
                return
            # loop through all physical attacks
            for physAtk in physicalAttacks:
                if physAtk.pressed(currentState):
                    # player cannot press heavy attack button until the ability coooldown = 0
                    if physAtk.attackType["name"] == "heavy" and self.abilityCooldown > 0:
                        break
                    elif physAtk.attackType["name"] == "heavy":
                        self.abilityCooldown = 5
                        
                    self.dealDamage(physAtk.attackType["name"], physAtk.attackType["baseDamage"], target)
                    self.actionTimer = 0

                    if self.abilityCooldown > 0:
                        self.abilityCooldown -= 1
                        # print("ability cooldown:", self.abilityCooldown)

                    return True

    def magicAttack(self, currentActor, currentState, target, magicAttacks):
        if self.aliveStatus and currentActor == 1:
            # starts timer
            self.actionTimer += 1
            # function does not run until timer is greater than the wait time
            # prevents player from mashing attack buttons
            if self.actionTimer < self.actionWait:
                return
            # loop through all magic attacks
            for mgkAttack in magicAttacks:
                if mgkAttack.pressed(currentState) and self.mp != 0:
                    # player cannot apply status effects if the target already has one 
                    # will still do damage
                    if not target.resistant: 
                        self.applyStatus(mgkAttack.attackType["statusEffect"], target)
                        # print("Enemy status effect:", target.statusEffect)

                    self.dealDamage(mgkAttack.attackType["name"], mgkAttack.attackType["baseDamage"], target)
                    self.mp -= mgkAttack.attackType["mpCost"]
                    target.statusEffectCooldown = 3
                    target.resistant = True
                    
                    if self.abilityCooldown > 0:
                        self.abilityCooldown -= 1
                        # print("ability cooldown:", self.abilityCooldown)

                    return True

    def usePotions(self, currentActor, currentState, currentPotions):
         if self.aliveStatus and currentActor == 1:
            # starts timer
            self.actionTimer += 1
            # function does not run until timer is greater than the wait time
            # prevents player from mashing attack buttons
            if self.actionTimer < self.actionWait:
                return
            for potion in currentPotions:
                if potion.pressed(currentState) and potion.attackType["currentAmount"] > 0:
                    # stops the potions from healing more than the player's max hp
                    if self.hp + potion.attackType["healStrength"] < self.maxHP:
                        healAmnt = potion.attackType["healStrength"]
                    else:
                        healAmnt = self.maxHP - self.hp

                    # print("Heal amt:", healAmnt)
                    # print("Player HP:", self.hp)

                    self.hp += healAmnt
                    potion.attackType["currentAmount"] -= 1
                    self.actionTimer = 0
                    return True