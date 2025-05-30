import declear_var as dv
from target import set_target
import pygame
from item_effect_off import item_effect_off

snd_pacman_blue = pygame.mixer.Sound("sound/pacman_blue.mp3")
snd_pacman_red = pygame.mixer.Sound("sound/pacman_red.mp3")
snd_pacman_yellow = pygame.mixer.Sound("sound/pacman_yellow.mp3")
snd_pacman_green = pygame.mixer.Sound("sound/pacman_green.mp3")
snd_pacman_brown = pygame.mixer.Sound("sound/pacman_brown.mp3")


def use_item(key):

    if key[pygame.K_1] == True and dv.pl_item[dv.COLOR_BLUE] > 0:
        snd_pacman_blue.play()
        item_effect_off()
        dv.pl_item[dv.COLOR_BLUE] -= 1
        dv.pl_col = dv.COLOR_BLUE
        dv.pl_fast = True
        dv.item_use = True
        dv.item_time = dv.FPS * 18
    
    if key[pygame.K_2] == True and dv.pl_item[dv.COLOR_RED] > 0:
        snd_pacman_red.play()
        item_effect_off()
        dv.pl_item[dv.COLOR_RED] -= 1
        dv.pl_col = dv.COLOR_RED
        dv.item_use = True
        dv.item_time = dv.FPS *8
    
    if key[pygame.K_3] == True and dv.pl_item[dv.COLOR_YELLOW] > 0:
        snd_pacman_yellow.play()
        item_effect_off()
        dv.pl_item[dv.COLOR_YELLOW] -= 1
        dv.pl_col = dv.COLOR_YELLOW
        dv.pl_scope = 1
        dv.item_use = True
        dv.item_time = dv.FPS * 13
    
    if key[pygame.K_5] == True and dv.pl_item[dv.COLOR_BROWN] > 0:
        snd_pacman_brown.play()
        item_effect_off()
        dv.pl_item[dv.COLOR_BROWN] -= 1
        dv.pl_col = dv.COLOR_BROWN
        dv.item_use = True
        dv.item_time = dv.FPS *33


def check_item_to_generate():

    count_item = 0
    for y in range(dv.maze_num):
        for x in range(dv.maze_num):
            if dv.maze[y][x] == dv.ITEM:
                count_item += 1
    
    if count_item < dv.item_max and dv.item_generate_time:
        dv.item_generate_time -= 1
    
    elif count_item < dv.item_max and dv.item_generate_time == 0:
        set_target(dv.ITEM)
        dv.item_generate_time = FPS * 15

def check_goal_to_generate():

    if dv.goal_f == False and dv.goal_generate_time > 0:
        dv.goal_generate_time -= 1
    
    elif dv.goal_f == False and dv.goal_generate_time == 0:
        set_target(dv.GOAL)
        dv.goal_f = True