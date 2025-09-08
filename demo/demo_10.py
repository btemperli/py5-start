import py5


def setup():
    py5.size(600, 600)


def draw():
    py5.background(255, 255, 255)

    # kopf
    py5.ellipse(300, 300, 200, 200)

    # augen
    py5.ellipse(270, 270, 20, 20)
    py5.ellipse(330, 270, 20, 20)

    # mund
    py5.line(280, 330, 320, 330)

py5.run_sketch()
