import py5


def setup():
    py5.size(600, 600)
    py5.background(248, 187, 208)


def draw():
    # Variante 1: Line zum Mauszeiger
    # Wenn der Background entkommentiert wird, so wird jedes mal ein neues Frame erstellt
    # py5.background(248,187,208)
    py5.ellipse(py5.mouse_x, py5.mouse_y, 30, 30)


py5.run_sketch()
