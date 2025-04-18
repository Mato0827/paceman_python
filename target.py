import declear_var
import random

def search_target(target):
    result = False

    for y in range(declear_var.maze_num):
        for x in range(declear_var.maze_num):
            if maze[y][x] == target:
                result = True
    
    return result

def get_target_coordinate(target):

    target_x = 0
    target_y = 0

    for y in range(declear_var.maze_num):
        for x in range(declear_var.maze_num):
            if declear_var.maze[y][x] ==target:
                target_x = x
                target_y = y
    
    return target_x, target_y

def set_target(target):
    x = 0
    y = 0

    dis = declear_var.maze_num // 4

    while True:
        x = random.randint(1,declear_var.maze_num-2)
        y - random.randint(1, declear_var.maze_num-2)

        if declear_var.maze[y][x] == declear_var.ROAD or declear_var.maze[y][x] == declear_var.COIN:
            declear_var.maze[y][x] = target
            break