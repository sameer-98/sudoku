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
        self.textSurface = self.font.render(str(self.num), 0, 'black')
        text_rect = self.textSurface.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.textSurface, text_rect)
        
    def set_num(self, num):
        self.num = num

    def update(self):
        self.create_cube()
        self.rect = self.image.get_rect(topleft=(self.pos[1] * self.width, self.pos[0] * self.height))
    
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
            cube = Cube((i,j), bo[i][j], SCREEN_WIDTH//9, SCREEN_HEIGHT//9)
            cubes.add(cube)
    
    return cubes

#Checks if we are using cube that has a zero
def check_pos(bo, cube):
    x,y = cube.pos
    if bo[x][y] == 0: return (x,y)

    return None

def game_loop(screen, game_active, clock):
    bo = []
    original_bo = []
    solved_bo = []
    cubes = pygame.sprite.Group()
    clicked_cube = ()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if game_active == False and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bo, solved_bo = get_board()
                    original_bo = deepcopy(bo)
                    cubes = initialize_board(bo, screen)
                    game_active = True

            if game_active == True and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                #select the clicked cube
                cube = [c for c in cubes if c.rect.collidepoint(mouse_pos)][0]
                clicked_cube = check_pos(original_bo, cube)
                #disable mouse click on other boxes

            if clicked_cube and event.type == pygame.KEYDOWN:
                #Need to allow back space and integers
                key = 0
                cube = [c for c in cubes if c.pos == clicked_cube][0]
                if event.key == pygame.K_BACKSPACE:
                    print('Hello')
                    cube.set_num(key)
                else:
                    try:
                        key = int(chr(event.key))
                        cube.set_num(key)
                    except ValueError:
                        print('Enter a Number')
                
                bo[clicked_cube[0]][clicked_cube[1]] = key
                

        if game_active:
            cubes.draw(screen)
            cubes.update()

            game_active = solved_bo != bo

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