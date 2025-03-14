from item_effect_off import item_effect_off

#エラー処理必要
#壁に当たった時の処理

def move_player_up():
    if key[pygame.K_UP] == True:
        pl_d = DIR_UP

        if maze[pl_y-1][pl_x] != WALL:
            pl_y -= 1
        
        else:
            if pl_col == COLOR_BROWN:
                snd_break_wall.play()
                maze[pl_y-1][pl_x] = ROAD
                pl_y -= 1
                item_effect_off()

def move_player_right():
    if key[pygame.K_RIGHT] == True:
        pl_d = DIR_RIGHT

        if maze[pl_y][pl_x+1] != WALL:
            pl_x += 1

        else:
            if pl_col == COLOR_BROWN:
                snd_break_wall.play()
                maze[pl_y+1][pl_x] = ROAD
                pl_y += 1
                item_effect_off()

def move_player_down():
    if key[pygame.K_DOWN] == True:
        pl_d = DIR_DOWN
        
        if maze[pl_y+1][pl_x] != WALL:
            pl_y += 1
        
        else:
            if pl_col == COLOR_BROWN:
                snd_break_wall.play()
                maze[pl_y+1][pl_x] = ROAD
                pl_y += 1
                item_effect_off()

def move_player_left():
    if key[pygame.K_LEFT] == True:
        pl_d = DIR_LEFT
        
        if maze[pl_y][pl_x-1] != WALL:
            pl_x -= 1
        
        else:
            if pl_col == COLOR_BROWN:
                snd_break_wall.play()
                maze[pl_y][pl_x-1] = ROAD
                pl_x -= 1
                item_effect_off()


def move_player(key):
    global pl_x,pl_y,pl_d

    if pl_fast == False:
        if tmr%2 == 0:
            return
    
    move_player_up()
    move_player_right()
    move_player_down()
    move_player_left()