import pygame
import os
from aereo import Aereo

pygame.init()

WIDTH, HEIGHT = 500, 700
WHITE = (0,0,0)
VEL = 7


def carica_texture(immagini = []):
    immagini.append([])
    immagini.append([])
    
    immagini[0].append(pygame.image.load("SF01.png"))
    immagini[0].append(pygame.image.load("SF02.png"))
    immagini[0].append(pygame.image.load("SF04.png"))
    immagini[0].append(pygame.image.load("SF03.png"))
    
    immagini[1].append(pygame.image.load("SF01a_strip60.png"))
    immagini[1].append(pygame.image.load("SF02a_strip60.png"))
    immagini[1].append(pygame.image.load("SF04a_strip60.png"))
    immagini[1].append(pygame.image.load("SF03a_strip60.png"))

def Draw(aereo):
    screen.fill(WHITE)
    screen.blit(img_aereo, (aereoPri.x, aereoPri.y))
    pygame.display.update()

# aereo_x, aereo_y, dim_aereo_x, dim_aereo_y  = 150, 545, 100, 100
aereo_x, aereo_y, dim_aereo_x, dim_aereo_y  = 150, 545, 14400, 240
proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y = 50, 50, 800, 100
aereo_rect = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
effetti_rect = pygame.Rect(proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("AIR BATTLE")
# img_aereo = pygame.image.load("C:\\Users\\Matteo\\Desktop\\Pygame\\Videogioco\\Textures\\Navicelle\\Designs - Base\\PNGs\\Nairan - Torpedo Ship - Base.png")
img_effetti = pygame.image.load("Nairan - Torpedo Ship - Engine.png")
jet_texture = []
carica_texture(jet_texture)

img_aereo = pygame.transform.scale(jet_texture[1][0], (dim_aereo_x, dim_aereo_y))
img_effetti = pygame.transform.scale(img_effetti, (dim_proiettile_x, dim_proiettile_y))
aereoPri = pygame.Rect(aereo_x, aereo_y, dim_aereo_x, dim_aereo_y)
effettiPri = pygame.Rect(proiettile_x, proiettile_y, dim_proiettile_x, dim_proiettile_y)
aereo = Aereo(aereo_rect, img_aereo, img_effetti, screen)
tasto_lasciato = None



FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    spara = False
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    key_pressed = pygame.key.get_pressed()
    aereo.move(key_pressed)
    
    
    screen.fill(WHITE)
    aereo.draw(screen, key_pressed)
    pygame.display.update()
    

pygame.quit()



# carriata da glucozio (10 in pagella per lui obbligatorio)