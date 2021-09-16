from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character = load_image('character.png')

x=0
y=0
z=0
k=0
while True:
    while x<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,90)
        x+=2
        delay(0.01)
        k=0
    while y<600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(750,y)
        y+=2
        delay(0.01)
        x=0
    while z<800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(800-z,510)
        z+=2
        delay(0.01)
        y=0
    while k<600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(30,600-k)
        k+=2
        delay(0.01)
        z=0
