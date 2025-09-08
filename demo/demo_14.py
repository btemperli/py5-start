from py5 import *

abstand = 16


def settings():
    size(600, 600)


def setup():
    background(255, 255, 255)


def draw():
    global abstand

    for k in range(0, 5):
        ellipse(300, 300, 400 - abstand, 400)
        abstand = abstand * 2
        if abstand >= 400:
            abstand = 20


run_sketch()
