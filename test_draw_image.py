import pygame
import sys
from draw_text import draw_img

def test_draw_img():
    pygame.init()
    
    screen_width, screen_height = 640, 640
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("draw_img テスト")
    
    screen.fill((255, 255, 255))
    
    try:
        img = pygame.image.load("./image/enemy_0.png") 
    except Exception as e: 
         print("画像の読み込みに失敗しました:", e)
         pygame.quit() 
         sys.exit()
    draw_img(screen,img,screen_width/2,screen_height/2)
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    test_draw_img()
