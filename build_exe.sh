python build_version.py && pyinstaller main.py --onefile --windowed --icon=icon.ico --add-data "assets;assets" --version-file version.txt --manifest "admin.manifest"
cp config.json dist/
cp servers.json dist/