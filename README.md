# py5-example

Dies ist ein Beispiel für die Nutzung von https://py5coding.org/

## installation

Eine genaue Anleitung existiert hier: https://py5coding.org/content/install.html#

Ergänzungen:

- Im Programm `PyCharm` muss unbedingt die Python-Version ausgewählt werden, die für die Installation von py5 genutzt wurde.
  - PyCharm &rarr; Settings &rarr; Python Interpreter

- Mit Homebrew (MacOS) muss eine Virtuelle Umgebung erstellt werden
  - `$ python3 -m venv path/to/venv`
  - `$ source path/to/venv/bin/activate` (in der Konsole die Umgebung aktivieren)
  - `$ python3 -m pip install py5` (Das Programm `py5` installieren)
- Das `main.py` kann gestartet werden, um die Umgebung zu testen. Gut möglich, dass dabei die folgenden Warnungen ausgegeben werden. Sofern das Programm läuft, kann das ignoriert werden:
  - `WARNING: A restricted method in java.lang.System has been called`
  - `WARNING: java.lang.System::load has been called by org.jpype.JPypeContext in an unnamed module (file:/Users/xxx/python3-venv/lib/python3.13/site-packages/org.jpype.jar)`
  - `WARNING: Use --enable-native-access=ALL-UNNAMED to avoid a warning for callers in this module`
  - `WARNING: Restricted methods will be blocked in a future release unless native access is enabled`