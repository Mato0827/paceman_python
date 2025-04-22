import declear_var
import random

ENEMY_HIGH_SPEED = 2
ENEMY_NORMAL_SPEED = 4
ENEMY_LOW_SPEED = 6

def move_enemy():
    for n in range(declear_var.emy_max):
        if declear_var.emy_f[n] == False:
            continue
    
        if declear_var.tmr%declear_var.emy_s[n] != 0:
            continue

def init_enemy():
    declear_var.emy_f = [False]*declear_var.emy_max
    declear_var.emy_col = [0]*declear_var.emy_max
    declear_var.emy_x = [0]*declear_var.emy_max
    declear_var.emy_y = [0]*declear_var.emy_max
    declear_var.emy_d = [0]*declear_var.emy_max
    declear_var.emy_s = [0]*declear_var.emy_max
    print("init_enemy")
    print(declear_var.emy_no)
    print(declear_var.emy_col)
    print(declear_var.emy_x)
    print(declear_var.emy_y)
    print(declear_var.emy_s)

def set_enemy(x,y,s,col):
    print("set_enemy")
    print(declear_var.emy_no)
    print(col)
    print(declear_var.emy_col)
    print(declear_var.emy_x)
    print(declear_var.emy_y)
    print(declear_var.emy_s)
    while True:
        if declear_var.emy_f[declear_var.emy_no] == False:
            declear_var.emy_f[declear_var.emy_no] = True
            declear_var.emy_col[declear_var.emy_no] = col
            declear_var.emy_x[declear_var.emy_no] = x
            declear_var.emy_y[declear_var.emy_no] = y
            declear_var.emy_s[declear_var.emy_no] = s
            break
        declear_var.emy_no = (declear_var.emy_no+1) % emy_max

def bring_enemy():
    print("set_enemy1")
    print(declear_var.emy_no)
    print(declear_var.emy_col)
    print(declear_var.emy_x)
    print(declear_var.emy_y)
    print(declear_var.emy_s)
    while True:
        declear_var.emy_x = random.randint(1,declear_var.maze_num-2)
        declear_var.emy_y = random.randint(1,declear_var.maze_num-2)

        if declear_var.maze[declear_var.emy_y][declear_var.emy_x] == declear_var.ROAD or declear_var.maze[declear_var.emy_y][declear_var.emy_x] == declear_var.COIN:
            if (declear_var.emy_x < declear_var.pl_x-5 or declear_var.pl_x+5 < declear_var.emy_x) and (declear_var.emy_y < declear_var.pl_y-5 or declear_var.pl_y+5 < declear_var.emy_y):
                break
    
    declear_var.emy_col = random.randint(declear_var.COLOR_BLACK, declear_var.COLOR_BROWN)
    print("bring_enemy")
    print(declear_var.emy_no)
    print(declear_var.emy_col)
    print(declear_var.emy_x)
    print(declear_var.emy_y)
    print(declear_var.emy_s)
    if declear_var.emy_col == declear_var.COLOR_BLACK:
        declear_var.emy_s = ENEMY_HIGH_SPEED
    elif declear_var.emy_col == declear_var.COLOR_RED:
        declear_var.emy_s = ENEMY_NORMAL_SPEED
    else:
        declear_var.emy_s = declear_var.ENEMY_LOW_SPEED
    
    set_enemy(declear_var.emy_x, declear_var.emy_y, declear_var.emy_s, declear_var.emy_col)
    