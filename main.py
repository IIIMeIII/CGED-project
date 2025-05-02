import pygame
from button import Button
from role import Role
from player import Player
from enemy import Enemy
from statusBar import StatusBar
import random

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

attackButton =  Button(24, HEIGHT - actionBoxHeight + 20, 
                  "images/attack_btn.png")

magicButton = Button(24, attackButton.rect.y + 110, 
                  "images/magic_btn.png")               

itemButton = Button(24, attackButton.rect.y + 220, 
                  "images/item_btn.png")

potionButton = Button(WIDTH / 2 + 20, HEIGHT - actionBoxHeight + 55,
                  "images/potion_btn.png", "images/potion_btn_hover.png",
                  getActionState = 4)

lightAtkButton = Button(WIDTH / 2 + 20, HEIGHT - actionBoxHeight + 55,
                  "images/LAttack_btn.png", "images/LAttack_btn_hover.png", 
                  light_attack, getActionState = 2)
  
mediumAtkButton = Button(WIDTH / 2 + 20, lightAtkButton.rect.y + 95, 
                  "images/MAttack_btn.png",  "images/MAttack_btn_hover.png", 
                  medium_attack, getActionState = 2)

heavyAtkButton = Button(WIDTH / 2 + 20, lightAtkButton.rect.y + 200,
                  "images/HAttack_btn.png", "images/HAttack_btn_hover.png", 
                  heavy_attack, getActionState = 2)
 
fireAtkButton = Button(WIDTH / 2 + 20, HEIGHT - actionBoxHeight + 55,
                  "images/fire_btn.png", "images/fire_btn_hover.png", 
                  fire_attack, getActionState = 3)

blizzardAtkButton = Button(WIDTH / 2 + 20, fireAtkButton.rect.y + 95,
                  "images/blizzard_btn.png", "images/blizzard_btn_hover.png", 
                  blizzard_attack, getActionState = 3)

thunderAtkButton = Button(WIDTH / 2 + 20, fireAtkButton.rect.y + 200,
                  "images/thunder_btn.png", "images/thunder_btn_hover.png", 
                  thunder_attack, getActionState = 3)

clock = pygame.time.Clock()
fps = 60

brawler = Role(
    roleName = "brawler",
    baseHP = 150, 
    baseMP = 100, 
    baseStrength = 5,
    baseMStrength = 2, 
    baseSpeed = 5, 
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [fire_attack]
)

knight = Role(
    roleName = "knight",
    baseHP = 300,
    baseMP = 150,
    baseStrength = 3,
    baseMStrength = 3,
    baseSpeed = 2,
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [blizzard_attack, thunder_attack]
)

mage = Role(
    roleName = "mage",
    baseHP = 100,
    baseMP = 200,
    baseStrength = 2,
    baseMStrength = 5,
    baseSpeed = 3,
    physicalAtks = [light_attack, medium_attack, heavy_attack], 
    magicAtks = [fire_attack, blizzard_attack, thunder_attack]
)

rogue = Role(
    roleName = "rogue",
    baseHP = 150,
    baseMP = 75,
    baseStrength = 4,
    baseMStrength = 2,
    baseSpeed = 7,
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [thunder_attack]
)

warrior = Role(
    roleName = "warrior",
    baseHP = 250,
    baseMP = 50,
    baseStrength = 5,
    baseMStrength = 2,
    baseSpeed = 3,
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [fire_attack]
)

allRoles = [brawler, knight, mage, rogue, warrior]

def drawTxt(text, textColour, font, xPos, yPos):
    txt = font.render(text, False, textColour)
    screen.blit(txt, (xPos, yPos))

def displayOptions(optionButtons):
    for option in optionButtons:
        option.draw(screen)

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
    
    tempPlayer = Player(
        xPos = 200, 
        yPos = 150, 
        colour = (0, 255, 0), 
        role = brawler)
    tempEnemy = Enemy(
        xPos = 900, 
        yPos = 150, 
        colour = (255, 0, 0), 
        role = random.choice(allRoles)
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

    if tempPlayer.speed < tempEnemy.speed:
        currentActor = 2
        state = 5
    else:
        currentActor = 1

    turn = 1
    gameOver = False
    win = False
    
    # when player chooses role append all attacks that are available to them
    # these will be empty
    physicalAtkButtons = [lightAtkButton, mediumAtkButton, heavyAtkButton] 
    magicAtksButtons = [fireAtkButton, blizzardAtkButton, thunderAtkButton]
    potionButtons = [potionButton]

    while running:
        clock.tick(fps)
        
        if not tempPlayer.aliveStatus:
            gameOver = True
        elif not tempEnemy.aliveStatus:
            win = True

        # fill screen with background colour
        screen.fill(BGCOLOUR)  

        # change state depending on what button is pressed
        if attackButton.pressed(state):
            state = 2
        elif magicButton.pressed(state):
            state = 3
        elif itemButton.pressed(state):
            state = 4

        # set text for each game state and display relevant options
        if state == 0:
            infoTxt = "what will you do next..."
        elif state == 2:
            infoTxt = "select an attack"
            displayOptions(physicalAtkButtons)
            turnEnd = tempPlayer.normalAttack(currentActor=currentActor, currentState=state, 
                                              target=tempEnemy, physicalAttacks=physicalAtkButtons)
            if turnEnd:
                state = 5
                currentActor = 2
                turn += 1
                tempPlayer.updateStatus()
        elif state == 3:
            infoTxt = "select a spell"
            displayOptions(magicAtksButtons)
            turnEnd = tempPlayer.magicAttack(currentActor=currentActor, currentState=state, 
                                             target=tempEnemy, magicAttacks=magicAtksButtons)
            if turnEnd:
                state = 5
                currentActor = 2
                turn += 1
                tempPlayer.updateStatus()
        elif state == 4:
            infoTxt = "select a potion"
            displayOptions(potionButtons)
            turnEnd = tempPlayer.usePotions(currentActor=currentActor, currentState=state, 
                                            currentPotions=potionButtons)
            if turnEnd:
                state = 5
                currentActor = 2
                turn += 1
                tempPlayer.updateStatus()
        elif state == 5:
            infoTxt = "the enemy is attacking!"
            enmyTurnEnd = tempEnemy.attack(currentActor=currentActor, target=tempPlayer)
            if enmyTurnEnd:
                state = 0
                currentActor = 1
                turn += 1
                tempEnemy.updateStatus()
                
        if tempPlayer.abilityCooldown > 0:
            warningTxt = "heavy attack on cooldown..."
        else:
            warningTxt = "heavy attack ready!"

        if tempPlayer.statusEffect != None:
            pStatusTxt = tempPlayer.statusEffect
        else:
            pStatusTxt = ""

        if tempEnemy.statusEffect != None:
            eStatusTxt = tempEnemy.statusEffect
        else:
            eStatusTxt = ""

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
                xPos = playerHealth.xPos + 225, 
                yPos = playerHealth.yPos - 30)
        
        drawTxt(text = eStatusTxt, 
                textColour = (255, 0, 0), 
                font = FONT, 
                xPos = enemyHealth.xPos, 
                yPos = enemyHealth.yPos - 30)

        # draw buttons
        attackButton.draw(screen)
        magicButton.draw(screen)
        itemButton.draw(screen)

        # draw actors  
        tempPlayer.draw(screen)
        tempEnemy.draw(screen)

        # draw status bars
        playerHealth.draw(tempPlayer.hp, screen)
        enemyHealth.draw(tempEnemy.hp, screen)
        playerMP.draw(tempPlayer.mp, screen)
        enemyMP.draw(tempEnemy.mp, screen)

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