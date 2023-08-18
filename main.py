import pygame
import sys

pygame.init()

#set up the display

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)

def draw(win):
    win.fill(black)
    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == '__main__':
    main()

