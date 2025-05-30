import declear_var
from collections import deque
def init_dist():
    global dist
    dist = []
    for y in range(declear_var.maze_num):
        dist.append([0]*declear_var.maze_num)

def set_dist():
    init_dist()

    for y in range(declear_var.maze_num):
        for x in range(declear_var.maze_num):
            if declear_var.maze[y][x] == declear_var.WALL:
                dist[y][x] = declear_var.WALL
            else:
                dist[y][x] = declear_var.ROAD

def BFS(start_x,start_y,end_x,end_y):

    set_dist()

    dist_num = 1

    dy = (1,0,-1,0)
    dx = (0,1,0,-1)

    q = deque()
    q.append((start_x,start_y))

    dist[start_y][start_x] = dist_num

    target_search = False

    target_search = False

    while len(q)>0:
        now_pos = q.popleft()
        x,y = now_pos

        dist_num += 1

        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]

            if (nx<0 or nx>=declear_var.maze_num or ny<0 or ny>=declear_var.maze_num): continue

            if (dist[ny][nx] >= declear_var.WALL): continue

            if nx == end_x and ny == end_y:

                dist[ny][nx] = dist_num
                target_search = True
                break
            
            dist[ny][nx] = dist_num

            q.append((nx,ny))
        
        if target_search == True:
            break

def next_direction(start_x, start_y, end_x, end_y):
    dist_x = end_x
    dist_y = end_y
    dist_num = dist[end_y][end_x]

    next_dir = 0

    while True:

        dist_num -= 1


        if dist[dist_y-1][dist_x] == dist_num:
            dist_y -= 1
            next_dir = declear_var.DIR_DOWN

        elif dist[dist_y][dist_x+1] == dist_num:
            dist_x += 1
            next_dir = declear_var.DIR_LEFT

        elif dist[dist_y+1][dist_x] == dist_num:
            dist_y += 1
            next_dir = declear_var.DIR_UP
        
        elif dist[dist_y][dist_x-1] == dist_num:
            dist_x -= 1
            next_dir = declear_var.DIR_RIGHT
        
        if dist_x == start_x and dist_y == start_y:
            break
    
    return next_dir