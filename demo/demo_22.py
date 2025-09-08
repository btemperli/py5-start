import py5


def setup():
    py5.size(600, 600);
    py5.stroke(0, 0, 0)


def draw():
    if py5.is_mouse_pressed:
        if py5.mouse_button == py5.LEFT:
            py5.stroke(0, 0, 0)
        if py5.mouse_button == py5.RIGHT:
            py5.stroke(255, 0, 0)
        if py5.mouse_button == py5.CENTER:
            py5.stroke(0, 0, 255)

        py5.line(py5.pmouse_x,
                 py5.pmouse_y,
                 py5.mouse_x,
                 py5.mouse_y)


py5.run_sketch()
