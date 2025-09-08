import py5

def setup():
    py5.size(400, 200)
    py5.fill(0)
    py5.text_size(24)
    name = input("Name eingeben: ")
    py5.background(255)
    py5.text(f"Hallo {name}", 50, 100)

py5.run_sketch()