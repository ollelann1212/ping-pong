from pygame import *
from random import *
from time import time as timer


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
        if keys_pressed[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
    def updateR(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 700:
            self.rect.y += self.speed

window = display.set_mode((700,500))
display.set_caption('Ping pong')
background = transform.scale(image.load('space.jpg'), (700, 500))

ball = GameSprite('ball.png', 350, 250, 66, 59, 50)
pong1 = Player('pong.png', 650, 200, 50, 150, 4)
pong2 = Player('pong.png', 30, 200, 50, 150, 4)

font.init()
font2 = font.SysFont('Arial', 24)

mixer.init()
#mixer.music.load('space.ogg')
#mixer.music.play()

game = True
clock = time.Clock()
FPS = 144
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False    
         
    window.blit(background,(0,0))
    ball.reset()
    pong1.reset()
    pong2.reset()
    pong1.updateR()
    pong2.updateL()
    keys_pressed = key.get_pressed()
    display.update()
    clock.tick(FPS)