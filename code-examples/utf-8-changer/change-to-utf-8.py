# Datei von Latin-1/Windows-1252 nach UTF-8 konvertieren
input_file = "neue_gemeinden.csv"
output_file = "../csv-gemeinden-a/neue_gemeinden_utf8.csv"

with open(input_file, "r", encoding="mac_roman") as f_in:
    content = f_in.read()

with open(output_file, "w", encoding="utf-8") as f_out:
    f_out.write(content)

print("Konvertierung abgeschlossen:", output_file)
