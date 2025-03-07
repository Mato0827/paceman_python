import pygame
import sys
from draw_text import draw_text

def test_draw_text():
    pygame.init()
    
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("draw_text テスト")
    
    screen.fill((255, 255, 255))
    
    draw_text(screen, "Centered Text0", screen_width//2, screen_height//2, 50, (0, 0, 0), True)
    
    draw_text(screen, "Centered Text1", screen_width//2, screen_height//2, 50, (255, 0, 0), False)
    
    pygame.display.flip()
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                running = False

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    test_draw_text()

