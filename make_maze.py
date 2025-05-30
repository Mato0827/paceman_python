import random
import declear_var
#迷路の初期化
def init_maze():

    declear_var.maze_num += 2

    declear_var.maze = []
    for y in range(declear_var.maze_num):
        declear_var.maze.append([0]*declear_var.maze_num)
#迷路の自動生成
def make_maze():
    init_maze()

    XP = [0,1,0,-1]
    YP = [-1,0,1,0]

    for x in range(declear_var.maze_num):
        declear_var.maze[0][x] = declear_var.WALL
        declear_var.maze[declear_var.maze_num-1][x] = declear_var.WALL

    for y in range(declear_var.maze_num-1):
        declear_var.maze[y][0] = declear_var.WALL
        declear_var.maze[y][declear_var.maze_num-1] = declear_var.WALL
    
    for y in range(1,declear_var.maze_num-1):
        for x in range(1,declear_var.maze_num-1):
            declear_var.maze[y][x] = declear_var.ROAD
    

    for y in range(2,declear_var.maze_num-2,2):
        for x in range(2,declear_var.maze_num-2,2):
            d = random.randint(0,3)
            if x > 2:
                d = random.randint(0,2)
            declear_var.maze[y+YP[d]][x+XP[d]] = declear_var.WALL