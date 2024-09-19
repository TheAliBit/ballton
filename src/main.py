import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ballton')

clock = pygame.time.Clock()

ball = pygame.image.load('ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (80, 80))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(ball, (0, 0))
    pygame.display.update()
    clock.tick(60)
