#迷路の描画
import declear_var
import road_image as ri
import pygame
from draw_text import draw_img

COIN = -4
WALL = 0
GOAL = -2
ROAD = -1
ITEM = -3

def print_player_details(sc):
    draw_text(sc,"COURSE  :  "+str(course),declear_var.SCREEN_SIZE+70,750,35,declear_var.BLACK,False)
    draw_text(sc,"COIN       :   "+str(pl_coin),declear_var.SCREEN_SIZE+70,790,35,declear_var.BLACK,False)
    draw_text(sc,"LIFE        :   "+str(pl_life),declear_var.SCREEN_SIZE+70,830,35,declear_var.BLACK,False)

def print_enemy_details(sc):
    count_enemy_color = [0]*6
    for n in range(declear_var.emy_max):
        if declear_var.emy_f[n] == False:
            continue
        print(declear_var.emy_col[n])
        count_enemy_color[declear_var.emy_col[n]] += 1
    
    for i in range(6):

        ri.img_rz = pygame.transform.rotozoom(ri.img_enemy[i*4],0,0.8)
        sc.blit(ri.img_tz,[declear_var.SCREEN_SIZE+70,50+50*i])

        draw_text(sc,"X  "+str(count_enemy_color[i]),declear_var.SCREEN_SIZE+150,60+50*i,35,BLACK,False)

def print_paceman_details(sc):
    for i in range(i,6):
        ri.img_rz = pygame.transform.rotozoom(ri.img_player[i*2],-90,0.8)
        sc.blit(ri.img_rz,[declear_var.SCREEN_SIZE+110,370+50*i])

        draw_text(sc,"["+str(i)+"]:",declear_var.SCREEN_SIZE+50,380+50*i,35,BLACK,False)
        draw_text(sc,"X   "+str(declear_var.pl_item[i]),declear_var.SCREEN_SIZE+180,380+50*i,35,BLACK,False)
    
    
def draw_maze(sc):
    for y in range(-7,8):
        for x in range(-7,8):
            X = (x+7) * declear_var.maze_size
            Y = (y+7) * declear_var.maze_size
            mx = declear_var.pl_x + x 
            my = declear_var.pl_y + y 

            if 0 <= mx < declear_var.maze_num and 0 <= my < declear_var.maze_num:
                if declear_var.maze[my][mx] == WALL:
                    sc.blit(ri.img_wall,[X,Y])
                if declear_var.maze[my][mx] == ROAD:
                    sc.blit(ri.img_road,[X,Y])
                
                if declear_var.maze[my][mx] == GOAL:
                    sc.blit(ri.img_goal,[X,Y])
                
                if declear_var.maze[my][mx] == COIN:
                    sc.blit(ri.img_coin,[X,Y])
                
                if declear_var.maze[my][mx] == ITEM:
                    sc.blit(ri.img_item,[X,Y])
                
                for n in range(declear_var.emy_max):
                    if declear_var.emy_f[n] == False:
                        continue
                    if declear_var.emy_x[n] == mx and emy_y[n] == my:
                        sc.blit(img_enemy[declear_var.emy_col[n]*4 + declear_var.emy_d[n]],[X,Y])
            if x == 0 and y == 0:
                if declear_var.pl_muteki%2 == 0:
                    ri.img_rz = pygame.transform.rotozoom(ri.img_player[declear_var.pl_col*2+declear_var.tmr%2],declear_var.pl_d*(-90),1.0)

                    if declear_var.item_use == True and item_time<FPS*3:
                        if declear_var.tmr%2 == 0:
                            sc.blit(ri.img_rz,[X,Y])
                    else:
                        sc.blit(ri.img_rz,[X,Y])
                
                if declear_var.pl_col == declear_var.COLOR_GREEN and goal_f == True:

                    a = calc_angle_of_goal_from_player()

                    ri.img_rz = pygame.transform.rotozoom(ri.img_arrow,-a,1.0)
                    draw_img(sc,img_rz,X+maze_size/2,Y-maze_size)

    draw_img(sc,ri.img_scope[declear_var.pl_scope],declear_var.SCREEN_SIZE/2,declear_var.SCREEN_SIZE/2)

    pygame.draw.rect(sc,declear_var.WHITE,[declear_var.SCREEN_SIZE+30,30,240,340])
    pygame.draw.rect(sc,declear_var.WHITE,[declear_var.SCREEN_SIZE+30,400,240,290])
    pygame.draw.rect(sc,declear_var.WHITE,[declear_var.SCREEN_SIZE+30,720,240,150])

    print_enemy_details(sc)
    print_paceman_details(sc)
    print_player_details(sc)
                    