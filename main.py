import pygame
from Button import Button
from Role import Role
from Actor import Actor
from StatusBar import StatusBar
from random import randint

pygame.init()

WIDTH, HEIGHT = (1200, 1000)
BGCOLOUR = (255, 255, 255)
FONT = pygame.font.Font(None, 40)
actionBoxHeight = 350
screen = pygame.display.set_mode((WIDTH, HEIGHT))

light_attack = {
    "name" : "light",
    "statusEffect" : "none",
    "baseDamage" : 2
}
medium_attack = {
    "name" : "medium",
    "statusEffect" : "none",
    "baseDamage" : 4
}
heavy_attack = {
    "name" : "heavy",
    "statusEffect" : "none",
    "baseDamage" : 6
}
fire_attack = {
    "name" : "fire",
    "statusEffect" : "burning",
    "baseDamage" : 5,
    "mpCost" : 10
}
blizzard_attack = {
    "name" : "blizzard",
    "statusEffect" : "frozen",
    "baseDamage" : 5,
    "mpCost" : 10
}
thunder_attack = {
    "name" : "thunder",
    "statusEffect" : "stunned",
    "baseDamage" : 5,
    "mpCost" : 10
}

attackButton = {
    "button" : Button(24, HEIGHT - actionBoxHeight + 20, 
                  "images/attack_btn.png")
}

magicButton = {
    "button" : Button(24, attackButton["button"].rect.y + 110, 
                  "images/magic_btn.png")               
}

itemButton = {
    "button" : Button(24, attackButton["button"].rect.y + 220, 
                  "images/item_btn.png")
}

potionButton = {
    "button" : Button(WIDTH / 2 + 20, HEIGHT - actionBoxHeight + 55,
                  "images/potion_btn.png", "images/potion_btn_hover.png",
                  getActionState = 4)
}

lightAtkButton = {
    "button" : Button(WIDTH / 2 + 20, HEIGHT - actionBoxHeight + 55,
                  "images/LAttack_btn.png", "images/LAttack_btn_hover.png",
                  getActionState = 2),
    "attackType" : light_attack
}

mediumAtkButton = {
    "button" : Button(WIDTH / 2 + 20, lightAtkButton["button"].rect.y + 95, 
                  "images/MAttack_btn.png",  "images/MAttack_btn_hover.png",
                  getActionState = 2),
    "attackType" : medium_attack
}

heavyAtkButton = {
    "button" : Button(WIDTH / 2 + 20, lightAtkButton["button"].rect.y + 200,
                  "images/HAttack_btn.png", "images/HAttack_btn_hover.png",
                  getActionState = 2),
    "attackType" : heavy_attack
}

fireAtkButton = {
    "button" : Button(WIDTH / 2 + 20, HEIGHT - actionBoxHeight + 55,
                  "images/fire_btn.png", "images/fire_btn_hover.png",
                  getActionState = 3),
    "attackType" : fire_attack
}
    
blizzardAtkButton = {
    "button" : Button(WIDTH / 2 + 20, fireAtkButton["button"].rect.y + 95,
                  "images/blizzard_btn.png", "images/blizzard_btn_hover.png",
                  getActionState = 3),
    "attackType" : blizzard_attack
}

thunderAtkButton = {
    "button" : Button(WIDTH / 2 + 20, fireAtkButton["button"].rect.y + 200,
                  "images/thunder_btn.png", "images/thunder_btn_hover.png",
                  getActionState = 3),
    "attackType" : thunder_attack
}

clock = pygame.time.Clock()
fps = 60

brawler = Role(
    roleName = "brawler",
    baseHP = 150, 
    baseMP = 100, 
    baseStrength = 5,
    baseMStrength = 2, 
    baseSpeed = 5, 
    enemyAtks = ["light", "medium", "heavy"],
    enemyMAtks = [fire_attack]
)

knight = Role(
    roleName = "knight",
    baseHP = 300,
    baseMP = 150,
    baseStrength = 3,
    baseMStrength = 3,
    baseSpeed = 2,
    enemyAtks = ["light", "medium", "heavy"],
    enemyMAtks = [blizzard_attack, thunder_attack]
)

mage = Role(
    roleName = "mage",
    baseHP = 100,
    baseMP = 200,
    baseStrength = 2,
    baseMStrength = 5,
    baseSpeed = 3,
    enemyAtks = ["medium", "heavy"], 
    enemyMAtks = [fire_attack, blizzard_attack, thunder_attack]
)

rogue = Role(
    roleName = "rogue",
    baseHP = 150,
    baseMP = 75,
    baseStrength = 4,
    baseMStrength = 2,
    baseSpeed = 7,
    enemyAtks = ["light", "medium", "heavy"],
    enemyMAtks = [thunder_attack]
)

warrior = Role(
    roleName = "warrior",
    baseHP = 250,
    baseMP = 50,
    baseStrength = 5,
    baseMStrength = 2,
    baseSpeed = 3,
    enemyAtks = ["light", "medium", "heavy"],
    enemyMAtks = [fire_attack]
)

allRoles = [brawler, knight, mage, rogue, warrior]

class StatusBar():
    def __init__(self, currentAmnt, maxAmnt, xPos, yPos, width, height, mainCol, bgCol):
        self.currentAmnt = currentAmnt
        self.maxAmnt = maxAmnt
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.mainCol = mainCol
        self.bgCol = bgCol

    def draw(self, currentAmnt):
        self.currentAmnt = currentAmnt
        updatedAmnt = self.currentAmnt / self.maxAmnt
        pygame.draw.rect(screen, self.bgCol, (self.xPos, self.yPos, self.width, self.height))
        pygame.draw.rect(screen, self.mainCol, (self.xPos, self.yPos, self.width * updatedAmnt, self.height))

def drawTxt(text, textColour, font, xPos, yPos):
    txt = font.render(text, False, textColour)
    screen.blit(txt, (xPos, yPos))

def displayOptions(optionButtons):
    for option in optionButtons:
        option["button"].draw(screen)

def drawActionBox():
    pygame.draw.rect(screen, (0), (0, HEIGHT - actionBoxHeight, WIDTH, 350), 4) 
    pygame.draw.rect(screen, (0), (WIDTH / 2, HEIGHT - actionBoxHeight, WIDTH / 2, 350), 4)

def die():
    screen.fill((255, 0, 0))
    drawTxt("you died :(", (0), FONT, WIDTH/2, HEIGHT/2)

def yay():
    screen.fill((0, 255, 0))
    drawTxt("you won!", (0), FONT, WIDTH/2, HEIGHT/2)

def main():
    running = True
    
    tempPlayer = Actor(
        xPos = 200, 
        yPos = 150, 
        colour = (0, 255, 0), 
        role = brawler
    )
    
    tempEnemy = Actor(
        xPos = 900, 
        yPos = 150, 
        colour = (255, 0, 0), 
        role = allRoles[randint(0, len(allRoles) - 1)]
    )

    playerHealth = StatusBar(currentAmnt = tempPlayer.hp,
                             maxAmnt = tempPlayer.maxHP, 
                             xPos = 20, 
                             yPos = 40, 
                             width = 400, 
                             height = 50, 
                             mainCol = (0, 255, 0), 
                             bgCol = (255, 0, 0)
    )

    enemyHealth = StatusBar(currentAmnt = tempEnemy.hp, 
                            maxAmnt = tempEnemy.maxHP, 
                            xPos = 780, 
                            yPos = 40, 
                            width = 400, 
                            height = 50, 
                            mainCol = (0, 255, 0), 
                            bgCol = (255, 0, 0)
    )

    playerMP = StatusBar(currentAmnt = tempPlayer.mp, 
                         maxAmnt = tempPlayer.maxMP, 
                         xPos = 20, 
                         yPos = 90, 
                         width = 200, 
                         height = 20,
                         mainCol = (0, 0, 255), 
                         bgCol = (255, 0, 0)
    )

    enemyMP = StatusBar(currentAmnt = tempEnemy.mp, 
                        maxAmnt = tempEnemy.maxMP, 
                        xPos = 780, 
                        yPos = 90, 
                        width = 200, 
                        height = 20,
                        mainCol = (0, 0, 255), 
                        bgCol = (255, 0, 0))
        
    warningTxt = ""
    pStatusTxt = ""
    eStatusTxt = ""
     
    state = 0
    actionTimer = 0
    actionWait = 90
    potionHeal = 20

    if tempPlayer.speed <= tempEnemy.speed:
        currentActor = 2
    else:
        currentActor = 1

    turn = 1
    abilityCooldown = 0
    # statusCooldown = 3 

    gameOver = False
    win = False
    
    physicalAttacks = [lightAtkButton, mediumAtkButton, heavyAtkButton] 
    magicAttacks = [fireAtkButton, blizzardAtkButton, thunderAtkButton]
    potions = [potionButton]

    while running:
        clock.tick(fps)
        
        if not tempPlayer.aliveStatus:
            gameOver = True
        elif not tempEnemy.aliveStatus:
            win = True

        # fill screen with background colour
        screen.fill(BGCOLOUR)  

        # set text for each game state and display relevant options
        if state == 0:
            infoTxt = "what will you do next..."
        elif state == 2:
            infoTxt = "select an attack"
            displayOptions(physicalAttacks)
        elif state == 3:
            infoTxt = "select a spell"
            displayOptions(magicAttacks)
        elif state == 4:
            infoTxt = "select a potion"
            displayOptions(potions)
        elif state == 5:
            infoTxt = "the enemy is attacking!"

        # draw action box
        drawActionBox()

        # draw text
        drawTxt(text = infoTxt, 
                textColour = (0), 
                font = FONT, 
                xPos = WIDTH / 2 + 10, 
                yPos = 660)

        drawTxt(text = "turn: " + str(turn), 
                textColour = (0), 
                font = FONT, 
                xPos = WIDTH/2 - 60, 
                yPos = 30)
        
        drawTxt(text = tempPlayer.role.roleName, 
                textColour = (0), 
                font = FONT, 
                xPos = playerHealth.xPos, 
                yPos = playerHealth.yPos - 30)
        
        drawTxt(text = tempEnemy.role.roleName, 
                textColour = (0), 
                font = FONT, 
                xPos = enemyHealth.xPos + 310, 
                yPos = enemyHealth.yPos - 30)
        
        drawTxt(text = warningTxt, 
                textColour = (255, 0, 0), 
                font = FONT, 
                xPos = WIDTH / 2 + 10, 
                yPos = HEIGHT - actionBoxHeight - 50)
        
        drawTxt(text = pStatusTxt, 
                textColour = (255, 0, 0), 
                font = FONT, 
                xPos = 24, 
                yPos = 50)
        
        drawTxt(text = eStatusTxt, 
                textColour = (255, 0, 0), 
                font = FONT, 
                xPos = 980, 
                yPos = 50)

        # draw buttons
        attackButton["button"].draw(screen)
        magicButton["button"].draw(screen)
        itemButton["button"].draw(screen)

        # draw actors  
        tempPlayer.draw(screen)
        tempEnemy.draw(screen)

        # draw status bars
        playerHealth.draw(tempPlayer.hp, screen)
        enemyHealth.draw(tempEnemy.hp, screen)
        playerMP.draw(tempPlayer.mp, screen)
        enemyMP.draw(tempEnemy.mp, screen)

        # change state depending on what button is pressed
        if attackButton["button"].getAction(state):
            state = 2
        elif magicButton["button"].getAction(state):
            state = 3
        elif itemButton["button"].getAction(state):
            state = 4
        
        # player attack
        if tempPlayer.aliveStatus and currentActor == 1:
            # start timer
            actionTimer += 1
            if actionTimer >= actionWait:
                for option in physicalAttacks + magicAttacks:
                    tempVar = option["attackType"]
                    # print(tempVar["statusEffect"])
                    if option["button"].getAction(state):
                        print("yippie")
                        if tempVar["name"] == "heavy" and abilityCooldown > 0:
                            print("yay")
                            break
                        elif tempVar["name"] == "heavy":
                            abilityCooldown = 5
                            warningTxt = "Heavy attack on cooldown..."
                        tempPlayer.attack(tempVar["name"], tempEnemy)

                        if tempVar["statusEffect"] != "none":
                            print("magic")
                            tempPlayer.applyStatus(tempVar["statusEffect"], tempEnemy)
                            print("Enemy status effect:", tempEnemy.statusEffect)
                            tempPlayer.mp -= tempVar["mpCost"]

        #                 state = 0
        #                 currentActor = 2
        #                 actionTimer = 0
        #                 turn += 1
        #                 if abilityCooldown > 0:
        #                     abilityCooldown -= 1
                               
        #                 if abilityCooldown == 0:
        #                     warningTxt = "Heavy attack ready!"
                            
        #                 break
        #         else: # if no break
        #             if potion.button.getAction(state) and tempPlayer.potions > 0:
        #                 if tempPlayer.hp + potionHeal < tempPlayer.maxHP:
        #                     healAmnt = potionHeal
        #                 else:
        #                     healAmnt = tempPlayer.maxHP - tempPlayer.hp

        #                 print("Heal amt:", healAmnt)
        #                 print("Player HP:", tempPlayer.hp)

        #                 tempPlayer.hp += healAmnt
        #                 tempPlayer.potions -= 1
        #                 state = 0
        #                 currentActor = 2
        #                 actionTimer = 0
        #                 turn += 1

        # enemy attack
        # if tempEnemy.aliveStatus and currentActor == 2:
        #     state = 5
        #     actionTimer += 1
        #     if actionTimer >= actionWait:
        #         attacks = tempEnemy.role.enemyAtks + tempEnemy.role.enemyMAtks
        #         attackType = attacks[randint(0, len(attacks) - 1)]
        #         tempEnemy.attack(attackType, tempPlayer)

        #         print(attacks)
        #         print("enemy attack:", attackType)
        #         # make dictionary
        #         # if attackType.statusEffect:
        #         #     print("yer")
        #         #     tempEnemy.applyStatus(attackType.statusEffect, tempPlayer)
        #         #     print("player status effect:", tempPlayer.statusEffect)
        #         #     tempEnemy.mp -= 10
                
        #         currentActor = 1
        #         actionTimer = 0
        #         state = 0

                # no way to differenciate between magic and normal attacks

        if gameOver:
            die()

        if win:
            yay()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    
if __name__ == "__main__":
    main()