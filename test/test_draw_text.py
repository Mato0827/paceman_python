import pygame
import sys
from text_drawer import ../draw_text

def test_draw_text():
    pygame.init()
    
    screen_width, screen_height = 640, 480
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("draw_text テスト")
    
    screen.fill((255, 255, 255))
    
    draw_text(screen, "Centered Text", screen_width, screen_height, 50, (0, 0, 0), True)
    
    draw_text(screen, "Non-Centered Text", 10, 10, 30, (255, 0, 0), False)
    
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

