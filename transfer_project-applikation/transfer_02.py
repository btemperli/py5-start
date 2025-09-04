# ----------------------------
# Transfer-Aufgabe 02.
# Zufällige Formen
# Mögliche Musterlösung.
# Modul Projekt Applikation.
# ----------------------------
import py5
import random


def setup():
    py5.size(1280, 720)
    py5.background(38, 50, 56)

    for i in range(0, 50):
        xPos = random.randint(0, py5.width)
        yPos = random.randint(0, py5.height)
        starSize = random.randint(15, 150)
        star(xPos, yPos, starSize)


def star(xPos, yPos, l):
    r = random.randint(70, 240)
    g = random.randint(81, 98)
    b = random.randint(146, 181)

    py5.no_stroke()
    py5.fill(r, g, b)

    # oben
    py5.begin_shape()
    py5.vertex(xPos, yPos - l)
    py5.vertex(xPos + l / 10, yPos)
    py5.vertex(xPos - l / 10, yPos)
    py5.end_shape(py5.CLOSE)

    # unten
    py5.begin_shape()
    py5.vertex(xPos, yPos + l)
    py5.vertex(xPos + l / 10, yPos)
    py5.vertex(xPos - l / 10, yPos)
    py5.end_shape(py5.CLOSE)

    # links
    py5.begin_shape()
    py5.vertex(xPos + l, yPos)
    py5.vertex(xPos, yPos + l / 10)
    py5.vertex(xPos, yPos - l / 10)
    py5.end_shape(py5.CLOSE)

    # rechts
    py5.begin_shape()
    py5.vertex(xPos - l, yPos)
    py5.vertex(xPos, yPos + l / 10)
    py5.vertex(xPos, yPos - l / 10)
    py5.end_shape(py5.CLOSE)

    # kreis innen
    py5.fill(211, 47, 47)
    py5.circle(xPos, yPos, l / 5)


py5.run_sketch()
