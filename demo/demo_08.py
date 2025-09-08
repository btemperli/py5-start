from py5 import *


def settings():
    size(600, 600)


def setup():
    fill(0, 121, 107)
    begin_shape()
    vertex(400, 100)
    vertex(500, 200)
    vertex(200, 500)
    vertex(100, 200)
    end_shape(CLOSE)


run_sketch()
