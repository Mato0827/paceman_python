import pygame
import sys
from collections import deque
from declear_var import *  
from draw_maze import *

def create_dummy_surface(color, size=(maze_size, maze_size)):
    surf = pygame.Surface(size)
    surf.fill(color)
    return surf

img_wall = create_dummy_surface((128, 128, 128))   
img_road = create_dummy_surface((200, 200, 200))     
img_goal = create_dummy_surface((0, 255, 0))          
img_coin = create_dummy_surface((255, 215, 0))         
img_item = create_dummy_surface((0, 0, 255))           

img_enemy = [create_dummy_surface(((i*40)%256, (j*60)%256, 200))
             for i in range(6) for j in range(4)]
img_player = [create_dummy_surface(((i*40)%256, (j*80)%256, 150))
              for i in range(6) for j in range(2)]
img_arrow = create_dummy_surface((255, 0, 0))
img_scope = [create_dummy_surface((0, 255, 255)) for _ in range(3)]
pl_scope = 0
def draw_text(sc, txt, x, y, siz, col, center):
    fnt = pygame.font.Font(None, siz)
    sur = fnt.render(txt, True, col)
    if center:
        x = x - sur.get_width() / 2
        y = y - sur.get_height() / 2
    sc.blit(sur, (x, y))

def draw_img(sc, img, x, y):
    x = x - img.get_width() / 2
    y = y - img.get_height() / 2
    sc.blit(img, (x, y))

def calc_angle_of_goal_from_player():
        return 45             

def test_draw_maze():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE + 300, SCREEN_SIZE))
    pygame.display.set_caption("draw_maze テスト")
    clock = pygame.time.Clock()
    
    global tmr
    tmr = 0  
    
    
    global maze
    maze = [[ROAD for _ in range(maze_num)] for _ in range(maze_num)]
    for i in range(maze_num):
        maze[0][i] = WALL
        maze[maze_num-1][i] = WALL
        maze[i][0] = WALL
        maze[i][maze_num-1] = WALL
        maze[maze_num-2][maze_num-2] = GOAL
        maze[5][5] = COIN
        maze[10][3] = ITEM

    
    global pl_x, pl_y
    pl_x, pl_y = maze_num // 2, maze_num // 2

    
    global emy_max, emy_f, emy_x, emy_y, emy_col, emy_d
    emy_max = 3
    emy_f = [True, True, True]
    emy_x = [3, 10, 7]
    emy_y = [4, 8, 7]
    emy_col = [0, 1, 2]
    emy_d = [0, 1, 2]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        tmr += 1
        screen.fill((0, 0, 0))
        draw_maze(screen)
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    test_draw_maze()