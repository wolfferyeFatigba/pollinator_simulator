import pygame
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))

bckgr = pygame.image.load('bckgr_simu2.jpeg')
screen.blit(bckgr, (0, 0))

class Bee(pygame.sprite.Sprite): #class to display bee sprite
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface((50, 50))
        self.image.fill((251, 4, 123))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)

bee1 = Bee()
simulator = True
clock = pygame.time.Clock() #manage framerate
while simulator :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulator = False
    #draw background and sprite
    screen.blit(bckgr, (0, 0))
    screen.blit(bee1.image, bee1.rect)
    pygame.display.flip()
    clock.tick(60) 
pygame.quit()
