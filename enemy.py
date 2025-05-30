import declear_var
import random
from target import search_target,get_target_coordinate
from BFS import *

ENEMY_HIGH_SPEED = 2
ENEMY_NORMAL_SPEED = 4
ENEMY_LOW_SPEED = 6

def move_enemy():
    for n in range(declear_var.emy_max):
        if declear_var.emy_f[n] == False:
            continue
    
        if declear_var.tmr%declear_var.emy_s[n] != 0:
            continue
        if declear_var.emy_col[n] == declear_var.COLOR_BLACK:
            # 移動方向：プレイヤーの方向
            if declear_var.emy_y[n] > declear_var.pl_y:
                declear_var.emy_dir = declear_var.DIR_UP    # 上方向
            if declear_var.emy_y[n] < declear_var.pl_y:
                declear_var.emy_dir = declear_var.DIR_DOWN  # 下方向
            if declear_var.emy_x[n] < declear_var.pl_x:
                declear_var.emy_dir = declear_var.DIR_RIGHT # 右方向
            if declear_var.emy_x[n] > declear_var.pl_x:
                declear_var.emy_dir = declear_var.DIR_LEFT  # 左方向

            # 移動できたかどうか -> 移動可能ならば移動(Trueを返す)
            move_ok = move_check_to_move(declear_var.emy_dir, n)

            # 移動できていない場合 -> ランダム
            if move_ok == False:
                while True:
                    declear_var.emy_dir = random.randint(declear_var.DIR_UP, declear_var.DIR_LEFT)  # 移動方向：ランダム選択
                    move_ok = move_check_to_move(declear_var.emy_dir, n)    # 移動できたかどうか -> 移動可能ならば移動(Trueを返す)

                    # 移動できるまで繰り返す
                    if move_ok == True:
                        break

        # 敵の色：青、赤、黄、緑、茶 -> 移動方向：目標へ移動(追尾)
        else:
            # 青、赤 -> プレイヤーを追尾
            if declear_var.emy_col[n] == declear_var.COLOR_BLUE or declear_var.emy_col[n] == declear_var.COLOR_RED:
                BFS(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)                         # 幅優先探索法でプレイヤーの位置までの最短ルートを算出
                next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)   # 幅優先探索法で求めたルートから次の移動方向を取得
                
            # 黄 -> ゴールへ移動 or プレイヤーを追尾
            elif declear_var.emy_col[n] == declear_var.COLOR_YELLOW:
                # ゴールが存在する：ゴールへ移動
                if search_target(declear_var.GOAL) == True:
                    goal_x, goal_y = get_target_coordinate(declear_var.GOAL)                    # ゴールのx,y座標を取得
                    BFS(declear_var.emy_x[n], declear_var.emy_y[n], goal_x, goal_y)                         # 幅優先探索法でゴールの位置までの最短ルートを算出
                    next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], goal_x, goal_y)   # 幅優先探索法で求めたルートから次の移動方向を取得
                # ゴールが存在しない：プレイヤーを追尾
                else:
                    BFS(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)                         # 幅優先探索法でプレイヤーの位置までの最短ルートを算出
                    next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)   # 幅優先探索法で求めたルートから次の移動方向を取得

            # 緑：コイン
            elif declear_var.emy_col[n] == declear_var.COLOR_GREEN:
                # コインが存在する：コインへ移動
                if search_target(declear_var.COIN) == True:
                    coin_x, coin_y = get_target_coordinate(declear_var.COIN)                    # コインのx,y座標を取得
                    BFS(declear_var.emy_x[n], declear_var.emy_y[n], coin_x, coin_y)                         # 幅優先探索法でコインの位置までの最短ルートを算出
                    next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], coin_x, coin_y)   # 幅優先探索法で求めたルートから次の移動方向を取得
                # コインが存在しない：プレイヤーを追尾
                else:
                    BFS(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)                         # 幅優先探索法でプレイヤーの位置までの最短ルートを算出
                    next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)   # 幅優先探索法で求めたルートから次の移動方向を取得
            
            # 茶：アイテム
            elif declear_var.emy_col[n] == declear_var.COLOR_BROWN:
                # アイテムが存在する：アイテムへ移動
                if search_target(declear_var.ITEM) == True:
                    item_x, item_y = get_target_coordinate(declear_var.ITEM)                    # アイテムのx,y座標を取得
                    BFS(declear_var.emy_x[n], declear_var.emy_y[n], item_x, item_y)                         # 幅優先探索法でコインの位置までの最短ルートを算出
                    next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], item_x, item_y)   # 幅優先探索法で求めたルートから次の移動方向を取得
                # アイテムが存在しない：プレイヤーを追尾
                else:
                    BFS(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)                         # 幅優先探索法でプレイヤーの位置までの最短ルートを算出
                    next_dir = next_direction(declear_var.emy_x[n], declear_var.emy_y[n], declear_var.pl_x, declear_var.pl_y)   # 幅優先探索法で求めたルートから次の移動方向を取得

            # 移動
            if next_dir == declear_var.DIR_UP:      # 上方向
                declear_var.emy_y[n] -= 1
                declear_var.emy_d[n] = declear_var.DIR_UP
            elif next_dir == declear_var.DIR_RIGHT: # 右方向
                declear_var.emy_x[n] += 1
                declear_var.emy_d[n] = declear_var.DIR_RIGHT
            elif next_dir == declear_var.DIR_DOWN:  # 下方向
                declear_var.emy_y[n] += 1
                declear_var.emy_d[n] = declear_var.DIR_DOWN
            elif next_dir == declear_var.DIR_LEFT:  # 左方向
                declear_var.emy_x[n] -= 1
                declear_var.emy_d[n] = declear_var.DIR_LEFT
def init_enemy():
    declear_var.emy_f = [False]*declear_var.emy_max
    declear_var.emy_col = [0]*declear_var.emy_max
    declear_var.emy_x = [0]*declear_var.emy_max
    declear_var.emy_y = [0]*declear_var.emy_max
    declear_var.emy_d = [0]*declear_var.emy_max
    declear_var.emy_s = [0]*declear_var.emy_max


def set_enemy(x,y,s,col):

    while True:
        if declear_var.emy_f[declear_var.emy_no] == False:
            declear_var.emy_f[declear_var.emy_no] = True
            declear_var.emy_col[declear_var.emy_no] = col
            declear_var.emy_x[declear_var.emy_no] = x
            declear_var.emy_y[declear_var.emy_no] = y
            declear_var.emy_s[declear_var.emy_no] = s
            break
        declear_var.emy_no = (declear_var.emy_no+1) % declear_var.emy_max

def bring_enemy():

    while True:
        emy_x = random.randint(1,declear_var.maze_num-2)
        emy_y = random.randint(1,declear_var.maze_num-2)

        if declear_var.maze[emy_y][emy_x] == declear_var.ROAD or declear_var.maze[emy_y][emy_x] == declear_var.COIN:
            if (emy_x < declear_var.pl_x-5 or declear_var.pl_x+5 < emy_x) and (emy_y < declear_var.pl_y-5 or declear_var.pl_y+5 < emy_y):
                break
    
    emy_col = random.randint(declear_var.COLOR_BLACK, declear_var.COLOR_BROWN)

    if emy_col == declear_var.COLOR_BLACK:
        emy_s = ENEMY_HIGH_SPEED
    elif emy_col == declear_var.COLOR_RED:
        emy_s = ENEMY_NORMAL_SPEED
    else:
        emy_s = declear_var.ENEMY_LOW_SPEED
    
    set_enemy(emy_x, emy_y, emy_s, emy_col)

def move_check_to_move(emy_dir, no):
    move_ok = False

    if emy_dir == declear_var.DIR_UP and declear_var.maze[declear_var.emy_y[no]-1][declear_var.emy_x[no]] != 0:
        declear_var.emy_d[no] = declear_var.DIR_UP
        declear_var.emy_y[no] -= 1
        move_ok = True
    
    if emy_dir == declear_var.DIR_RIGHT and declear_var.maze[declear_var.emy_y[no]][declear_var.emy_x[no]] != 0:
        declear_var.emy_d[no] = declear_var.DIR_RIGHT
        declear_var.emy_x[no] += 1
        move_ok = True
    
    if emy_dir == declear_var.DIR_DOWN and declear_var.maze[declear_var.emy_y[no]][declear_var.emy_x[no]-1] != 0:
        declear_var.emy_d[no] = declear_var.DIR_DOWN
        declear_var.emy_y[no] += 1
        move_ok = True
    
    if emy_dir == declear_var.DIR_LEFT and declear_var.maze[declear_var.emy_y[no]][declear_var.emy_x[no]-1] != 0:
        declear_var.emy_d[no] = declear_var.DIR_LEFT
        declear_var.emy_x[no] -= 1
        move_ok = True
    
    return move_ok

def enemy_num_max_check():

    for n in range(declear_var.emy_max):

        if declear_var.emy_f[n] == False:
            declear_var.emy_num_max = False
            declear_var.emy_time = declear_var.FPS * 20
            break

def check_enemy_to_generate():

    if declear_var.emy_num_max == True:
        enemy_num_max_check()
    
    elif declear_var.emy_num_max == False and declear_var.emy_time > 0:
        declear_var.emy_time -= 1
    
    elif declear_var.emy_num_max == False and declear_var.emy_time == 0:
        bring_enemy()
        declear_var.emy_num_max = True

    