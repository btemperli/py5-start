from py5 import *


def settings():
    size(600, 600)


def setup():
    background(55, 71, 79)
    no_stroke()
    fill(194, 24, 91)
    triangle(300, 100, 500, 500, 100, 500)

    fill(55, 71, 79)
    circle(300, 400, 200)

    fill(194, 24, 91)
    rect_mode(CENTER)
    rect(300, 400, 100, 100)


run_sketch()
