import random, os.path
import pygame
from pygame.locals import *
import pygame.gfxdraw


#see if we can load more than standard BMP
#if not pygame.image.get_extended():
#    raise SystemExit("Sorry, extended image module required")

dimx = 64
dimy = 48

# Set the display mode
SCREENRECT = Rect(0, 0, (10*dimx), (10*dimy))

def update(Grid):
    for i in range(1, dimx-1):
        for j in range(1, dimy-1):
            updatexy(Grid, i, j)

def updatexy(Grid, x, y):
    s = Grid[x+1][y] + Grid[x+1][y+1] + Grid[x][y+1] + Grid[x-1][y+1] + Grid[x-1][y] + Grid[x-1][y-1] + Grid[x][y-1] + Grid[x+1][y-1]
    if s <= 1:
        Grid[x][y] = 0
    elif s >= 4:
        Grid[x][y] = 0
    elif s == 3:
        Grid[x][y] = 1

pygame.init()
winstyle = 0
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
main_dir = os.path.split(os.path.abspath(__file__))[0]


def draw_grid(Grid):
    for i in range(dimx):
        for j in range(dimy):
            if Grid[i][j] == 0:
                square = pygame.Rect(10*i, 10*j, 10, 10)
                screen.blit(load_image("Borders.png"), square)
            if Grid[i][j] == 1:
                square = pygame.Rect(10*i, 10*j, 10, 10)
                screen.blit(load_image("Black.png"), square)

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file).convert()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

def main():
    Grid = [[0 for j in range(dimy)] for i in range(dimx)]
    Grid[20][20] = 1
    Grid[21][20] = 1
    Grid[22][20] = 1
    Grid[21][21] = 1
    draw_grid(Grid)
    while 1:
        update(Grid)
    try:
        while 1:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                    break
            pygame.display.flip()
    finally:
        pygame.quit()

if __name__ == '__main__': main()
