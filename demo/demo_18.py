from py5 import *


def settings():
    size(1280, 720)


def setup():
    bild = load_image("./sprites/Run (1).png")
    image(bild, 100, 100)


run_sketch()