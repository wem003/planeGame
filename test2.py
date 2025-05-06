import pygame


pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
clock = pygame.time.Clock()

while not done:
    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         done = True

    screen.fill((255, 255, 255))

    titleImage = pygame.image.load("./graphics/space_title.png").convert()

    screen.blit(titleImage, (0, 0))

    pygame.display.flip()
    clock.tick(60)