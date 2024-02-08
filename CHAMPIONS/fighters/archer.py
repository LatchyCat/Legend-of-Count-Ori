import pygame


class Archer:
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.tick.get_ticks()
        for x in range(8):
            img = pygame.image.load(f'CHAMPIONS/images/{self.name}/Idle/{x}.png')
            img = pygame.transform.scale(img, (img.get_width() * 3, img.get_height() * 3))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)



    def update(self):
        animation_cooldown = 100
        #Handle Animation
        #Update Image
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.get_ticks()
            self.frame_index += 1
        # If animation runs out. Reset to the start
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0



    def draw(self, screen):
        screen.blit(self.image, self.rect)
