import pygame
import random
from solver import board,board1,board2, solve, print_board
from copy import deepcopy

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
        self.rect = self.image.get_rect(topleft=(self.pos[1] * self.width, self.pos[0] * self.height))


    def create_cube(self):
        self.image.fill('white')
        pygame.draw.rect(self.image, 'black', [0, 0, self.width, self.height], 1)
        self.textSurface = self.font.render(self.num, 0, 'black')
        text_rect = self.textSurface.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.textSurface, text_rect)
        


    def update(self, num):
        self.create_cube(num)     
    
def get_board():

    boards = [board, board1, board2]
    current_board = random.choice(boards)
    solved_board = deepcopy(current_board)
    if solve(solved_board):
        return current_board, solved_board
    return current_board, None


def initialize_board(bo, screen):
    SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
    cubes = pygame.sprite.Group()
    for i in range(9):
        for j in range(9):
            cube = Cube((i,j), str(bo[i][j]), SCREEN_WIDTH//9, SCREEN_HEIGHT//9)
            cubes.add(cube)
    
    cubes.draw(screen)
    return cubes

def game_loop(screen, game_active, clock):
    bo = []
    solved_bo = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if game_active == False and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bo, solved_bo = get_board()
                    game_active = True
                    print_board(bo)
                    print('**************************')
                    print_board(solved_bo)
                    
        
        if game_active:
            screen.fill('black')
            initialize_board(bo, screen)
            
            # game_active = solve() == bo 

        else:
            screen.fill('green')
        ## Here we will add code to start a new board or reset the board

        pygame.display.update()
        clock.tick(60)

def main():
    # Initialize the game
    pygame.init()

    SCREEN_WIDTH = 540
    SCREEN_HEIGHT = 540

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Sudoku')
    clock = pygame.time.Clock()
    game_active = False

    # solved = solve(board)
    game_loop(screen, game_active, clock)

if __name__ == '__main__':
    main()