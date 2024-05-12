import pygame
import os

pygame.init()

WIDTH, HEIGHT = 500, 690
run = True
WHITE = (250,250,250)
aereo_x = 150
aereo_y = 545
dim_aereo_x = 100
dim_aereo_y = 100

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR BATTLE")
aereo = pygame.image.load("immagineAereo.png")
aereo = pygame.transform.scale(aereo, (dim_aereo_x, dim_aereo_y))
aereo = pygame.transform.rotate(aereo, 278)

while run:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(aereo, (aereo_x, aereo_y))
    pygame.display.update()


pygame.quit()