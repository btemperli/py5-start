# py5-example

Dies ist ein Beispiel für die Nutzung von https://py5coding.org/

## vorbereitung

Für die Installation von `py5` benötigst du Java und Python. In der Konsole (windows: `cmd`, macOS: `terminal`) kannst du folgendes eingeben:

    $ python --version
    $ java --version

Falls `$ python --version` nicht gefunden wird, probiere es mit `$ python3 --version` 

Die Ausgabe müsste anzeigen, ob die Programme installiert sind und in welcher Version, oder ob die Befehle nicht bekannt sind: in diesem Fall musst du die beiden Programme installieren.

### Installation Java (17+)

https://www.oracle.com/java/technologies/downloads/#jdk24-windows
Installation befolgen

### Installation Python (3.10+)

#### Windows
https://www.python.org/downloads/

Berücksichtige: bei der Installation bitte auswählen, dass "Add Python to PATH" ausgewählt wird. Nur so ist im Nachhinein `python` direkt als Programm aufrufbar.

#### Mac OS
Auf einem Apple-Gerät ist es leider etwas komplizierter. Mehr Informationen gibt es beispielsweise hier:
https://mac.install.guide/python/update

Wenn du Python über die normale Python-Webseite herunterlädst und installierst, wird das python-Programm wahrscheinlich hier abgelegt:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/python3

Pip3 müsste entsprechend hier liegen:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/pip3

Du kannst direkt diese Programme nutzen und entweder direkt darauf verlinken:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/pip3 install py5

anstatt

    pip3 install py5

Eine wiederum komplizierter Version ist die Installation mit `homebrew`: https://brew.sh/

## installation py5

Eine genaue Anleitung existiert hier: https://py5coding.org/content/install.html#


## installation IDE

Für die Programmierung brauchst du nun eine Entwicklungsumgebung, in der du Code schreiben kannst und von der aus du dein Programm direkt starten kannst.
- Variante A: Visual Studio Code. Gratis, aber es braucht noch die Extension `Python`.
- Variante B: PyCharm. Als Studierende Person gratis, man muss sich aber bei jetbrains registrieren.


## Ergänzungen

- Im Programm `PyCharm` muss unbedingt die Python-Version ausgewählt werden, die für die Installation von py5 genutzt wurde.
  - PyCharm &rarr; Settings &rarr; Python Interpreter

- Mit Homebrew (MacOS) muss eine Virtuelle Umgebung erstellt werden
  - `$ python3 -m venv path/to/venv`
  - `$ source path/to/venv/bin/activate` (in der Konsole die Umgebung aktivieren)
  - `$ python3 -m pip install py5` (Das Programm `py5` installieren)
- Die Datei `test-py5.py` kann gestartet werden, um die Umgebung zu testen.
  - Variante Konsole: `$ python3 test-py5.py`
  - Variante `PyCharm`: Rechtsklick auf Datei &rarr; Run 'test-py5.py'
  - Variante `Visual Studio Code`: Rechtsklick auf Datei &rarr; Run Python File in Terminal
  - Gut möglich, dass bei der Ausführung die folgenden Warnungen ausgegeben werden. Sofern das Programm läuft, kann das ignoriert werden:
    - ```
         WARNING: A restricted method in java.lang.System has been called
         WARNING: java.lang.System::load has been called by org.jpype.JPypeContext in an unnamed module (file:/Users/xxx/python3-venv/lib/python3.13/site-packages/org.jpype.jar)
         WARNING: Use --enable-native-access=ALL-UNNAMED to avoid a warning for callers in this module
         WARNING: Restricted methods will be blocked in a future release unless native access is enabled
      ```