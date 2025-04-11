#迷路の描画
import declear_var

def print_player_details(sc):
    draw_text(sc,"COURSE  :  "+str(course),declear_var.SCREEN_SIZE+70,750,35,declear_var.BLACK,False)
    draw_text(sc,"COIN       :   "+str(pl_coin),declear_var.SCREEN_SIZE+70,790,35,declear_var.BLACK,False)
    draw_text(sc,"LIFE        :   "+str(pl_life),declear_var.SCREEN_SIZE+70,830,35,BLACK,False)

def print_enemy_details(sc):
    count_enemy_color = [0]*6
    for n in range(emy_max):
        if emy_f[n] == False:
            continue
        count_enemy_color[emy_col[n]] += 1
    
    for i in range(6):

        img_rz = pygame.transform.rotozoom(img_enemy[i*4],0,0.8)
        sc.blit(img_tz,[declear_var.SCREEN_SIZE+70,50+50*i])

        draw_text(sc,"X  "+str(count_enemy_color[i]),declear_var.SCREEN_SIZE+150,60+50*i,35,BLACK,False)

def print_paceman_details(sc):
    for i in range(i,6):
        img_rz = pygame.transform.rotozoom(img_player[i*2],-90,0.8)
        sc.blit(img_rz,[declear_var.SCREEN_SIZE+110,370+50*i])

        draw_text(sc,"["+str(i)+"]:",declear_var.SCREEN_SIZE+50,380+50*i,35,BLACK,False)
        draw_text(sc,"X   "+str(pl_item[i]),declear_var.SCREEN_SIZE+180,380+50*i,35,BLACK,False)
    
    
def draw_maze(sc):
    for y in range(-7,8):
        for x in range(-7,8):
            X = (x+7) * declear_var.maze_size
            Y = (y+7) * declear_var.maze_size
            mx = declear_var.pl_x + x 
            my = declear_var.pl_y + y 

            if 0 <= mx < declear_var.maze_num and 0 <= my < declear_var.maze_num:
                if declear_var.maze[my][mx] == WALL:
                    sc.blit(img_wall,[X,Y])
                if declear_var.maze[my][mx] == ROAD:
                    sc.blit(img_road,[X,Y])
                
                if declear_var.maze[my][mx] == GOAL:
                    sc.blit(img_goal,[X,Y])
                
                if declear_var.maze[my][mx] == COIN:
                    sc.blit(img_coin,[X,Y])
                
                if declear_var.maze[my][mx] == ITEM:
                    sc.blit(img_item,[X,Y])
                
                for n in range(emy_max):
                    if emy_f[n] == False:
                        continue
                    if emy_x[n] == mx and emy_y[n] == my:
                        sc.blit(img_enemy[emy_col[n]*4 + emy_d[n]],[X,Y])
            if x == 0 and y == 0:
                if pl_muteki%2 == 0:
                    img_rz = pygame.transform.rotozoom(img_player[pl_col*2+tmr%2],pl_d*(-90),1.0)

                    if item_use == True and item_time<FPS*3:
                        if tmr%2 == 0:
                            sc.blit(img_rz,[X,Y])
                    else:
                        sc.blit(img_rz,[X,Y])
                
                if pl_col == COLOR_GREEN and goal_f == True:

                    a = calc_angle_of_goal_from_player()

                    img_rz = pygame.transform.rotozoom(img_arrow,-a,1.0)
                    draw_img(sc,img_rz,X+maze_size/2,Y-maze_size)

    draw_img(sc,img_scope[pl_scope],SCREEN_SIZE/2,SCREEN_SIZE/2)

    pygame.draw.rect(sc,WHITE,[SCREEN_SIZE+30,30,240,340])
    pygame.draw.rect(sc,WHITE,[SCREEN_SIZE+30,400,240,290])
    pygame.draw.rect(sc,WHITE,[SCREEN_SIZE+30,720,240,150])

    print_enemy_details(sc)
    print_paceman_details(sc)
    print_player_details(sc)
                    