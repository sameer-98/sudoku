import pygame
from sys import exit

#Initialize the pygame modules
pygame.init()


screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Sudoku')
clock = pygame.time.Clock()
game_active = True


class Cube(pygame.sprite.Sprite):

    font = pygame.font.SysFont("Arial", 24)

    def __init__(self, width, height, num):
        super().__init__()
        self.width = width
        self.height = height
        self.image = pygame.Surface((width, height))
        self.create_cube(num)
        self.rect = pygame.draw.rect(self.image, 'black', [0, 0, width, height], 1)

    def create_cube(self, num):
        self.image.fill('white')
        self.textSurface = self.font.render(num, 0, 'black')
        W = self.textSurface.get_width()
        H = self.textSurface.get_height()
        self.image.blit(self.textSurface, [self.width/2 - W/2, self.height/2 - H/2])
        

    def update(self, num):
        self.create_cube(num)

class Grid(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        

     

    def update(self):  
        pass

cubes = pygame.sprite.Group()

cube = Cube(100,100, '9')
cubes.add(cube)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if game_active:
        cubes.draw(screen)
    
    pygame.display.update()
    clock.tick(60)