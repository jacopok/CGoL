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

#class Alive:
    

#class Dead:
    

pygame.init()
winstyle = 0
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
main_dir = os.path.split(os.path.abspath(__file__))[0]


def draw_grid():
    Grid = [[0 for i in range(dimx)] for j in range(dimy)]
    for i in range(dimx):
        for j in range(dimy):
            if Grid[i][j] == 0: #  Works with "i" going from 0 to 47; 48-64 is "out of order". No idea. 
                square = pygame.Rect(10*i, 10*j, 10, 10)
                screen.blit(load_image("Borders.png"), square)

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
    draw_grid()
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
