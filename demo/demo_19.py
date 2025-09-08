from py5 import *


def settings():
    size(1280, 720)


def setup():
    bilder = []
    for i in range(0, 8):
        bilder.append(load_image("./sprites/Run (" + str(i + 1) + ").png"))

    image(bilder[0], 20, 100)
    image(bilder[1], 420, 100)
    image(bilder[2], 820, 100)


run_sketch()