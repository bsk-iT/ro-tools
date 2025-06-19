pyinstaller main.py --onefile --windowed --icon=icon.ico --add-data "assets;assets" --manifest admin.manifest
cp config.json dist/
cp servers.json dist/