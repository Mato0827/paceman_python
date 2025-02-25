import pygame
import sys
from load_img import img_road, img_wall, img_scope, img_player, img_enemy, img_goal, img_coin, img_item, img_arrow

def test_images_one_by_one():
    pygame.init()
    
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("画像読み込みテスト - 一枚ずつ表示")
    font = pygame.font.SysFont(None, 24)
    clock = pygame.time.Clock()
    
    images = []
    images.append(("road", img_road))
    images.append(("wall", img_wall))
    for idx, scope_img in enumerate(img_scope):
        images.append((f"scope_{idx}", scope_img))
    for idx, player_img in enumerate(img_player):
        images.append((f"player_{idx}", player_img))
    for idx, enemy_img in enumerate(img_enemy):
        images.append((f"enemy_{idx}", enemy_img))
    images.append(("goal", img_goal))
    images.append(("coin", img_coin))
    images.append(("item", img_item))
    images.append(("arrow", img_arrow))
    
    for label, image in images:
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False
                    
            screen.fill((50, 50, 50))
            
            rect = image.get_rect(center=(400, 300))
            screen.blit(image, rect)
            
            label_surface = font.render(label, True, (255, 255, 255))
            label_rect = label_surface.get_rect(midtop=(400, rect.bottom + 10))
            screen.blit(label_surface, label_rect)
            
            pygame.display.flip()
            clock.tick(30)
    
    pygame.time.wait(1000)
    pygame.quit()

if __name__ == "__main__":
    test_images_one_by_one()

