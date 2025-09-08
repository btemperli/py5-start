# ----------------------------
# Transfer-Aufgabe 04.
# Random Walker.
#
# Lösungsvorschlag.
#
# Modul Projekt Applikation.
# ----------------------------

from py5 import *
import py5

gridLength = 8
startCoord = [50, 50]


def settings():
    size(816, 846)


def setup():
    f = create_font("Courier New", 16, True)
    text_font(f)
    text_align(CENTER)

    frame_rate(24)

    background(255, 255, 255)
    stroke(200, 200, 200)

    for y in range(1, 102):
        for x in range(1, 102):
            xPos = x * gridLength
            yPos = y * gridLength
            point(xPos, yPos)


def draw():
    global startCoord

    # Zielkoordinaten ermitteln
    zielCoord = getZielCoord(startCoord)

    # Linie zeichnen
    stroke(244, 143, 177)
    line(startCoord[0] * gridLength, startCoord[1] * gridLength, zielCoord[0] * gridLength, zielCoord[1] * gridLength)
    print(zielCoord)
    startCoord = zielCoord

    # Textbox am unteren Rand
    fill(255)
    no_stroke()
    rect(0, 816, 816, 846)
    fill(0)
    text("Framerate: " + str(py5.frame_rate) + "  |  Schritt: " + str(py5.frame_count), py5.width / 2, 830)


# Liefert anhand von [X, Y] Koordinaten (startCoord) eine «benachbarte» Zielkoordinate
def getZielCoord(startCoord):
    # Annahme zu Begin: Keine Bewegung
    zielX = startCoord[0]
    zielY = startCoord[1]
    zielCoord = [zielX, zielY]

    # Richtung per Zufallszahl ermitteln
    direction = int(random(0, 8))

    # Y - Zielkoordinate
    if direction == 0 or direction == 1 or direction == 2:
        if startCoord[1] > 1:
            zielY = startCoord[1] - 1  # Ziel: oben
    if direction == 4 or direction == 5 or direction == 6:
        if startCoord[1] <= 100:
            zielY = startCoord[1] + 1  # Ziel: unten

    # X - Zielkoordinate
    if direction == 0 or direction == 6 or direction == 7:
        if startCoord[0] > 1:
            zielX = startCoord[0] - 1  # Ziel: links
    if direction == 2 or direction == 3 or direction == 4:
        if startCoord[0] <= 100:
            zielX = startCoord[0] + 1  # Ziel: rechts

    zielCoord[0] = zielX
    zielCoord[1] = zielY

    return (zielCoord)


run_sketch()