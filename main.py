import pygame

pygame.init()

#set up the display

width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong")

FPS = 60

white = (255, 255, 255)
black = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT =  20, 100
ball_radius = 7

class Paddle:
    COLOR = white
    VEL = 4

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up=True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

class Ball:
    max_vel = 5
    color = white

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.max_vel
        self.y_vel = 0

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x,self.y),self.radius, )

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

def draw(win, paddles, ball):
    win.fill(black)

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, height, height//20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, white, (width//2 - 5, i, 10, height//20))

    ball.draw(win)
    pygame.display.update()

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >=0:
       left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= height:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >=0:
       right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= height:
        right_paddle.move(up=False)

def main():
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(width - 10 - PADDLE_WIDTH, height//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(width // 2, height // 2, ball_radius)

    while run:
        clock.tick(FPS)
        draw(screen, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle,right_paddle)

    pygame.quit()

if __name__ == '__main__':
    main()

