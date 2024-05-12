import pygame
import os

pygame.init()

WIDTH, HEIGHT = 500, 690
run = True
WHITE = (250,250,250)
aereo_x, aereo_y, dim_aereo_x, dim_aereo_y  = 150, 545, 100, 100
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 182, 500, 50, 50
FPS = 60
VEL = 5
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AIR BATTLE")
aereo = pygame.image.load("immagineAereo.png")
proiettile = pygame.image.load("proiettile.png")
aereo = pygame.transform.scale(aereo, (dim_aereo_x, dim_aereo_y))
proiettile = pygame.transform.scale(proiettile, (dim_proiettile_x, dim_proiettile_y))
aereo = pygame.transform.rotate(aereo, 278)
aereoPri = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
proiettilePri = pygame.Rect(proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y)

def MovimentoAereo(key_pressed, aereoPri, proiettilePri):
    if key_pressed[pygame.K_w] and aereoPri.y - VEL >= 0:
        aereoPri.y -= VEL
    if key_pressed[pygame.K_s] and aereoPri.y + VEL <= HEIGHT-100:
        aereoPri.y += VEL
    if key_pressed[pygame.K_a] and aereoPri.x - VEL >= 0:
        aereoPri.x -= VEL
    if key_pressed[pygame.K_d] and aereoPri.x + VEL <= WIDTH-100:
        aereoPri.x += VEL

def Draw(aereoPri, proiettilePri, spara):
    screen.fill(WHITE)
    screen.blit(aereo, (aereoPri.x, aereoPri.y))
    if spara:
        screen.blit(proiettile, (proiettilePri.x, proiettilePri.y))
    pygame.display.update()



while run:
    spara = False
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key_pressed = pygame.key.get_pressed()
    MovimentoAereo(key_pressed, aereoPri, proiettilePri)
    Draw(aereoPri, proiettilePri, spara)

pygame.quit()