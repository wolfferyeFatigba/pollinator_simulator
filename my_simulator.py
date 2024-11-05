import pygame
import random
import math

pygame.init()
width = 800
height = 400
screen = pygame.display.set_mode((width, height))
bckgr = pygame.image.load('bckgr_simu2.jpeg')

# Load and resize bee sprites
sprites = [
    pygame.transform.scale(pygame.image.load('bee_1.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_2.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_3.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_4.png').convert_alpha(), (50, 50)),
    pygame.transform.scale(pygame.image.load('bee_5.png').convert_alpha(), (50, 50)),
]

air_pollution = 0
wind_speed = 0
bee_speed = 5
water_pollution = 0
soil_pollution = 0
light_pollution = 0
noise_pollution = 0
particles = pygame.sprite.Group()
#flowers = pygame.sprite.Group()

class Bee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.sprites = sprites
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.base_speed = bee_speed
        self.speed = self.base_speed
        self.is_moving = True

    def update(self, target, light_pollution):
        # Alternate sprites
        self.current_sprite += 0.2
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]
        
        if light_pollution > 50:
            self.rect.x += random.choice([-1, 1]) * self.speed
            self.rect.y += random.choice([-1, 1]) * self.speed
        else:
            direction_x = target.rect.x - self.rect.x
            direction_y = target.rect.y - self.rect.y
            distance = math.hypot(direction_x, direction_y)
        
            if distance < 5:
                self.is_moving = False
                self.speed = 0
            elif self.is_moving:
            #bee movement
                if distance != 0:
                    move_x = int(self.speed * (direction_x / distance))
                    move_y = int(self.speed * (direction_y / distance))
                    self.rect.x += move_x
                    self.rect.y += move_y



class Particle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect(center=(x, y))
        # particle's random speed  
        self.vx = random.choice([-1, 1]) * random.uniform(0.5, 1.5)
        self.vy = random.choice([-1, 1]) * random.uniform(0.5, 1.5)

    def update(self):
        # Move the particle and bounce against the edges
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > width:
            self.vx *= -1
        if self.rect.top < 0 or self.rect.bottom > height:
            self.vy *= -1

class Flower(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("flower.jpeg").convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.image.set_colorkey((255, 255, 255))  # Rendre le blanc transparent
        self.rect = self.image.get_rect(center=(x, y))

flower = Flower(x = 400, y = 200)
flowers = pygame.sprite.Group()
flowers.add(flower)
# create particles and flowers
for _ in range(80):
    particle = Particle(random.randint(0, width), random.randint(0, height))
    particles.add(particle)

#for _ in range(1):
    #flower = Flower(random.randint(50, width - 50), random.randint(50, height - 50))
    #flowers.add(flower)

bee1 = Bee()
clock = pygame.time.Clock()

simulator = True
while simulator:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            simulator = False
        # Increase air pollution
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                air_pollution = min(100, air_pollution + 10)
            if event.key == pygame.K_w:
                water_pollution = min(100, water_pollution + 10)
            if event.key == pygame.K_s:
                soil_pollution = min(100, soil_pollution + 10)
            if event.key == pygame.K_l:
                light_pollution = min(100, light_pollution + 10)
            if event.key == pygame.K_n:
                noise_pollution = min(100, noise_pollution + 10)

    # Adjusting bee speed based on air pollution
    bee1.speed = max(1, bee1.base_speed - (air_pollution / 20))

    bee1.update(flower, light_pollution)
    # collisions
    if pygame.sprite.spritecollideany(bee1, particles):
        bee1.speed = max(1, bee1.speed - 0.8)
    if light_pollution > 50:
        bee1.rect.y += random.choice([-1, 1])
    if soil_pollution > 30:
        for flower in flowers:
            if bee1.rect.colliderect(flower.rect):
                bee1.rect.x -= 10
    if water_pollution > 50:
        bee1.speed = max(1, bee1.speed - 0.5)

    # draw elements
    screen.blit(bckgr, (0, 0))
    flowers.draw(screen)
    particles.update()  # Update particle position
    particles.draw(screen)
    #bee1.update()
    screen.blit(bee1.image, bee1.rect)

    # Drawing the gauges
    pygame.draw.rect(screen, (0, 0, 255), (50, 50, air_pollution * 2, 20))
    pygame.draw.rect(screen, (255, 255, 0), (50, 80, bee1.speed * 20, 20))
    pygame.draw.rect(screen,(128, 0, 125), (50, 170, light_pollution* 2, 20))

    font = pygame.font.Font(None, 24)
    text_pollution = font.render(f'Niveau de Pollution: {air_pollution}', True, (255, 255, 255))
    text_bee_speed = font.render(f'Vitesse de l\'Abeille: {bee1.speed:.1f}', True, (255, 255, 255))
    text_light = font.render(f'Niveau de pollution: {light_pollution}', True, (255, 255, 255))
    screen.blit(text_pollution, (50, 30))
    screen.blit(text_bee_speed, (50, 110))
    screen.blit(text_light, (50, 150))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
