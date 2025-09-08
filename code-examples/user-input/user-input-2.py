# User-Input
# Variante 2: Fenster
# In dieser Variante wird der Input direkt im Fenster angezeigt

import py5

name = ""
eingabe_fertig = False


def setup():
    py5.size(400, 200)
    py5.text_size(24)


def draw():
    py5.background(255)
    py5.fill(0)

    if not eingabe_fertig:
        py5.text("Name eingeben: " + name + "|", 50, 100)
    else:
        py5.text(f"Hallo {name}", 50, 100)


def key_typed(e):
    global name, eingabe_fertig
    if not eingabe_fertig:
        if e.get_key() == '\n':   # Enter beendet Eingabe
            eingabe_fertig = True
        elif e.get_key() == '\b':  # Backspace löscht
            name = name[:-1]
        else:
            name += e.get_key()


py5.run_sketch()