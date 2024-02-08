import pygame

class HealthBar:
    def __init__(self, x, y, hp, max_hp, color=(255, 0, 0)):  # Default color is red
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
        self.color = color

    def draw(self, screen):
        # Calculate the width of the health bar based on the current HP
        bar_width = int(150 * (self.hp / self.max_hp))
        # Draw the health bar
        pygame.draw.rect(screen, self.color, (self.x, self.y, 150, 20))
