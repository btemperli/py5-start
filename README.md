# py5-example

Dies ist ein Beispiel für die Nutzung von https://py5coding.org/

## Welche Variante?

Es gibt 2 Möglichkeiten, py5 auf deinen Computer zu bringen:

- Variante A: lokale Installation.
  <br>Du installierst bei dir auf dem Computer die Programme `python` und die Library `py5`. In einer Entwicklungsumgebung bearbeitest du deine Programme
  und kannst diese auch gleich starten, testen und ausprobieren.
- Variante B: virtuelle Installation.
  <br>Die relevanten Programme `python` und `py5` laufen in einer virutellen Umgebung (Docker-Umgebung) auf deinem Computer.
  Du entwickelst deine Programme bei dir lokal in einer Entwicklungsumgebung. Die Dateien sind dabei direkt mit der virtuellen Umgebung verknüpft.
  In der virtuellen Umgebung kannst du deine erstellten Programme starten, testen und ausprobieren.

Für Variante B wählst du die [Docker-Installation](docker-environment).

Für Variante A kannst du gleich hier fortfahren.

## Vorbereitung

Für die Installation von `py5` benötigst du Java und Python. In der Konsole (windows: `cmd`, macOS: `terminal`) kannst du folgendes eingeben:

    python --version
    java --version

Falls `python --version` nicht gefunden wird, probiere es mit `python3 --version` 

Die Ausgabe müsste anzeigen, ob die Programme installiert sind und in welcher Version, oder ob die Befehle nicht bekannt sind: in diesem Fall musst du die beiden Programme installieren.

---

<details>

<summary>Java installieren</summary>

### Installation Java (17+)

https://www.oracle.com/java/technologies/downloads/#jdk24-windows
Installation befolgen

</details>

---

<details>

<summary>Python installieren</summary>

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

Du kannst direkt diese Programme nutzen und den ganzen Dateipfad anstatt nur `pip3` einsetzen:

    /Library/Frameworks/Python.framework/Versions/3.13/bin/pip3 install py5

Um die kurze Variante zu nutzen, kannst du pip3 bzw. python3 in der Konfigurationsdatei von deiner Konsole `~/.zshrc` (im Home-Folder) überschreiben:

    alias python3="/Library/Frameworks/Python.framework/Versions/3.13/bin/python3"
    alias pip3="/Library/Frameworks/Python.framework/Versions/3.13/bin/pip3"

Teste dein Setup nun wieder:

    python3 --version

Eine wiederum komplizierter Version ist die Installation mit `homebrew`: https://brew.sh/

</details>

---

## installation py5

    pip3 install py5

Eine genaue Anleitung existiert hier: https://py5coding.org/content/install.html#

---

<details>

<summary>Entwicklungsumgebung installieren</summary>

## installation IDE (Entwicklungsumgebung)

Für die Programmierung brauchst du nun eine Entwicklungsumgebung, in der du Code schreiben kannst und von der aus du dein Programm direkt starten kannst.
- Variante A: Visual Studio Code. Gratis, aber es braucht noch die Extension `Python`.
- Variante B: PyCharm. Als Studierende Person gratis, man muss sich aber bei jetbrains registrieren.

</details>

---

## Fehlermeldungen

Hier eine Auflistung von Problemen, die auftauchen könnten und Ansätze, wie diese behoben werden.

<details>

<summary>Exit code -1073741819 (0xC0000005) &rarr; Windows</summary>

### Auftauchen

- `import py5` in einem `.py`-Programm verwenden und das Programm starten
- `python` in der Konsole starten, dann `import py5` ausführen

In beiden Fällen bricht das Programm ab mit dem oben genannten Fehler.

### Problem

Eventuell liegt es an der installierten Version von Python.
Es kann sein, dass das Problem bei `3.13` und auch `3.12` auftaucht.

### Problemlösung

- (die aktuelle Python-Version deinstallieren)
- Python `3.11` [herunterladen](https://www.python.org/downloads/#:~:text=Looking%20for%20a%20specific%20release%3F) und installieren

</details>

<details>

<summary>raise JVMNotFoundException("No JVM shared library file ({0}) "</summary>

### Auftauchen

- `import py5` in einem `.py`-Programm verwenden und das Programm starten
- `python` in der Konsole starten, dann `import py5` ausführen

In beiden Fällen bricht das Programm ab mit dem oben genannten Fehler, ergänzt durch Informationen, wo das Problem genau auftaucht
- `jpype.startJVM()`
- `jvmpath = getDefaultJVMPath()`
- `return finder.get_jvm_path()`
- `jpype._jvmfinder.JVMNotFoundException: No JVM shared library file (jvm.dll) found. Try setting up the JAVA_HOME environment variable properly.`

### Problemlösung

Die `JAVA_HOME`-Variable fehlt bei den Systemumgebungsvariablen. Dort werden alle Programme als "Variable" aufgelistet, so dass andere Programme auf diese Programme zugreifen können.

1. Wie du die `JAVA_HOME`-Variable manuell einfügen kannst: [Umgebungsvariablen anpassen](https://learn.jamf.com/de-DE/bundle/technical-articles/page/Configuring_JAVA_HOME_and_JRE_HOME_Environment_Variables_on_a_Windows_Server.html)
2. Wie du `JAVA_HOME` anschliessend in die globale `PATH`-Variable hinzufügen kannst: [Path-Variable bearbeiten](https://www.java.com/de/download/help/path.html). Der neue Eintrag (neue Zeile einfügen) sollte lauten: `%JAVA_HOME%\bin`
3. Bevor du nun weiterfahrst, musst du `cmd` neu starten und im schlimmsten Fall `pyCharm` neu installieren. Vielleicht reicht aber auch ein Neustart.
4. Umgebungsvariablen testen: `$ echo %JAVA_HOME%` in der Kommandozeile ausführen
5. `import py5` in der Python-Umgebung oder in einer Python-Datei ausführen.

</details>

---

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