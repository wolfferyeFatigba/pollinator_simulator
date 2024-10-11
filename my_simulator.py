import pygame
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
bckgr = pygame.image.load('bckgr_simu2.jpeg')
screen.blit(bckgr, (0, 0))
pygame.display.flip()
simulator = True
while simulator :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulator = False
