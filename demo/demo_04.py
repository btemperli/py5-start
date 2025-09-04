import py5


def setup():
    # Programmstart (Initialisierung)
    # print("Programmstart")
    py5.size(400, 400)
    py5.background(248, 187, 208)


def draw():
    # Laufendes Programm (Betriebsmodus)
    # print("im Betrieb")
    py5.ellipse(200, 200, 100, 100)
    py5.line(100, 250, 300, 250)


py5.run_sketch()
