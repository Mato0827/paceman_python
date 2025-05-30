from item_effect_off import item_effect_off
import declear_var as dv
import pygame

#エラー処理必要
#壁に当たった時の処理

def move_player_up(key):
    if key[pygame.K_UP] == True:
        dv.pl_d = dv.DIR_UP

        if dv.maze[dv.pl_y-1][dv.pl_x] != dv.WALL:
            dv.pl_y -= 1
        
        else:
            if dv.pl_col == dv.COLOR_BROWN:
                snd_break_wall.play()
                dv.maze[dv.pl_y-1][dv.pl_x] = dv.ROAD
                dv.pl_y -= 1
                item_effect_off()

def move_player_right(key):
    if key[pygame.K_RIGHT] == True:
        dv.pl_d = dv.DIR_RIGHT

        if dv.maze[dv.pl_y][dv.pl_x+1] != dv.WALL:
            dv.pl_x += 1

        else:
            if dv.pl_col == dv.COLOR_BROWN:
                snd_break_wall.play()
                dv.maze[dv.pl_y+1][dv.pl_x] = dv.ROAD
                dv.pl_y += 1
                item_effect_off()

def move_player_down(key):
    if key[pygame.K_DOWN] == True:
        dv.pl_d = dv.DIR_DOWN
        
        if dv.maze[dv.pl_y+1][dv.pl_x] != dv.WALL:
            dv.pl_y += 1
        
        else:
            if dv.pl_col == dv.COLOR_BROWN:
                snd_break_wall.play()
                dv.maze[dv.pl_y+1][dv.pl_x] = dv.ROAD
                dv.pl_y += 1
                item_effect_off()

def move_player_left(key):
    if key[pygame.K_LEFT] == True:
        dv.pl_d = dv.DIR_LEFT
        
        if dv.maze[dv.pl_y][dv.pl_x-1] != dv.WALL:
            dv.pl_x -= 1
        
        else:
            if dv.pl_col == dv.COLOR_BROWN:
                snd_break_wall.play()
                dv.maze[dv.pl_y][dv.pl_x-1] = dv.ROAD
                dv.pl_x -= 1
                item_effect_off()


def move_player(key):


    if dv.pl_fast == False:
        if dv.tmr%2 == 0:
            return
    
    move_player_up(key)
    move_player_right(key)
    move_player_down(key)
    move_player_left(key)