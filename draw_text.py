import pygame
#文字の描画
def draw_text(sc,txt,x,y,siz,col,center):
    fnt = pygame.font.Font(None,siz)
    sur = fnt.render(txt,True,col)

    if center == True:
        x = x - sur.get_width()/2
        y = y - sur.get_height()/2
    
    sc.blit(sur,[x,y])

#画像の描画
def draw_img(sc,img,x,y):

    x = x - img.get_width()/2
    y = y - img.get_height()/2

    sc.blit(img,[x,y])