import py5

regions = []
regions.append(
    ['Genferseeregion', 'Espace Mittelland', 'Nordwestschweiz', 'Zuerich', 'Ostschweiz', 'Zentralschweiz', 'Tessin'])
regions.append(['GE', 'VD', 'VS'])
regions.append(['BE', 'FR', 'JU', 'NE', 'SO'])
regions.append(['AG', 'BL', 'BS'])
regions.append(['ZH'])
regions.append(['AI', 'AR', 'GL', 'GR', 'SH', 'SG', 'TG'])
regions.append(['LU', 'NW', 'OW', 'SZ', 'UR', 'ZG'])
regions.append(['TI'])
colors = [py5.color(194, 24, 91), py5.color(123, 31, 162), py5.color(57, 73, 171), py5.color(2, 136, 209), py5.color(0, 151, 167),
          py5.color(0, 121, 107), py5.color(175, 180, 43)]
data = []


# Funktion Quadrate Zeichnen
# xPos   : Position X
# yPos   : Position y
# extent : Länge des Quadrats
# vals   : Liste der Werte (Zwischenquadrate)
# c      : Farbe (Color)
def draw_quadrats(xPos, yPos, extent, val, c):
    py5.fill(c, 50)
    py5.stroke(c)
    py5.square(xPos, yPos, extent)
    py5.no_fill()
    for i in range(0, len(val)):
        py5.square(xPos, yPos + extent - val[i], val[i])

def setup():
    global data

    py5.size(998, 620)

    # CSV Datei auslesen und Zeile für Zeile in die Liste «sprites» speichern
    with open("neue_gemeinden_utf8.csv") as file:
        for line in file:
            zeile = line.strip().split(";")
            data.append(zeile)

    # Kopfzeile löschen
    del data[0]
    # print(sprites) #Test


def draw():
    global regions
    global colors
    global data

    # config
    py5.background('#ffffff')
    py5.text_align(py5.LEFT)
    py5.text_size(16)

    # Itreation Grossrregion Schweiz
    for i in range(1, len(regions)):  # Start bei 1, da die Kopfzeile ignoriert werden soll

        # Iteration sprites[] je Grossreegion
        vals = []
        for j in range(0, len(data)):
            if data[j][1] in regions[i]:
                y = int(data[j][2]) - 1850
                vals.append(y * 1.3)

        # Definition xPos, yPos je nach Grossreegion (Zeile 1 & 2)
        if i < 5:
            xPos = 20 + (i - 1) * (221 + 20)
            yPos = 100
        else:
            xPos = 20 + (i - 5) * (221 + 20)
            yPos = 120 + 221 + 20

        # Quadrate zeichnen
        draw_quadrats(xPos, yPos, 221, vals, colors[i - 1])

        # Grossregionen beschreiben
        py5.fill('#333333')
        py5.text(regions[0][i - 1], xPos, yPos - 4)

    # Titel
    py5.text_align(py5.CENTER)
    py5.text_size(28)
    py5.text("Neue Gemeinden in der CH seit 1850", 499, 50)

    # Legende
    py5.stroke(120, 144, 156)
    py5.fill(236, 239, 241)
    py5.square(743, 361, 221)
    py5.text_align(py5.LEFT)
    py5.text_size(16)
    py5.fill(69, 90, 100)
    py5.text("1850", 753, 572)
    py5.text("2020", 915, 383)

py5.run_sketch()