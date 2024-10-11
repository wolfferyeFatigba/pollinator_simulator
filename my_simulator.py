import pygame
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
simulator = True
while simulator :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulator = False

pygame.display.flip()