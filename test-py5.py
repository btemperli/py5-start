# Beispiel von https://py5coding.org/content/install.html
import py5


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.rect(py5.mouse_x, py5.mouse_y, 10, 10)


py5.run_sketch()