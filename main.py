import pygame
from draw_text import draw_text
import declear_var
from item_effect_off import item_effect_off
from make_maze import make_maze
from enemy import init_enemy,bring_enemy
import sys
import random
def init_game():
    global maze_num, course
    global pl_life, pl_item, pl_coin, pl_muteki

    declear_var.maze_num = 17

    declear_var.course = 0

    declear_var.pl_life = 2
    declear_var.pl_item = [2]*6
    declear_var.pl_coin = 0
    declear_var.pl_muteki = 0

    item_effect_off()
def init_game_place():
    global pl_x, pl_y
    global emy_d, emy_x, emy_y, emy_max, emy_num_max, emy_time
    global item_n, item_max, item_generate_time
    global goal_f

    declear_var.emy_max = declear_var.maze_num // 5
    declear_var.emy_num_max = False
    declear_var.emy_time = declear_var.FPS * 20
    init_enemy()

    declear_var.item_max = declear_var.maze_num // 5
    declear_var.item_generate_time = declear_var.FPS * 60

    while True:
        declear_var.pl_x = random.randint(1,declear_var.maze_num-2)
        declear_var.pl_y = random.randint(1,declear_var.maze_num-2)
        if declear_var.maze[declear_var.pl_y][declear_var.pl_x] == declear_var.ROAD:
            break
    
    for i in range(declear_var.maze_num // 10):
        bring_enemy()
    
    set_target(GOAL)
    goal_f = True

    for n in range(declear_var.maze_num // 10):
        set_target(ITEM)
    
    for y in range(declear_var.maze_num):
        for x in range(declear_var.maze_num):
            if declear_var.maze[y][x] == declear_var.ROAD:
                declear_var.maze[y][x] = declear_var.COIN

def init_sound():
    snd_pacman_blue = pygame.mixer.Sound("sound/pacman_blue.mp3")
    snd_pacman_red = pygame.mixer.Sound("sound/pacman_red.mp3")
    snd_pacman_yellow = pygame.mixer.Sound("sound/pacman_yellow.mp3")
    snd_pacman_green = pygame.mixer.Sound("sound/pacman_green.mp3")
    snd_pacman_brown = pygame.mixer.Sound("sound/pacman_brown.mp3")
    snd_player_attack = pygame.mixer.Sound("sound/player_attack.mp3")
    snd_player_damage = pygame.mixer.Sound("sound/player_damage.mp3")
    snd_break_wall = pygame.mixer.Sound("sound/break_wall.mp3")
    snd_arrive_goal = pygame.mixer.Sound("sound/arrive_goal.mp3")
    snd_get_coin = pygame.mixer.Sound("sound/get_coin.mp3")
    snd_get_item = pygame.mixer.Sound("sound/get_item.mp3")

def main():
    global idx, tmr, course
    global snd_pacman_blue, snd_pacman_red, snd_pacman_yellow, snd_pacman_green, snd_pacman_brown
    global snd_player_attack, snd_player_damage, snd_break_wall
    global snd_arrive_goal, snd_get_coin, snd_get_item
    global pl_col, pl_muteki
    global item_use, item_time

    pygame.init()
    pygame.display.set_caption("PAC-MAN")
    
    screen = pygame.display.set_mode((declear_var.SCREEN_SIZE+300,declear_var.SCREEN_SIZE))
    clock = pygame.time.Clock()

    init_sound()

    while True:
        declear_var.tmr = declear_var.tmr + 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill(declear_var.BLACK)
        key = pygame.key.get_pressed()

        if declear_var.idx == 0:

            if declear_var.tmr == 1:
                pygame.mixer.music.load("music/Stellar_Wind-Unicorn_Heads.mp3")
                pygame.mixer.music.play(-1)

                init_game()
                declear_var.idx = 1
                declear_var.tmr = 0
            print("draw text")
            draw_text(screen,"PUSH [ SPACE ] TO START",(declear_var.SCREEN_SIZE+300)/2,declear_var.SCREEN_SIZE/2,80,declear_var.BLACK,True)
            print("draw text")
        elif declear_var.idx == 1:

            if declear_var.tmr == 1:
                declear_var.course += 1
                make_maze()
                init_game_place()
            
            else:
                move_player(key)
                move_enemy()
                use_item(key)
                hit_check()

                check_enemy_to_generate()
                check_goal_to_generate()
                check_item_to_generate()

                if item_use == True:
                    item_time -= 1

                    if item_time == 0:
                        item_effect_off()
                
                if pl_muteki > 0:
                    pl_muteki -= 1
                
                if pl_life <= 0:
                    declear_var.idx = 2
                    declear_var.tmr = 0
                
                if declear_var.maze[declear_var.pl_y][declear_var.pl_x] == GOAL:
                    snd_arrive_goal.play()
                    declear_var.tmr = 0
        
        elif declear_var.idx == 2:
            draw_text(screen,"GAME OVER",(declear_var.SCREEN_SIZE+300)/2,declear_var.SCREEN_SIZE/2,100,declear_var.RED,True)
            if declear_var.tmr == declear_var.FPS * 3:
                declear_var.idx = 0
                declear_var.tmr = 0
        
        if declear_var.idx == 1 and declear_var.tmr > 0:
            draw_maze(screen)
        
        pygame.display.update()
        clock.tick(declear_var.FPS)

if __name__ == '__main__':
    main()