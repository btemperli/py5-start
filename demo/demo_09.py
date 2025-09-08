from py5 import *


def settings():
    size(600, 600)


def setup():
    background(55, 71, 79)


def draw():
    xPos = 130
    yPos = 300
    text_size(64)

    # Schatten
    fill(38, 50, 56)
    text("Hello World", xPos - 4, yPos - 4)

    # Haupttext
    fill(236, 64, 122)
    text("Hello World", xPos, yPos)


run_sketch()
