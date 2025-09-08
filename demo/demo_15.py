import py5


def settings():
    w = py5.display_width
    h = py5.display_height
    py5.size(int(w / 2), int(h / 2))


def setup():
    py5.background(255, 255, 255)

    for y in range(0, py5.height, 40):
        py5.ellipse(py5.width / 2, y + 20, 40, 40)


py5.run_sketch()
