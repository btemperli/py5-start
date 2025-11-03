# py5 + python via docker

-- beta-version --

## Installieren

1. Lade "Docker Desktop" für dein Betriebssystem von der offiziellen [Docker-Seite](https://docs.docker.com/get-started/get-docker/) herunter.
2. "Docker Desktop" installieren
3. Diesen Ordner `docker-environment` herunterladen und bei einem zugänglichen Pfad ablegen
4. Via Konsole<sup>[1](#fn1)</sup> zum Pfad navigieren<sup>[2](#fn2)</sup>: `cd pfad/zum/projekt/docker-environment`
5. Die Datei `start.sh` in der Konsole<sup>[1](#fn1)</sup> ausführen: `./start.sh`
   (dies dauert gut und gerne 2-3 Minuten)
6. Am Ende sollte unter anderem die Ausgabe `✅ Container läuft!` erscheinen


## Testen

1. Im Browser deiner Wahl die Webseite [`http://localhost:6080/`](http://localhost:6080/) öffnen
2. Du siehst nun die Desktop-Oberfläche von dieser Docker-Umgebung
3. Via Konsole kannst du nun in der Docker-Umgebung das py5-Programm starten: `Applications -> Terminal Emulator`
4. Nun sollte dein `py5-Programm` erfolgreich starten: `python test-py5.py`


## Python programmieren

Dieser Ordner `docker-environment` von dem aus du gestartet bist, ist direkt mit der Docker-Umgebung verknüpft.
Du kannst also direkt in diesem Ordner arbeiten.
Erstelle einen Unterordner "projekt" direkt auf dem Computer.
Öffne diesen Ordner in der Programmierumgebung deiner Wahl und erstelle darin dein erstes Programm: z.B. `main.py`

1. Bearbeite dein Programm in deiner Programmierumgebung
2. Teste das Programm in der Docker-Umgebung
3. im Terminal der Docker-Umgebung startest du dein Programm: `python main.py`

Deine Änderungen von der Programmierumgebung kannst du nun beliebig neu testen.
Falls du diesen Projekt-Ordner mit [github](https://github.com/) verknüpfen möchtest, kannst du diesen Ordner bei `Github Desktop` verknüpfen.


## Docker?

Docker ist ein Programm, welches dir ermöglicht, eine einfache virtuelle Umgebung auf deinem Computer einzurichten.
Du kannst auf deinem Computer also eine Emulation von einem zweiten Computer laufen lassen - und diesen zweiten Computer habe ich für dich vorbereitet.
Auf diesem zweiten Computer ist python, java und py5 vorbereitet und korrekt konfiguriert. 

In deiner Docker-Umgebung (`Docker Desktop`) siehst du unter "Containers" den erstellten Container `py5-vnc-container`.
Du kannst direkt im Programm den Container starten und stoppen.

Falls du die Datei `start.sh` erneut ausführen willst, stoppst du den Container davor und entfernst diesen.
<small>Beim erneuten Ausführen der Datei dauert es nun übrigens nur noch ein paar Sekunden und nicht mehr 2-3 Minuten.</small>

---

<br><a name="fn1">1</a> Windows: *cmd* / Mac: *Terminal*
<br><a name="fn2">2</a> Die wichtigsten Befehle für die Konsole unter [Windows](https://www.thomas-krenn.com/de/wiki/Cmd-Befehle_unter_Windows) und [Unix (mac + linux)](https://www.computerweekly.com/de/ratgeber/Die-Top-50-universellen-UNIX-Befehle)
<br><a name="fn3">3</a> zum Beispiel [PyCharm](https://www.jetbrains.com/de-de/pycharm/) oder [Visual Studio Code](https://code.visualstudio.com/)
