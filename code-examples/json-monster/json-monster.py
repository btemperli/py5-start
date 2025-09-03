import json
import py5

def setup():
    py5.size(600, 600)
    py5.fill(55, 71, 79)
    py5.text_size(24)
    py5.text_align(py5.CENTER)

    f = open('monster.json')
    data = json.load(f)

    py5.text(data[0]["common name"], 300, 200)
    py5.text(data[0]["scientific name"]["species"], 300, 225)

    py5.text(data[1]["common name"], 300, 300)
    py5.text(data[1]["scientific name"]["species"], 300, 325)

py5.run_sketch()