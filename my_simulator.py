import pygame
pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
bckgr = pygame.image.load('bckgr_simu2.jpeg')

#screen.blit(bckgr, (0, 0))
sprites = [
    pygame.transform.scale(pygame.image.load('bee_1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_5.png').convert_alpha(), (50, 50)),
]

air_pollution = 0

class Bee(pygame.sprite.Sprite): #class to display bee sprite
    def __init__(self):
        super().__init__()
        self.sprites = sprites # accessprite list
        self.current_sprite = 0 # Actual sprite index
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 5
    def update(self):
        global air_pollution
        self.speed = max(1, 5 - air_pollution // 20)
    # change sprite position
        self.current_sprite += 0.2
        if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
        #bee moves
        self.rect.x += self.speed

        if self.rect.x > width:
             self.rect.x = 0
bee1 = Bee()
simulator = True
clock = pygame.time.Clock() #manage framerate
while simulator :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulator = False
            #ajust air pollution
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                  air_pollution = min(100, air_pollution + 10)
             elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                  air_pollution = max(100, air_pollution - 10)
    #draw background and sprite
    screen.blit(bckgr, (0, 0))
    bee1.update()

    screen.blit(bee1.image, bee1.rect)

    #display air pollution level
    font = pygame.font.Font(None, 36)
    text = font.render('Air Pollution: {air_pollution}', True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(220) 
pygame.quit()
