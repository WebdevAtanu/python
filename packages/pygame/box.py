import pygame
import sys

# Initialize pygame
pygame.init()

# Create window
screen = pygame.display.set_mode((800, 600))

# Window title
pygame.display.set_caption("My First Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Game loop
running = True

while running:

    # Fill background
    screen.fill(WHITE)

    # Draw rectangle
    pygame.draw.rect(screen, BLUE, (300, 200, 200, 100))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update screen
    pygame.display.update()

pygame.quit()
sys.exit()

