from py5 import *
from zusatz import kreuz


def settings():
    size(600, 600)


def setup():
    kreuz(300, 300, 100)
    kreuz(100, 50, 10)
    kreuz(500, 150, 20)


run_sketch()