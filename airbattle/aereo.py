import pygame
import math
from funzioni import distanza_punti

VEL = 7
HEIGHT = 690
WIDTH = 500

class Aereo:
    def __init__(self, rect, img, img_effetti, screen, time = 0):
        self.rect = rect
        self.img = img
        self.screen = screen
        self.time = time
        self.effetti = []
        effetti_width = img_effetti.get_width() // 8
        effetti_height = img_effetti.get_height()
        for i in range(8):
            startx = i * effetti_width
            img_part = img_effetti.subsurface((startx, 0, effetti_width, effetti_height))
            self.effetti.append(img_part)
        self.centro_aereo = pygame.math.Vector2(self.rect.x + self.rect.width, self.rect.y + self.rect.height)
        
    def move(self, key, pos):
        if key[pygame.K_w] and self.rect.y - VEL >= 0:
            self.rect.y -= VEL  
        if key[pygame.K_s] and self.rect.y + VEL <= HEIGHT-100:
            self.rect.y += VEL
        if key[pygame.K_a] and self.rect.x - VEL >= 0:
            self.rect.x -= VEL
        if key[pygame.K_d] and self.rect.x + VEL <= WIDTH-100:
            self.rect.x += VEL
        # ipo = distanza_punti(self.centro_aereo, pos)
        # catx = distanza_punti()
        
    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))
        screen.blit(self.effetti[int(self.time) % 8], (self.rect.x, self.rect.y + 2))
        self.time += 0.2