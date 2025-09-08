'''
' Schieberegler
' Simon Hefti & Beat Temperli
'''

from py5 import *
import py5

# Globale Variablen:
# movingMode (Boolean): True, wenn der Schieber (Kreis) in Bewegung ist, False wenn nicht
# pointerPos (Integer): Position des Pointers in Pixeln
# pointerVal (Float):   Eingestellter Wert (0 - 100)
moving_mode = False
pointer_pos = 0
pointer_val = 1.0


# settings, weil "from py5 import *"
def settings():
    size(900, 500)


# Initialisierung
def setup():
    text_size(64)
    text_align(CENTER)


# Sich wiederholende draw() Funktion
def draw():
    background(255)
    draw_ruler(200, 400, 500)
    text(str(pointer_val) + "%", py5.width / 2, py5.height / 2)


# Funktion: Schieberegler generieren
# objX:      X-Position des Reglers
# objY:      Y-Position des Reglers
# objLength: Länge des Reglers
def draw_ruler(objX, objY, objLength):
    global moving_mode
    global pointer_pos
    global pointer_val

    # Schieber einstellen
    pointer_radius = 24
    if pointer_pos == 0:
        pointer_pos = objX

    # Linie zeichnen
    fill(85)
    stroke_weight(6)
    line(objX, objY, objX + objLength, objY)
    fill(185)
    stroke_weight(2)

    # Überprüfen ob Schieber angeklickt worden ist --> Bewegungsmodus aktivieren
    if pointer_pos - pointer_radius < py5.mouse_x < pointer_pos + pointer_radius and objY - pointer_radius < py5.mouse_y < objY + pointer_radius and py5.is_mouse_pressed:
        moving_mode = True

    # Wenn keine Maustaste gedrückt ist --> Bewegungsmodus deaktivieren
    if not py5.is_mouse_pressed:
        moving_mode = False
        cursor(ARROW)

    # Bei aktiviertem Bewegungsmodus
    if moving_mode:
        cursor(HAND)

        # Schieber der Line entlang bewegen
        if objX < py5.mouse_x < objX + objLength:
            pointer_pos = py5.mouse_x

        # Wenn Maus ausserhalb der Linie, Schieber am Start oder Ende fixieren
        else:
            if py5.mouse_x < objX:
                pointer_pos = objX
            if py5.mouse_x > objX:
                pointer_pos = objX + objLength

    # Schieber zeichnen
    circle(pointer_pos, objY, pointer_radius)

    # Eingestellter Wert anhand der Schieberposition ermitteln
    pointer_val = int(100 / float(objLength) * (pointer_pos - objX))


run_sketch()