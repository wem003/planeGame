# Simple pygame program

# Import and initialize the pygame library
import pygame
import time
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
pixelShift = 5
circleX = 250
circleY = 250
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (circleX, circleY), 75)

    circleX = circleX + pixelShift
    circleY = circleY + pixelShift

    # Flip the display
    pygame.display.flip()

    time.sleep(2)

# Done! Time to quit.
pygame.quit()