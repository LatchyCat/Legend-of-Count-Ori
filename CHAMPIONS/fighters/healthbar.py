import pygame

#? Define Colours
red = (255, 0, 0)
green = (0, 255, 0)

class HealthBar:
    def __init__(self, x, y, hp, max_hp, color=(255, 0, 0)):  # Default color is red
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        self.color = color

    def draw(self, screen):
        #Update with new health
        self.hp = self.hp
        #Calculate health ratio
        ratio = self.hp / self.max_hp

        # Draw the health bar
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))
