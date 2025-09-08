from py5 import *


# Funktion zeichnet ein Kreuz
#
# xPos, yPos: Koordinaten fuer den Mittelpunkt des Kreuzes
# l: Laenge eines Arms
def kreuz(xPos, yPos, l):
    print("hello")
    stroke(255, 255, 255)

    rect(xPos - 0.5 * l, yPos - 1.5 * l, l, l * 3)
    rect(xPos - 1.5 * l, yPos - 0.5 * l, l * 3, l)
