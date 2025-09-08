import py5


def setup():
    py5.size(600, 600)


def draw():
    py5.line(py5.pmouse_x,
         py5.pmouse_y,
         py5.mouse_x,
         py5.mouse_y)

py5.run_sketch()