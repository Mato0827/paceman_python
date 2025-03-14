import pygame
from pygame.locals import *  # これにより、K_UP を直接使えるようになります

def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("pygame.K_UP のサンプル")

    # pygame.K_UP の値を確認（整数）
    print("pygame.K_UP の値:", pygame.K_UP)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # KEYDOWN イベントで上矢印キーかどうかを判定
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    print("上矢印キーが押されました！")
                    
    pygame.quit()

if __name__ == "__main__":
    main()