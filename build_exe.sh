pyinstaller main.py --onefile --windowed --icon=icon.ico --add-data "assets;assets"
cp config.json dist/
cp servers.json dist/
cp maps.json dist/