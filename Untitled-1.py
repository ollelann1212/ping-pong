from pygame import *
from random import *
from time import time as timer


speed_x = 3
speed_y = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def updateL(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 350:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 350:
            self.rect.y += self.speed

window = display.set_mode((700,500))
display.set_caption('Ping pong')
background = transform.scale(image.load('space.jpg'), (700, 500))

ball = GameSprite('ball.png', 350, 250, 66, 59, 5)
pong1 = Player('pong.png', 650, 200, 50, 150, 4)
pong2 = Player('pong.png', 30, 200, 50, 150, 4)

font.init()
font2 = font.SysFont('Arial', 24)
pong1_win = font2.render('ПРАВАЯ РАКЕТКА ВЫИГРАЛА', 1, (255,255,255))
pong2_win = font2.render('ЛЕВАЯ РАКЕТКА ВЫИГРАЛА', 1, (255,255,255))

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

game = True
clock = time.Clock()
FPS = 60
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False    
    if game == True:
        ball.rect.x += speed_x
        ball.rect.y += speed_y

    if ball.rect.y > 450 or ball.rect.y < 0:
        speed_y *= -1
    
    if sprite.collide_rect(pong1, ball) or sprite.collide_rect(pong2, ball):
        speed_x *= -1
    if ball.rect.x < -1:
        window.blit(pong1_win, (200, 250))

    if ball.rect.x > 701:
        window.blit(pong2_win, (200, 250))
    
    if ball.rect.x < -1 or ball.rect.x > 701:
        time.delay(1000)
        ball.rect.x = 350
        ball.rect.y = 250

    ball.reset()
    pong1.reset()
    pong2.reset()
    pong1.updateR()
    pong2.updateL()
    display.update()
    clock.tick(FPS)