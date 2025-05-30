import declear_var as dv
import math

def calc_angle_of_goal_from_player():
    dv.x_pl = dv.pl_x * dv.maze_size + dv.maze_size/2
    dv.y_pl = dv.pl_y * dv.maze_size + dv.maze_size/2

    dv.x_goal = 0
    dv.y_goal = 0
    for y in range(dv.maze_num):
        for x in range(dv.maze_num):
            if dv.maze[y][x] == dv.GOAL:
                dv.x_goal = x * dv.maze_size + dv.maze_size/2
                dv.y_goal = y * dv.maze_size + dv.maze_size/2
    
    x_dis = dv.x_goal - dv.x_pl
    y_dis = dv.y_goal - dv.y_pl

    ang = math.degrees(math.atan2(y_dis, x_dis))

    return ang