import pygame
from button import Button
from role import Role
from player import Player
from enemy import Enemy
from statusBar import StatusBar
import random

pygame.init()

WIDTH, HEIGHT = (1200, 950)
BGCOLOUR = (255, 255, 255)
FONT = pygame.font.Font(None, 40)
ACTIONBOXHEIGHT = 350
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# ---------------- BACKGROUND IMAGES ---------------- #
MENUIMAGE = pygame.image.load("images/backgrounds/menu_bg.png")
HTPIMAGE = pygame.image.load("images/backgrounds/HTP_bg.png")
CONTROLSIMAGE = pygame.image.load("images/backgrounds/controls_bg.png")
ARENAIMAGE = pygame.image.load("images/backgrounds/arena_bg.png")
PAUSEIMAGE = pygame.image.load("images/backgrounds/pause_bg.png")
SHOPIMAGE = pygame.image.load("images/backgrounds/shop_bg.png")

CLOCK = pygame.time.Clock()
FPS = 60

# ---------------- ALL ATTACKS ---------------- #
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

# ---------------- ALL POTIONS ---------------- #
mini_potion = {
    "name": "potion",
    "price" : 20,
    "healStrength": 30,
    "currentAmount": 3
}
hi_potion = {
    "name": "hipotion",
    "price" : 50,
    "healStrength": 60,
    "currentAmount": 1
}
mega_potion = {
    "name": "megapotion",
    "price" : 120,
    "healStrength": 100,
    "currentAmount": 0
}

# ---------------- MENU BUTTONS ---------------- #
# main menu play button
playButton = Button(WIDTH / 2 - 100, HEIGHT / 2, "images/buttons/play_button.png", 
                    hoverImage = None, attackType = None, getActionState = 0)
# select character play button
startButton = Button(WIDTH / 2 - 100, HEIGHT - 120, "images/buttons/play_button.png", 
                    hoverImage = None, attackType = None, getActionState = 1)

HTPButton = Button(WIDTH / 2 - 100, HEIGHT / 2 + 100, "images/buttons/HTP_button.png", 
                    hoverImage = None, attackType = None, getActionState = 0)

controlsButton = Button(WIDTH / 2 - 100, HEIGHT / 2 + 200, "images/buttons/controls_button.png", 
                    hoverImage = None, attackType = None, getActionState = 0)

backButton = Button(0, HEIGHT - 60, "images/buttons/back_button.png")

nextButton = Button(WIDTH / 2 - 150, HEIGHT - 60, "images/buttons/next_button.png")

# select role screen
selectBrawlerButton = Button(WIDTH / 2 - 590, HEIGHT / 2 - 300, "images/buttons/chara_select_brawler.png", 
                    hoverImage = None, attackType = None, getActionState = 1)

selectKnightButton = Button(WIDTH / 2 - 350, HEIGHT / 2 - 300, "images/buttons/chara_select_knight.png", 
                    hoverImage = None, attackType = None, getActionState = 1)

selectMageButton = Button(WIDTH / 2 - 100, HEIGHT / 2 - 300, "images/buttons/chara_select_mage.png", 
                    hoverImage = None, attackType = None, getActionState = 1)

selectRogueButton = Button(WIDTH / 2 + 130, HEIGHT / 2 - 300, "images/buttons/chara_select_rogue.png", 
                    hoverImage = None, attackType = None, getActionState = 1)

selectWarriorButton = Button(WIDTH / 2 + 380, HEIGHT / 2 - 300, "images/buttons/chara_select_warrior.png", 
                    hoverImage = None, attackType = None, getActionState = 1)

# pause screen
quitButton = Button(WIDTH / 2 - 100, HEIGHT / 2 + 200, "images/buttons/quit_button.png",
                    hoverImage = None, attackType = None, getActionState = 5)

statsButton = Button(WIDTH / 2 - 100, HEIGHT / 2, "images/buttons/stats_button.png",
                    hoverImage = None, attackType = None, getActionState = 5)
# in between fights
shopButton = Button(WIDTH / 2 - 400, HEIGHT / 2 - 150, "images/buttons/shop_button.png",
                    hoverImage = None, attackType = None, getActionState = 6)

restButton = Button(WIDTH / 2 + 200, HEIGHT / 2 - 150, "images/buttons/rest_button.png",
                    hoverImage = None, attackType = None, getActionState = 6)

# potions
miniPotion = Button(80, 300, "images/icons/potion.png", hoverImage = None, 
                    attackType = None, getActionState = 7)

hiPotion = Button(WIDTH / 2 - 150, 300, "images/icons/hi_potion.png", hoverImage = None, 
                    attackType = None, getActionState = 7)

megaPotion = Button(800, 300, "images/icons/mega_potion.png", hoverImage = None, 
                    attackType = None, getActionState = 7)
# ---------------- MAIN LOOP BUTTONS ---------------- #
# action selectors
attackButton =  Button(24, HEIGHT - ACTIONBOXHEIGHT + 20, 
                  "images/buttons/attack_btn.png")

magicButton = Button(24, attackButton.rect.y + 110, 
                  "images/buttons/magic_btn.png")               

itemButton = Button(24, attackButton.rect.y + 220, 
                  "images/buttons/item_btn.png")

# items
miniPotionButton = Button(WIDTH / 2 + 20, HEIGHT - ACTIONBOXHEIGHT + 55,
                  "images/buttons/potion_btn.png", "images/buttons/potion_btn_hover.png",
                  mini_potion, getActionState = 3)

hiPotionButton = Button(WIDTH / 2 + 20, miniPotionButton.rect.y + 95,
                  "images/buttons/hiPotion_btn.png", "images/buttons/hiPotion_btn_hover.png",
                  hi_potion, getActionState = 3)

megaPotionButton = Button(WIDTH / 2 + 20, miniPotionButton.rect.y + 200,
                  "images/buttons/megaPotion_btn.png", "images/buttons/megaPotion_btn_hover.png",
                  mega_potion, getActionState = 3)

# attacks
lightAtkButton = Button(WIDTH / 2 + 20, HEIGHT - ACTIONBOXHEIGHT + 55,
                  "images/buttons/LAttack_btn.png", "images/buttons/LAttack_btn_hover.png", 
                  light_attack, getActionState = 1)
  
mediumAtkButton = Button(WIDTH / 2 + 20, lightAtkButton.rect.y + 95, 
                  "images/buttons/MAttack_btn.png",  "images/buttons/MAttack_btn_hover.png", 
                  medium_attack, getActionState = 1)

heavyAtkButton = Button(WIDTH / 2 + 20, lightAtkButton.rect.y + 200,
                  "images/buttons/HAttack_btn.png", "images/buttons/HAttack_btn_hover.png", 
                  heavy_attack, getActionState = 1)
 
fireAtkButton = Button(WIDTH / 2 + 20, HEIGHT - ACTIONBOXHEIGHT + 55,
                  "images/buttons/fire_btn.png", "images/buttons/fire_btn_hover.png", 
                  fire_attack, getActionState = 2)

blizzardAtkButton = Button(WIDTH / 2 + 20, fireAtkButton.rect.y + 95,
                  "images/buttons/blizzard_btn.png", "images/buttons/blizzard_btn_hover.png", 
                  blizzard_attack, getActionState = 2)

thunderAtkButton = Button(WIDTH / 2 + 20, fireAtkButton.rect.y + 200,
                  "images/buttons/thunder_btn.png", "images/buttons/thunder_btn_hover.png", 
                  thunder_attack, getActionState = 2)

# ---------------- ROLES ---------------- #
brawler = Role(
    roleName = "brawler",
    baseHP = 150, 
    baseMP = 100, 
    baseStrength = 5,
    baseMStrength = 2, 
    baseSpeed = 5, 
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [fire_attack],
    allPotions = [mini_potion, hi_potion, mega_potion]
)

knight = Role(
    roleName = "knight",
    baseHP = 300,
    baseMP = 150,
    baseStrength = 3,
    baseMStrength = 3,
    baseSpeed = 2,
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [blizzard_attack, thunder_attack],
    allPotions = [mini_potion, hi_potion, mega_potion]
)

mage = Role(
    roleName = "mage",
    baseHP = 100,
    baseMP = 200,
    baseStrength = 2,
    baseMStrength = 5,
    baseSpeed = 3,
    physicalAtks = [light_attack, heavy_attack], 
    magicAtks = [fire_attack, blizzard_attack, thunder_attack],
    allPotions = [mini_potion, hi_potion, mega_potion]
)

rogue = Role(
    roleName = "rogue",
    baseHP = 125,
    baseMP = 75,
    baseStrength = 4,
    baseMStrength = 2,
    baseSpeed = 7,
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [thunder_attack],
    allPotions = [mini_potion, hi_potion, mega_potion]
)

warrior = Role(
    roleName = "warrior",
    baseHP = 250,
    baseMP = 50,
    baseStrength = 5,
    baseMStrength = 2,
    baseSpeed = 3,
    physicalAtks = [light_attack, medium_attack, heavy_attack],
    magicAtks = [fire_attack],
    allPotions = [mini_potion, hi_potion, mega_potion]
)

allRoles = [brawler, knight, mage, rogue, warrior]

# ---------------- FUNCTIONS ---------------- #
def drawTxt(text, textColour, font, xPos, yPos):
    txt = font.render(text, False, textColour)
    SCREEN.blit(txt, (xPos, yPos))

def displayOptions(optionButtons):
    for option in optionButtons:
        option.draw(SCREEN)

def drawActionBox():
    pygame.draw.rect(SCREEN, (255, 255, 255), (0, HEIGHT - ACTIONBOXHEIGHT, WIDTH, 350))
    pygame.draw.rect(SCREEN, (255, 255, 255), (WIDTH / 2, HEIGHT - ACTIONBOXHEIGHT - 40, WIDTH / 2, 45))
    pygame.draw.rect(SCREEN, (0), (0, HEIGHT - ACTIONBOXHEIGHT, WIDTH, 350), 4) 
    pygame.draw.rect(SCREEN, (0), (WIDTH / 2, HEIGHT - ACTIONBOXHEIGHT, WIDTH / 2, 350), 4)
    pygame.draw.rect(SCREEN, (0), (WIDTH / 2, HEIGHT - ACTIONBOXHEIGHT - 40, WIDTH / 2, 45), 4)

def displayStats(player):
    pygame.draw.rect(SCREEN, (255, 255, 255), (WIDTH / 2 - 200, HEIGHT / 2 - 200, 500, 600))
    drawTxt("Stats", (0, 0 ,0), FONT, WIDTH / 2 - 200, HEIGHT / 2 - 200)
    drawTxt("HP: " + str(player.maxHP), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 - 150)
    drawTxt("MP: " + str(player.maxMP), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 - 100)
    drawTxt("strength: " + str(player.strength), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 - 50)
    drawTxt("magic strength: " + str(player.MStrength), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2)
    drawTxt("speed: " + str(player.speed), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 + 50)
    drawTxt("mini potions: " + str(mini_potion["currentAmount"]), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 + 100)
    drawTxt("hi-potions: " + str(hi_potion["currentAmount"]), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 + 150)
    drawTxt("mega potions: " + str(mega_potion["currentAmount"]), (0, 0, 0), FONT, WIDTH / 2 - 200, HEIGHT / 2 + 200)

def increaseStats(target):
    target.strength += 2
    target.MStrength += 2
    target.speed += 1
    target.maxHP += 5
    target.money += 15

    if target.hp + ((target.maxHP * 40) / 100) < target.maxHP:
        healAmnt = ((target.maxHP * 40) / 100)
    else:
        healAmnt = target.maxHP - target.hp

    target.hp += healAmnt

def increaseEnemyStats(enemy):
    enemy.strength += 5
    enemy.MStrength += 5
    enemy.speed += 3
    enemy.maxHP += 20

def die():
    SCREEN.fill((255, 0, 0))
    drawTxt("you died :(", (0), FONT, WIDTH/2 - 100, HEIGHT/2 - 100)

def initialisePlayer(role):
    playerPhysAttacks = []
    playerMagicAttacks = []
    playerPotions = []

    player = Player(
        xPos = 200, 
        yPos = 150, 
        colour = (0, 255, 0), 
        role = role
    )
    playerHealth = StatusBar(currentAmnt = player.hp,
        maxAmnt = player.maxHP, 
        xPos = 20, 
        yPos = 40, 
        width = 400, 
        height = 50, 
        mainCol = (0, 255, 0), 
        bgCol = (255, 0, 0)                       
    )           
    playerMP = StatusBar(currentAmnt = player.mp, 
        maxAmnt = player.maxMP, 
        xPos = 20, 
        yPos = 90, 
        width = 200, 
        height = 20,
        mainCol = (0, 0, 255), 
        bgCol = (255, 0, 0)
    )

    for physButton in player.role.physicalAtks:
        if physButton["name"] == "light":
            playerPhysAttacks.append(lightAtkButton)
        elif physButton["name"] == "medium":
            playerPhysAttacks.append(mediumAtkButton)
        elif physButton["name"] == "heavy":
            playerPhysAttacks.append(heavyAtkButton)

    for magicButton in player.role.magicAtks:
        if magicButton["name"] == "fire":
            playerMagicAttacks.append(fireAtkButton)
        elif magicButton["name"] == "blizzard":
            playerMagicAttacks.append(blizzardAtkButton)
        elif magicButton["name"] == "thunder":
            playerMagicAttacks.append(thunderAtkButton)

    for potionButton in player.role.allPotions:
        if potionButton["name"] == "potion":
            playerPotions.append(miniPotionButton)
        elif potionButton["name"] == "hipotion":
            playerPotions.append(hiPotionButton)
        elif potionButton["name"] == "megapotion":
            playerPotions.append(megaPotionButton)
    return player, playerHealth, playerMP, playerPhysAttacks, playerMagicAttacks, playerPotions

def initialiseEnemy():
    enemy = Enemy(
        xPos = 900, 
        yPos = 150, 
        colour = (255, 0, 0), 
        role = random.choice(allRoles)
    )
    enemyHealth = StatusBar(currentAmnt = enemy.hp, 
                            maxAmnt = enemy.maxHP, 
                            xPos = 780, 
                            yPos = 40, 
                            width = 400, 
                            height = 50, 
                            mainCol = (0, 255, 0), 
                            bgCol = (255, 0, 0)
    )
    enemyMP = StatusBar(currentAmnt = enemy.mp, 
                        maxAmnt = enemy.maxMP, 
                        xPos = 780, 
                        yPos = 90, 
                        width = 200, 
                        height = 20,
                        mainCol = (0, 0, 255), 
                        bgCol = (255, 0, 0))
    
    return enemy, enemyHealth, enemyMP

# ---------------- MAIN FUNCTION ---------------- #
def main():
    running = True
    
    # pre game loop variables
    roleSelected = False
    state = 0
    # game loop variables
    gameState = 0
    currentActor = 1
    turn = 1
    totalWins = 0
    warningTxt = ""
    pStatusTxt = ""
    eStatusTxt = ""
    gameOver = False
    win = False
    showStats = False

    while running:
        CLOCK.tick(FPS)
        keys = pygame.key.get_pressed()
        
        # ---------------- MAIN MENU ---------------- #
        if state == 0:
            SCREEN.blit(MENUIMAGE, (0, 0))
            currentButtons = [playButton, HTPButton, controlsButton]
            for buttons in currentButtons:
                buttons.draw(SCREEN)
            
            if playButton.pressed(state):
                print("will play")
                state = 1
            elif HTPButton.pressed(state):
                print("how to play")
                state = 2
            elif controlsButton.pressed(state):
                print("controls")
                state = 3
        # ---------------- HOW TO PLAY MENU ---------------- #
        elif state == 2:
            SCREEN.blit(HTPIMAGE, (0, 0))
            backButton.draw(SCREEN)

            if backButton.pressed(state):
                print("menu")
                state = 0
        # ---------------- CONTROLS MENU ---------------- #
        elif state == 3:
            SCREEN.blit(CONTROLSIMAGE, (0, 0))
            backButton.draw(SCREEN)

            if backButton.pressed(state):
                print("menu")
                state = 0
        # ---------------- SELECT CHAARACTER MENU ---------------- #
        elif state == 1:
            SCREEN.blit(ARENAIMAGE, (0, 0))
            currentButtons = [selectBrawlerButton, selectKnightButton, selectMageButton, 
                              selectRogueButton, selectWarriorButton, startButton]
            currentRole = ""
            for buttons in currentButtons:
                buttons.draw(SCREEN)

            if selectBrawlerButton.pressed(state):
                player, playerHealth, playerMP, physicalAtkButtons, magicAtksButtons, playerPotions = initialisePlayer(brawler)
                roleSelected = True
                # print("selected brawler")
            elif selectKnightButton.pressed(state):
                player, playerHealth, playerMP, physicalAtkButtons, magicAtksButtons, playerPotions = initialisePlayer(knight)
                roleSelected = True
                # print("selected knight")
            elif selectMageButton.pressed(state):
                player, playerHealth, playerMP, physicalAtkButtons, magicAtksButtons, playerPotions = initialisePlayer(mage)
                roleSelected = True
                # print("selected mage")
            elif selectRogueButton.pressed(state):
                player, playerHealth, playerMP, physicalAtkButtons, magicAtksButtons, playerPotions = initialisePlayer(rogue)
                roleSelected = True
                # print("selected rogue")
            elif selectWarriorButton.pressed(state):
                player, playerHealth, playerMP, physicalAtkButtons, magicAtksButtons, playerPotions = initialisePlayer(warrior)
                roleSelected = True

            if roleSelected:
                drawTxt("your role: " + player.role.roleName, (0, 0, 0), FONT, WIDTH / 2 - 100, 50)

            enemy, enemyHealth, enemyMP = initialiseEnemy()
            if roleSelected and startButton.pressed(state):
                if player.speed < enemy.speed:
                    currentActor = 2
                    gameState = 5
                else:
                    currentActor = 1
                state = 4
        # ---------------- MAIN LOOP ---------------- #
        elif state == 4:
            if keys[pygame.K_ESCAPE]:
                state = 5

            # fill screen with background image
            SCREEN.blit(ARENAIMAGE, (0, 0))

            if not player.aliveStatus:
                gameOver = True
            elif not enemy.aliveStatus:
                win = True

            # draw action box
            drawActionBox()

            # change state depending on what button is pressed
            if attackButton.pressed(gameState):
                gameState = 1
            elif magicButton.pressed(gameState):
                gameState = 2
            elif itemButton.pressed(gameState):
                gameState = 3

            # set text for each game state and display relevant options
            if gameState == 0:
                infoTxt = "what will you do next..."
            elif gameState == 1:
                infoTxt = "select an attack"
                displayOptions(physicalAtkButtons)
                turnEnd = player.normalAttack(currentActor=currentActor, currentState=gameState, 
                                                  target=enemy, physicalAttacks=physicalAtkButtons)
                if turnEnd:
                    gameState = 5
                    currentActor = 2
                    turn += 1
                    player.updateStatus()
            elif gameState == 2:
                infoTxt = "select a spell"
                displayOptions(magicAtksButtons)
                turnEnd = player.magicAttack(currentActor=currentActor, currentState=gameState, 
                                                 target=enemy, magicAttacks=magicAtksButtons)
                if turnEnd:
                    gameState = 5
                    currentActor = 2
                    turn += 1
                    player.updateStatus()
            elif gameState == 3:
                infoTxt = "select a potion"
                displayOptions(playerPotions)
                turnEnd = player.usePotions(currentActor=currentActor, currentState=gameState, 
                                                currentPotions=playerPotions)
                if turnEnd:
                    gameState = 5
                    currentActor = 2
                    turn += 1
                    player.updateStatus()
            elif gameState == 5:
                infoTxt = "the enemy is attacking!"
                enmyTurnEnd = enemy.attack(currentActor=currentActor, target=player)
                if enmyTurnEnd:
                    gameState = 0
                    currentActor = 1
                    turn += 1
                    enemy.updateStatus()

            if player.abilityCooldown > 0:
                warningTxt = "heavy attack on cooldown..."
            else:
                warningTxt = "heavy attack ready!"

            if player.statusEffect != None:
                pStatusTxt = player.statusEffect
            else:
                pStatusTxt = ""

            if enemy.statusEffect != None:
                eStatusTxt = enemy.statusEffect
            else:
                eStatusTxt = ""

            # draw text
            drawTxt(text = infoTxt, 
                    textColour = (0), 
                    font = FONT, 
                    xPos = WIDTH / 2 + 10, 
                    yPos = HEIGHT - ACTIONBOXHEIGHT + 5)

            drawTxt(text = "turn: " + str(turn), 
                    textColour = (0), 
                    font = FONT, 
                    xPos = WIDTH/2 - 60, 
                    yPos = 30)
            
            drawTxt(text = "wins: " + str(totalWins), 
                    textColour = (0), 
                    font = FONT, 
                    xPos = WIDTH/2 - 60, 
                    yPos = 60)
            
            drawTxt(text = player.role.roleName, 
                    textColour = (0), 
                    font = FONT, 
                    xPos = playerHealth.xPos, 
                    yPos = playerHealth.yPos - 30)
            
            drawTxt(text = enemy.role.roleName, 
                    textColour = (0), 
                    font = FONT, 
                    xPos = enemyHealth.xPos + 310, 
                    yPos = enemyHealth.yPos - 30)
            
            drawTxt(text = warningTxt, 
                    textColour = (255, 0, 0), 
                    font = FONT, 
                    xPos = WIDTH / 2 + 10, 
                    yPos = HEIGHT - ACTIONBOXHEIGHT - 30)
            
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
            attackButton.draw(SCREEN)
            magicButton.draw(SCREEN)
            itemButton.draw(SCREEN)

            # draw actors  
            player.draw(SCREEN)
            enemy.draw(SCREEN)

            # draw status bars
            playerHealth.draw(player.hp, SCREEN)
            enemyHealth.draw(enemy.hp, SCREEN)
            playerMP.draw(player.mp, SCREEN)
            enemyMP.draw(enemy.mp, SCREEN)
            
            if gameOver:
                die()

            if win:
                totalWins += 1
                turn = 1
                increaseStats(player)
                enemy, enemyHealth, enemyMP = initialiseEnemy()
                state = 4

                win = False

            if totalWins == 3:
                state = 6
        # ---------------- PAUSE MENU ---------------- #
        elif state == 5:
            if keys[pygame.K_BACKSPACE]:
                state = 4

            currentButtons = [quitButton, statsButton, backButton]
            SCREEN.blit(PAUSEIMAGE, (0, 0))
            for buttons in currentButtons:
                buttons.draw(SCREEN)

            if quitButton.pressed(state):
                state = 0
            elif statsButton.pressed(state):
                showStats = True
            elif backButton.pressed(state) and showStats:
                showStats = False

            if showStats:
                displayStats(player)
        # ---------------- POST WIN MENU ---------------- #
        elif state == 6:
            currentButtons = [restButton, shopButton]
            SCREEN.blit(ARENAIMAGE, (0, 0))

            for buttons in currentButtons:
                buttons.draw(SCREEN)

            if restButton.pressed(state):
                player.hp = player.maxHP
                player.mp = player.maxMP
                enemy, enemyHealth, enemyMP = initialiseEnemy()
                increaseEnemyStats(enemy)
                totalWins = 0
                state = 4
            if shopButton.pressed(state):
                player.hp = player.maxHP
                player.mp = player.maxMP
                state = 7
        # ---------------- SHOP MENU ---------------- #
        elif state == 7:
            currentButtons = [miniPotion, hiPotion, megaPotion, nextButton]
            SCREEN.blit(SHOPIMAGE, (0, 0))
            for buttons in currentButtons:
                buttons.draw(SCREEN)

            drawTxt("money: " + str(player.money), (0), FONT, WIDTH / 2 - 100, 20)
            drawTxt("price: " + str(mini_potion["price"]), (0), FONT, 80, 650)
            drawTxt("price: " + str(hi_potion["price"]), (0), FONT, WIDTH / 2 - 150, 650)
            drawTxt("price: " + str(mega_potion["price"]), (0), FONT, 1000, 650)

            if miniPotion.pressed(state) and (player.money - mini_potion["price"]) > 0:
                player.money -= mini_potion["price"]
            elif hiPotion.pressed(state) and (player.money - hi_potion["price"]) > 0:
                player.money -= hi_potion["price"]
            elif megaPotion.pressed(state) and (player.money - mega_potion["price"]) > 0:
                player.money -= mega_potion["price"]
            elif nextButton.pressed(state):
                enemy, enemyHealth, enemyMP = initialiseEnemy()
                increaseEnemyStats(enemy)
                totalWins = 0
                state = 4

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()
    
if __name__ == "__main__":
    main()