import pgzrun
from random import randint
TITLE = "flappy_ball"
WIDTH = 800
HEIGHT = 600
gravity = 2000

class Ball:
    def __init__(self,initialx,initialy):
        self.x = initialx
        self.y = initialy
        self.vx = 200
        self.vy = 0
        self.radius = 50
    
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,"blue")

ball1 = Ball (50,100)

def draw():
    screen.clear()
    ball1.draw()

def update(dt):
    uy = ball1.vy
    ball1.vy = ball1.vy + gravity * dt
    ball1.y = ball1.y + (uy+ball1.vy) * 0.5 * dt
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = - ball1.vy * 0.9
    
    ball1.x = ball1.x + ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius :
        ball1.vx = - ball1.vx

def on_key_down(key):
    if key == keys.SPACE:
        ball1.vy = -500




pgzrun.go()