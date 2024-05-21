import pygame
from solver import board

class Cube(pygame.sprite.Sprite):
    
    def __init__(self, pos, num, width, height):
        super().__init__()
        self.font = pygame.font.SysFont("Arial", 24)
        self.pos = pos
        self.num = num
        self.width = width
        self.height = height 
        self.image = pygame.Surface((self.width, self.height))
        self.create_cube()
        self.rect = self.image.get_rect(topleft=(self.pos[0] * self.width, self.pos[1] * self.height))


    def create_cube(self):
        self.image.fill('white')
        pygame.draw.rect(self.image, 'black', [0, 0, self.width, self.height], 1)
        self.textSurface = self.font.render(self.num, 0, 'black')
        text_rect = self.textSurface.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.textSurface, text_rect)
        


    def update(self, num):
        self.create_cube(num)     



def game_loop(screen, game_active, clock, cubes):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if game_active:
            cubes.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

def main():
    # Initialize the game
    pygame.init()

    screen = pygame.display.set_mode((540,540))
    pygame.display.set_caption('Sudoku')
    clock = pygame.time.Clock()
    game_active = True

    

    cubes = pygame.sprite.Group()
    for i in range(9):
        for j in range(9):
            cube = Cube((i,j), str(board[i][j]), 540//9, 540//9)
            cubes.add(cube)
    


    game_loop(screen, game_active, clock, cubes)

if __name__ == '__main__':
    main()