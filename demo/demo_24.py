import py5


def setup():
    py5.size(600, 600)
    py5.text_size(24)
    py5.fill(255, 128, 0)


def draw():
    py5.text("Maustaste klicken", 10, 30)


def mouse_pressed():
    py5.fill(180, 180, 180)
    py5.text("hallo", py5.mouse_x, py5.mouse_y)


def mouse_released():
    py5.fill(255, 128, 0)
    py5.text("hallo", py5.mouse_x - 2, py5.mouse_y - 2)


py5.run_sketch()
