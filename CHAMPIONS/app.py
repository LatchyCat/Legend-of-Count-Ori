
#! Current Fighter Classes
from fighters.knight import Knight
from fighters.bandit import Bandit
from fighters.blob import Blob

from fighters.healthbar import HealthBar
from buttons.button import Button
from fighters.damagetext import DamageText


#! Future Imports Fighter Classes
# from fighters.archer import Archer
# from fighters.monk import Monk
# from fighters.wizard import Wizard
# from fighters.summoner import Summoner

#Import pygame and invoke the init function
import pygame
import random
pygame.init()

clock = pygame.time.Clock()
fps = 60

'''
#! Random Background Generator
#? Under development
# import random
# radnom_background = ['CHAMPIONS/images/background_one.jpg', 'CHAMPIONS/images/background_two.jpg']
# random_index = random.randint(0, len(random_background) - 1)
'''


#! Game Window
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Legend of Count Ori")

#! Difine game variables
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_wait_time = 90
attack = False
potion = False
potion_effect = 15
clicked = False
game_over = 0


#? Define the path to your downloaded font file
font_path = ''

#? Define Fonts
font = pygame.font.SysFont('MedievalSharp', 26)

#? Define Colours
red = (255, 0, 0)
green = (0, 255, 0)


#! Define damage_text_group here
damage_text_group = pygame.sprite.Group()

#! Load Images
#! Back Ground Image
back_ground_img = pygame.image.load('CHAMPIONS/images/background/background.png').convert_alpha()

#! Panel Image
panel_img = pygame.image.load('CHAMPIONS/images/icons/panel.png').convert_alpha()

#! Button Images
potion_img = pygame.image.load('CHAMPIONS/images/icons/potion.png').convert_alpha()
restart_img = pygame.image.load('CHAMPIONS/images/icons/restart.png').convert_alpha()

#! Load Victory and Defeat Images
victory_img = pygame.image.load('CHAMPIONS/images/icons/victory.png').convert_alpha()
defeat_img = pygame.image.load('CHAMPIONS/images/icons/defeat.png').convert_alpha()

#! Sword Image
sword_img = pygame.image.load('CHAMPIONS/images/icons/sword.png').convert_alpha()

#! Create function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


#! Function for drawing backgrounds
def draw_bg():
    screen.blit(back_ground_img, (0, 0))



#! Function for drawing panel
def draw_panel():
    #? Draw panel rectangle
    screen.blit(panel_img, (0, screen_height - bottom_panel))

    #?Show knight stats
    draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height - bottom_panel + 10)

    for count, i in enumerate(enemy_list):
        #? Show name and health
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 10) + count * 60)



#! Current Fighter models
knight = Knight(200, 260, 'Knight', 30, 15, 3, damage_text_group)
bandit1 = Bandit(550, 270, 'Bandit', 20, 6, 1, damage_text_group)
bandit2 = Bandit(700, 270, 'Bandit', 20, 6, 1, damage_text_group)
blob = Summoner(700, 270, 'Summoner', 20, 8, 1, damage_text_group)
Summoner2 = Summoner(700, 270, 'Summoner', 20, 8, 1, damage_text_group)


#? Holding Enemy's
enemy_list = []
enemy_list.append(bandit1)
enemy_list.append(bandit2)



#? Health Bars
knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)


#! Future Fighters
#?       x, y, name, max_hp, strength, potions
# archer = Archer(200, 260, 'Archer', 100, 8, 3)
# wizard = Wizard(200, 260, 'Wizard', 100, 14, 3)
# monk =   Monk(200, 260, 'Monk', 100, 12, 10)


#! Create Buttons
potion_button = Button(screen, 100, screen_height - bottom_panel + 70, potion_img, 64, 64)
restart_button = Button(screen, 330, 120, restart_img, 120, 30)


#! WARNING
#! The game is RUNNING HERE
run = True
while run:

    clock.tick(fps)


    #* Update health bars with current health values
    knight_health_bar.hp = knight.hp
    bandit1_health_bar.hp = bandit1.hp
    bandit2_health_bar.hp = bandit2.hp

    #* Draw Background
    draw_bg()

    #* Draw Panel
    draw_panel()
    knight_health_bar.draw(screen)
    bandit1_health_bar.draw(screen)
    bandit2_health_bar.draw(screen)

    #* Draw Knight
    knight.update()
    knight.draw(screen)

    #* Draw Bandit
    for bandit in enemy_list:
        bandit.update()
        bandit.draw(screen)



    #Draw the damage text
    damage_text_group.update()
    damage_text_group.draw(screen)


    #* Control Player Action
    #* Reset Action Variables
    attack = False
    potion = False
    target = None
    # Make sure mouse is visable
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()
    for count, bandit in enumerate(enemy_list):
        if bandit.rect.collidepoint(pos):
            # Hide Mouse
            pygame.mouse.set_visible(False)
            # Show sword in place of mouse cursor
            screen.blit(sword_img, pos)
            if clicked == True and bandit.alive == True:
                attack = True
                target = enemy_list[count]

    if potion_button.draw():
        potion = True
    # Show number of potions left
    draw_text(str(knight.potions), font, red, 150, screen_height - bottom_panel + 70)


    if game_over == 0:
        #* Player Action
        if knight.alive == True:
            if current_fighter == 1:
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    #* Look for player action
                    #* Attack
                    if attack == True and target != None:
                        knight.attack(target, font)
                        current_fighter += 1
                        action_cooldown = 0
                    #* Potion
                    if potion == True:
                        if knight.potions > 0:
                            #? Check if the potion will heal over max Health
                            if knight.max_hp - knight.hp > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = knight.max_hp - knight.hp
                            knight.hp += heal_amount
                            knight.potions -= 1
                            #Damage Text
                            damage_text = DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), green, font)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown = 0
        else:
            game_over = -1


        #* Enemy Action
        for count, bandit in enumerate(enemy_list):
            if current_fighter == 2 + count:
                if bandit.alive == True:
                    action_cooldown += 1
                    if action_cooldown >= action_wait_time:
                        #? Check if bandit needs to heal first
                        if (bandit.hp / bandit.max_hp) < 0.5 and bandit.potions > 0:
                            #? Check if the potion would heal the bandit beyond max health
                            if bandit.max_hp - bandit.hp > potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = bandit.max_hp - bandit.hp
                            bandit.hp += heal_amount
                            bandit.potions -= 1
                            #Damage Text
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green, font)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown = 0
                        #Attack
                        else:
                            bandit.attack(knight, font)
                            current_fighter += 1
                            action_cooldown = 0
                else:
                    current_fighter += 1

            #* If all fighters have had a turn then reset
            if current_fighter > total_fighters:
                current_fighter = 1


    #? Check if all bandits are dead
    alive_bandits = 0
    for bandit in enemy_list:
        if bandit.alive == True:
            alive_bandits += 1
    if alive_bandits == 0:
        game_over = 1


    #? Check if game is over
    if game_over != 0:
        if game_over == 1:
            screen.blit(victory_img, (250, 50))
        if game_over == -1:
            screen.blit(defeat_img, (290, 50))
        if restart_button.draw():
            knight.reset()
            for bandit in enemy_list:
                bandit.reset()
            current_fighter = 1
            action_cooldown
            game_over = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        else:
            clicked = False



    pygame.display.update()

pygame.quit()
