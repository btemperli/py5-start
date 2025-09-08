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
data = []


def setup():
    global data

    py5.size(920, 500)
    py5.text_size(18)

    # Datei auslesen und Zeile für Zeile in die Liste «sprites» speichern
    with open("neue_gemeinden_utf8.csv") as file:
        for line in file:
            zeile = line.strip().split(";")
            data.append(zeile)

    print(data)

    del data[0]
    # print(sprites)


def draw():
    global regions
    global data

    py5.background('#ffffff')

    for i in range(1, len(regions)):
        py5.fill('#333333')
        py5.text(regions[0][i - 1], 20, i * 60)

        # Linien
        py5.stroke('#333333')
        py5.line(210, i * 60, 890, i * 60)

        # Data
        py5.fill('#ff2222')
        py5.no_stroke()
        for j in range(0, len(data)):
            if data[j][1] in regions[i]:
                y = int(data[j][2]) - 1850
                py5.circle(210 + y * 4, i * 60, 8)

    # year legende
    py5.fill('#333333')
    for y in range(0, 4):
        py5.text(1850 + y * 50, 200 + y * 200, 470)


py5.run_sketch()