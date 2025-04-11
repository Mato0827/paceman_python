from collections import deque
#COLOR
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
#SOUND
snd_pacman_blue = None
snd_pacman_red = None
snd_pacman_yellow = None
snd_pacman_green = None
snd_pacman_brown = None
snd_player_attack = None
snd_player_damage = None
snd_break_wall = None
snd_arrive_goal = None
snd_get_coin = None
snd_get_item = None
#SIZE/FPS
SCREEN_SIZE = 900
FPS = 10
#DIRECTION
DIR_UP = 0
DIR_RIGHT = 1
DIR_DOWN = 2
DIR_LEFT = 3
#COLOR
COLOR_BLACK = 0
COLOR_BLUE = 1
COLOR_RED = 2
COLOR_YELLOW = 3
COLOR_GREEN = 4
COLOR_BROWN = 5
#GAME MANAGE
idx = 0
tmr = 0
course = 0
WALL = 0
ROAD = -1
GOAL = -2
ITEM = -3
COIN = -4
#PLAYER
pl_col = 0
pl_x = 0
pl_y = 0
pl_d = 0
pl_fast = False
pl_coin = 0
pl_item = [0]*6
pl_scope = 0
pl_muteki = 0
#ENEMY
emy_max = 0
emy_no = 0
emy_num_max = False
emy_time = 0
emy_f = [False]*emy_max
emy_col = [0]*emy_max
emy_x = [0]*emy_max
emy_y = [0]*emy_max
emy_d = [0]*emy_max
emy_s = [0]*emy_max
ENEMY_HIGH_SPEED = 2
ENEMY_NORMAL_SPEED = 4
ENEMY_LOW_SPEED = 6
#ITEM
item_use = False
item_time = 0
item_max = 0
item_generate_time = 0
#MAZE
goal_f = False
goal_generate_time = 0
#MAZE
maze_size = 60
maze_num = 17
maze = []
#BFS
q = deque()
dist = []