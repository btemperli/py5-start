# ----------------------------
# Transfer-Aufgabe 01.
# Interaktiver Kreis.
#
# Lösungsvorschlag.
#
# Modul Programmieren.
# Modul Projekt Applikation.
# ----------------------------
import py5


def setup():
    py5.size(600, 600)


def draw():
    helligkeit = py5.mouse_y / 2.35
    print(helligkeit)
    py5.background(helligkeit, helligkeit, helligkeit)
    py5.ellipse(300, 300, py5.mouse_x, py5.mouse_x)


py5.run_sketch()
