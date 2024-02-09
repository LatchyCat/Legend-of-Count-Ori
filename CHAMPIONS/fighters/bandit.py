import pygame
import random
from fighters.damagetext import DamageText

#? Define Colours
red = (255, 0, 0)
green = (0, 255, 0)


clock = pygame.time.Clock()

class Bandit:
    def __init__(self, x, y, name, max_hp, strength, potions, damage_text_group):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.potions = potions
        self.alive = True
        self.damage_text_group = damage_text_group
        self.animation_list = []
        self.frame_index = 0
        self.action = 0 #? 0:idle, 1:attack, 2:hurt, 3:dead
        self.update_time = pygame.time.get_ticks()
        #Load Idle Images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'CHAMPIONS/images/{self.name}/Idle/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        #Load Attack Images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f'CHAMPIONS/images/{self.name}/Attack/{i}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            temp_list.append(img)
        self.animation_list.append(temp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


    def update(self):
        animation_cooldown = 100
        #Handle Animation
        #Update Image
        self.image = self.animation_list[self.action][self.frame_index]
        #Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # If animation runs out. Reset to the start
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()


    def idle(self):
        # Set variable to attack animation
        self.action = 0
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()



    def attack(self, target, font):
        # Attack enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        # Check if target has died
        if target.hp < 1:
            target.hp = 0
            target.alive = False
        #Damage Text
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red, font)
        self.damage_text_group.add(damage_text)

        # Set variable to attack animation
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def draw(self, screen):
        screen.blit(self.image, self.rect)
