
#! Current Fighter Classes
from fighters.knight import Knight
from fighters.bandit import Bandit
from fighters.healthbar import HealthBar


#! Future Imports Fighter Classes
# from fighters.archer import Archer
# from fighters.monk import Monk
# from fighters.wizard import Wizard

#Import pygame and invoke the init function
import pygame
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




#? Define the path to your downloaded font file
font_path = ''

#? Define Fonts
font = pygame.font.SysFont('MedievalSharp', 26)

#? Define Colours
red = (255, 0, 0)
green = (0, 255, 0)



#! Load Images
#! Back Ground Image
back_ground_img = pygame.image.load('CHAMPIONS/images/background/background.png').convert_alpha()

#! Panel Image
panel_img = pygame.image.load('CHAMPIONS/images/icons/panel.png').convert_alpha()



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

    for count, i in enumerate(bandit_list):
        #? Show name and health
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, (screen_height - bottom_panel + 10) + count * 60)



#! Current Fighter models
knight = Knight(200, 260, 'Knight', 100, 12, 5)
bandit1 = Bandit(550, 270, 'Bandit', 100, 8, 1)
bandit2 = Bandit(700, 270, 'Bandit', 100, 6, 1)

#? Holding bandits
bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)

#? Health Bars
knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)



#! Future Fighters
#?       x, y, name, max_hp, strength, potions
# archer = Archer(200, 260, 'Archer', 100, 8, 3)
# wizard = Wizard(200, 260, 'Wizard', 100, 14, 3)
# monk =   Monk(200, 260, 'Monk', 100, 12, 10)




#! WARNING
#! The game is RUNNING HERE
run = True
while run:

    clock.tick(fps)

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
    for bandit in bandit_list:
        bandit.update()
        bandit.draw(screen)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
