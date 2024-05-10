import pygame
from sys import exit

#Initialize the pygame modules
pygame.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)