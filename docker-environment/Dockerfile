# Verwende neueste stabile Python-Version
FROM consol/debian-xfce-vnc:latest

# Konfiguration für DEBIAN-XFCE-VNC
ENV NO_VNC_PORT=6080
ENV VNC_PASSWORDLESS=true

# Wechsle zu root für Installation
USER root

# 🔧 Entferne/Deaktiviere alle fehlerhaften Chrome-Repos (mehrere mögliche Speicherorte)
RUN rm -f /etc/apt/sources.list.d/google-chrome.list \
    && rm -f /etc/apt/sources.list.d/google-chrome-beta.list \
    && rm -f /etc/apt/sources.list.d/google-chrome-unstable.list \
    && sed -i '/google-chrome/d' /etc/apt/sources.list || true
RUN apt-get purge -y google-chrome-stable || true

# Installiere systemweite Abhängigkeiten für py5 (inkl. Java)
RUN apt-get update && apt-get install -y \
    python3 python3-pip python3-tk \
    openjdk-17-jre \
    g++ \
    python3.11-venv \
    && rm -rf /var/lib/apt/lists/*

RUN ln -s /usr/bin/python3 /usr/bin/python

# Arbeitsverzeichnis im Container
WORKDIR /workspace

# requirements.txt kopieren, daraus werden die benötigten Libraries installiert
COPY requirements.txt .

RUN python3 -m venv /opt/venv
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Virtuelle Python-Umgebung mit py5 zum PATH hinzufügen
ENV PATH="/opt/venv/bin:$PATH"

# Öffne Port für noVNC
EXPOSE 6080

# Container soll weiterlaufen
CMD ["/bin/bash", "-c", "tail -f /dev/null"]

