import py5

x = 200
y = 200


def setup():
    py5.size(600, 600)
    py5.background(255, 255, 255)


def draw():
    if x <= py5.mouse_x <= x + 200 and y <= py5.mouse_y <= y + 50 and py5.is_mouse_pressed:
        py5.fill(255, 0, 0)
    else:
        py5.fill(60, 60, 60)

    py5.rect(x, y, 200, 50)


py5.run_sketch()
