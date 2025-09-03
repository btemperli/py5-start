import requests
import py5

# Modul JSON laden um Daten im JSON-Format lesen zu können
import json


def setup():
    py5.size(600, 600)
    py5.fill(55, 71, 79)
    py5.text_size(24)
    py5.text_align(py5.CENTER)

    # Daten auslesen und in «response» speichern
    url = "https://nominatim.openstreetmap.org/search.php?q=st.gallen+notkerstrasse+27+phsg&format=jsonv2"
    headers = {"User-Agent": "py5-geo-demo"}  # Nominatim verlangt einen User-Agent
    response = requests.get(url, headers=headers)

    # «response» als JSON interpretieren und in die Liste «data» speichern
    data = response.json()

    # Resultat ausgeben
    output = "Koordinaten PHSG: " + data[0]['lat'] + ", " + data[0]['lon']
    py5.text(output, 300, 300)

py5.run_sketch()