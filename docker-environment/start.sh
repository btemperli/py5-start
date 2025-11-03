#!/bin/bash
# Starte den py5-Container mit VNC und Desktop im Browser

docker build -t py5-vnc .
docker run -d \
  -p 6080:6080 \
  -v "$(pwd)":/workspace \
  --name py5-vnc-container \
  py5-vnc

echo ""
echo "✅ Container läuft!"
echo "Öffne im Browser: http://localhost:6080"
echo "Starte Applikation > Terminal Emulation"
echo "Starte Test-Datei: python test-py5.py"
echo ""
echo "Zum Stoppen: docker stop py5-vnc-container"