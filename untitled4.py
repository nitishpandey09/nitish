# Importing the library
import pygame

# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((400,300))

# Initialing Color
color = (255,240,0)

# Drawing Rectangle
pygame.draw.rect(surface, color, pygame.Rect(250, 150, 40, 40))
pygame.display.flip()


