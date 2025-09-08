from py5 import *
import py5


def settings():
    size(600, 600)


def setup():
    background(255, 255, 255)
    fill(216, 27, 96)
    no_stroke()
    rect(150, 150, 300, 300, 30)


def draw():
    stroke(255, 255, 255)
    stroke_weight(12)


def key_pressed():
    if py5.key == CODED:

        if py5.key_code == UP:
            triangle(300, 200, 400, 400, 200, 400)
        if py5.key_code == DOWN:
            triangle(200, 200, 400, 200, 300, 400)
        if py5.key_code == LEFT:
            triangle(200, 300, 400, 200, 400, 400)
        if py5.key_code == RIGHT:
            triangle(200, 200, 400, 300, 200, 400)


def key_released():
    fill(216, 27, 96)
    no_stroke()
    rect(150, 150, 300, 300, 30)


run_sketch()
