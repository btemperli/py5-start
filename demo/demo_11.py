import py5

kopf_x = 300
kopf_y = 300


def setup():
    py5.size(600, 600)


def draw():
    py5.background(255, 255, 255)

    py5.ellipse(kopf_x, kopf_y, 200, 200)
    py5.ellipse(kopf_x - 30, kopf_y - 30, 20, 20)
    py5.ellipse(kopf_x + 30, kopf_y - 30, 20, 20)
    py5.line(kopf_x - 20, kopf_y + 30, kopf_x + 20, kopf_y + 30)


py5.run_sketch()
