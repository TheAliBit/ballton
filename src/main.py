import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Ballton')

clock = pygame.time.Clock()

ball = pygame.image.load('ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (80, 80))
ball_rect = ball.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False
    speed = 10
    if keys[pygame.K_w]:
        if ball_rect.top > 0:
            ball_rect.y -= speed

    if keys[pygame.K_s]:
        if ball_rect.bottom < SCREEN_HEIGHT:
            ball_rect.y += speed

    if keys[pygame.K_a]:
        if ball_rect.left > 0:
            ball_rect.x -= speed

    if keys[pygame.K_d]:
        if ball_rect.right < SCREEN_WIDTH:
            ball_rect.x += speed


    screen.fill((0, 0, 0))
    screen.blit(ball, (ball_rect))
    pygame.display.update()
    clock.tick(60)
