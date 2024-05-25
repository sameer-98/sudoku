import pygame
import random
from solver import board,board1,board2, solve, print_board
from copy import deepcopy

class Cube(pygame.sprite.Sprite):
    
    def __init__(self, pos, num, width, height, font, offset):
        super().__init__()
        self.font = font
        self.pos = pos
        self.offset = offset
        self.num = num
        self.width = width
        self.height = height 
        self.fill = 'white'
        self.image = pygame.Surface((self.width, self.height))
        self.create_cube()
        self.rect = self.image.get_rect(topleft=(self.pos[1] * self.width + self.offset[0], self.pos[0] * self.height + self.offset[1]))
        self.is_selected = False


    def create_cube(self):
        self.image.fill(self.fill)
        pygame.draw.rect(self.image, 'black', [0, 0, self.width, self.height], 1)
        self.textSurface = self.font.render(str(self.num), 0, 'black')
        text_rect = self.textSurface.get_rect(center=(self.width/2, self.height/2))
        self.image.blit(self.textSurface, text_rect)
        
    def set_num(self, num):
        self.num = num
        if num != 0:
            self.fill = 'darkslategray1'
        else:
            self.fill = 'white'

    def select_cube(self):
        if self.is_selected:
            pygame.draw.rect(self.image, 'blue', [0, 0, self.width, self.height], 5)

    def update(self):
        self.create_cube()
        self.rect = self.image.get_rect(topleft=(self.pos[1] * self.width + self.offset[0], self.pos[0] * self.height + self.offset[1]))
        self.select_cube()
    

def display_score(start_time, font, screen):
    current_time = (pygame.time.get_ticks() // 1000) - start_time
    score_surf = font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center=(300,650))
    # screen.blit(score_surf, score_rect)
    return current_time, score_surf, score_rect

def get_board():

    boards = [board, board1, board2]
    current_board = random.choice(boards)
    solved_board = deepcopy(current_board)
    if solve(solved_board):
        return current_board, solved_board
    return current_board, None


def initialize_board(bo, font, board_width, board_height,offset):
    board_width -= 100
    board_height -= 100
    
    cubes = pygame.sprite.Group()
    for i in range(9):
        for j in range(9):
            cube = Cube((i,j), bo[i][j], board_width//9, board_height//9, font, offset)
            cubes.add(cube)
    
    return cubes

#Checks if we are using cube that has a zero
def check_pos(bo, cube):
    x,y = cube.pos
    if bo[x][y] == 0: return (x,y)

    return None

def display_text(surface, text, pos, font, color):
    collection = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    x,y = pos
    for lines in collection:
        for words in lines:
            word_surface = font.render(words, True, color)
            word_width , word_height = word_surface.get_size()
            if x + word_width >= 540:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x,y))
            x += word_width + space
        x = pos[0]
        y += word_height

def game_loop(screen, game_active, clock, font):
    bo = []
    original_bo = []
    solved_bo = []
    cubes = pygame.sprite.Group()
    clicked_cube = ()
    disabled = False
    win_width, win_height = screen.get_size()
    game_board_width, game_board_height = win_width - 100, win_height - 100
    board_x = (win_width - game_board_width) // 2
    board_y = (win_height - game_board_height ) // 2
    offset = (board_x, board_y)
    start_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if game_active == False and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bo, solved_bo = get_board()
                    original_bo = deepcopy(bo)
                    cubes = initialize_board(bo, font, game_board_width, game_board_height , offset)
                    game_active = True
                    start_time = pygame.time.get_ticks()//1000

            if game_active == True and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if disabled: continue
                #select the clicked cube
                cube = [c for c in cubes if c.rect.collidepoint(mouse_pos)][0]
                clicked_cube = check_pos(original_bo, cube)
                if clicked_cube: 
                    cube.is_selected = True
                    disabled = True
                #disable mouse click on other boxes

            if clicked_cube and event.type == pygame.KEYDOWN:
                #Need to allow back space and integers
                key = 0
                cube = [c for c in cubes if c.pos == clicked_cube][0]
                
                if event.key == pygame.K_BACKSPACE:
                    cube.set_num(key)
                else:
                    try:
                        key = int(chr(event.key))
                        if cube.is_selected: cube.set_num(key)
                    except ValueError:
                        pass
                
                cube.is_selected = False
                disabled = False
                
                bo[clicked_cube[0]][clicked_cube[1]] = key

            if game_active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    for cube in cubes:
                        i, j = cube.pos
                        cube.set_num(solved_bo[i][j])
                        game_active = False
                    #go to end screen and display the answer        

        if game_active:
            screen.fill((94,129,162))
            time_taken, score_surf, score_rect = display_score(start_time, font, screen)
            cubes.draw(screen)
            cubes.update()

            screen.blit(score_surf, score_rect)

            game_active = solved_bo != bo
            


        else:
            screen.fill((94,129,162))
            if len(bo) == 0:
                text = 'Welcome to a game of sudoku\nPress Space to start and Enter to get the solved board'
                pos = (60,60)
            else:
               cubes.draw(screen)
               cubes.update()
               text = 'Press Space to restart'
               pos = (300, 600)

            display_text(screen, text, pos, font, 'purple')
        ## Here we will add code to start a new board or reset the board

        pygame.display.update()
        clock.tick(60)

def main():
    # Initialize the game
    pygame.init()

    SCREEN_WIDTH = 740
    SCREEN_HEIGHT = 740

    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    pygame.display.set_caption('Sudoku')
    clock = pygame.time.Clock()
    game_active = False
    font = pygame.font.SysFont("Inkfree", 50)

    # solved = solve(board)
    game_loop(screen, game_active, clock, font)

if __name__ == '__main__':
    main()