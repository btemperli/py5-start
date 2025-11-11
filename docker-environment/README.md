# py5 + python via docker

-- beta-version --

## Schema

      =============================== Entwicklungsumgebung ===============================
      
      +----------------------------------+          +------------------------------------+
      |  Lokaler Rechner                 |          |  Docker-Container (Linux)          |
      |  ------------------------------  |          |  --------------------------------  |
      |  IDE (z. B. PyCharm)             |   Code   |  Python + py5                      |
      |  - Bearbeiten von Programmen     | <------> |  - Ausführung des Programms        |
      |  - Projekte im lokalen Ordner    |   Sync   |  - Zugriff über Browser            |
      |    gespeichert                   |   via    |    (z. B. http://localhost:6080)   |
      |                                  |  Volume  |                                    |
      |  Browser (z. B. Firefox)         |          |                                    |
      |  - Verbindung zur Docker-App     | -------> |  - Weboberfläche bereitgestellt    |
      +----------------------------------+          +------------------------------------+

### Legende


      <------> Gemeinsamer synchronisierter Projektordner
      -------> Zugriff über localhost via Browser

---


## Installieren

1. Lade "Docker Desktop" für dein Betriebssystem von der offiziellen [Docker-Seite](https://docs.docker.com/get-started/get-docker/) herunter.
2. "Docker Desktop" installieren
3. Diesen Ordner `docker-environment` herunterladen und bei einem zugänglichen Pfad ablegen
4. Via Konsole<sup>[1](#fn1)</sup> zum Pfad navigieren<sup>[2](#fn2)</sup>: `cd pfad/zum/projekt/docker-environment`
5. *Nur Windows:* Doppelklick auf die Datei `start.sh`. Damit sollte der Docker-Container erstellt werden und direkt in der Docker-App sichtbar werden. 
   Die Installation ist somit abgeschlossen.
6. *Nur Mac:* Die Datei `start.sh` in der Konsole<sup>[1](#fn1)</sup> ausführen: `./start.sh`
   (dies dauert gut und gerne 2-3 Minuten)
7. *Nur Mac:* Am Ende sollte in der Konsole unter anderem die Ausgabe `✅ Container läuft!` erscheinen


## Testen

1. Im Browser deiner Wahl<sup>[3](#fn3)</sup> die Webseite [`http://localhost:6080/`](http://localhost:6080/) öffnen
2. Du siehst nun die Desktop-Oberfläche von dieser Docker-Umgebung
3. In der Docker-Umgebung kannst du nun via Konsole<sup>[5](#fn5)</sup> das py5-Programm starten: `Applications -> Terminal Emulator`
4. Nun sollte dein `py5-Programm` erfolgreich starten: `python test-py5.py`
5. Im Browser-Fenster kannst du nun dein `py5-Programm` testen


## Python programmieren

Dieser Ordner `docker-environment` von dem aus du gestartet bist, ist direkt mit der Docker-Umgebung verknüpft.
Du kannst also direkt in diesem Ordner arbeiten.
Erstelle einen Unterordner "projekt" direkt auf dem Computer.
Öffne diesen Ordner in der Programmierumgebung deiner Wahl und erstelle darin dein erstes Programm: z.B. `main.py`

1. Bearbeite dein Programm in deiner Programmierumgebung deiner Wahl<sup>[4](#fn4)</sup>
2. Teste das Programm in der Docker-Umgebung
3. navigiere via Terminal der Docker-Umgebung<sup>[5](#fn5)</sup> in den Projekt-Ordner: `cd projekt`
4. starte im Terminal der Docker-Umgebung<sup>[5](#fn5)</sup> dein Programm: `python main.py`

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


## Probleme

<details>

<summary>Der Ordner workspace ist leer</summary>

### Auftauchen

`Terminal Emulator` starten, der Befehl `ls` gibt nur das Dokument `requirements.txt` aus. Alle anderen Dateien aus diesem Ordner sind nicht vorhanden.

### Problem

Der lokale Ordner (Ausgang: `docker-environment`) ist nicht korrekt mit der Docker-Umgebung synchronisiert.
Normalerweise wird der Ordner mit dem Ordner `workspace` in der Docker-Umgebung live synchronisiert.
Sobald du bei dir lokal im Ordner eine Datei erstellst, ist diese auch direkt in der Docker-Umgebung vorhanden.

### Problemlösung

1. Überprüfe in der Docker-App die `Details` vom Container `py5-vnc-container` (3 Punkte neben dem Start-Knopf: `-> View Details`).
2. Wechsle zum Reiter `Bind mounts`.
3. Hier sollte sichtbar sein, wo der Ordner (linke Seite) auf deinem Computer liegt und wo er (rechte Seite) in der Docker-Umgebung zu finden ist.
4. Wende dich an den Dozenten, falls du mit diesen Informationen nichts anfangen kannst.

</details>

<details>

<summary> <code>python test.py</code> führt zu <code>py5 not found</code>-Fehler</summary>

### Auftauchen

`Terminal Emulator` starten, der Befehl `python test.py` gibt eine Fehlermeldung: `ModuleNotFound: py5`.

### Problem

Python, so wie es ausgeführt wurde, ist in der "echten" Variante gestartet, `py5` wurde aber nur in der virtuellen Umgebung hinzugefügt.
Du kannst mit `echo $PATH` überprüfen, ob die virtuelle Python-Umgebung eingebunden wurde: die Ausgabe müsste zuvorderst mit `/opt/venv/bin:` starten.

### Problemlösung

1. Stoppe den Docker-Container in der Docker-App.
2. Lösche den Docker-Container in der Docker-App.
3. Starte den Container neu: `Installieren -> Punkt 5 / 7`.

Falls das nichts bringt: wechsle von `python test.py` zu `/opt/venv/bin/python test.py`.

</details>

---

<br><a name="fn1">1</a> Windows: *cmd* / Mac: *Terminal*
<br><a name="fn2">2</a> Die wichtigsten Befehle für die Konsole unter [Windows](https://www.thomas-krenn.com/de/wiki/Cmd-Befehle_unter_Windows) und [Unix (mac + linux)](https://www.computerweekly.com/de/ratgeber/Die-Top-50-universellen-UNIX-Befehle)
<br><a name="fn3">3</a> zum Beispiel [Firefox](https://www.firefox.com/) oder [Brave](https://brave.com/)
<br><a name="fn4">4</a> zum Beispiel [PyCharm](https://www.jetbrains.com/de-de/pycharm/) oder [Visual Studio Code](https://code.visualstudio.com/)
<br><a name="fn5">5</a> [http://localhost:6080/](http://localhost:6080/) öffnen `->` Applications `->` Terminal Emulator
