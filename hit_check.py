import declear_var as dv
import random
import pygame

pygame.mixer.init()


snd_player_attack = pygame.mixer.Sound("sound/player_attack.mp3")
snd_player_damage = pygame.mixer.Sound("sound/player_damage.mp3")
snd_get_coin = pygame.mixer.Sound("sound/get_coin.mp3")
snd_get_item = pygame.mixer.Sound("sound/get_item.mp3")

def hit_check():
    if dv.maze[dv.pl_y][dv.pl_x] == dv.COIN:
        snd_get_coin.play()
        dv.maze[dv.pl_y][dv.pl_x] = dv.ROAD
        dv.pl_coin += 1

        if dv.pl_coin >= 100:
            dv.pl_life += 1
            dv.pl_coin -= 100

    if dv.maze[dv.pl_y][dv.pl_x] == dv.ITEM:
        snd_get_item.play()
        dv.maze[dv.pl_y][dv.pl_x] = dv.ROAD

        dv.item = random.randint(1, 5)
        dv.pl_item[dv.item] += 1
    
    for n in range(dv.emy_max):
        if dv.emy_f[n] == False:
            continue
        
        if dv.emy_x[n] == dv.pl_x and dv.emy_y[n] == dv.pl_y:
            print(dv.pl_col)
            if dv.pl_col == dv.COLOR_RED:
                snd_player_attack.play()
                dv.emy_f[n] = False
            
            else:
            
                if dv.pl_muteki == 0:
                    snd_player_damage.play()
                    dv.pl_muteki = dv.FPS * 3
                    dv.pl_life -= 1
                    dv.emy_f[n] = False
        
        if dv.emy_col[n] == dv.COLOR_YELLOW and dv.maze[dv.emy_y[n]][dv.emy_x[n]] == dv.GOAL:
            dv.maze[dv.emy_y[n]][dv.emy_x[n]] = dv.ROAD
            goal_f = False
            goal_generate_time = dv.FPS * 15

        if dv.emy_col[n] == dv.COLOR_GREEN and dv.maze[dv.emy_y[n]][dv.emy_x[n]] == dv.COIN:
            dv.maze[dv.emy_y[n]][dv.emy_x[n]] = dv.ROAD

        if dv.emy_col[n] == dv.COLOR_BROWN and dv.maze[dv.emy_y[n]][dv.emy_x[n]] == dv.ITEM:
            dv.maze[dv.emy_y[n]][dv.emy_x[n]] = dv.ROAD
    
