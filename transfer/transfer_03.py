# ----------------------------
# Transfer-Aufgabe 03.
# Updown Animation.
#
# Lösungsvorschlag.
#
# Modul Programmieren.
# Modul Projekt Applikation.
# ----------------------------
import py5

yPos = 50
offset = 5


def setup():
    py5.size(600, 600)


def draw():
    global yPos
    global offset

    print(yPos)
    py5.background(255, 255, 255)

    py5.ellipse(py5.width / 2, yPos, 100, 100)

    if yPos > py5.height - 50 or yPos < 50:
        offset = offset * -1

    yPos = yPos + offset


py5.run_sketch()
