import py5


def setup():
    py5.size(400, 400)
    py5.frame_rate(24)
    py5.fill(0, 0, 0)


def draw():
    py5.background(255, 255, 255)
    py5.text(str(py5.get_frame_rate()), 100, 100)
    py5.text(str(py5.frame_count), 100, 150)


py5.run_sketch()
