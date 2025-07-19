rm -r dist

python -m nuitka --standalone \
  --output-dir=dist \
  --onefile \
  --output-filename=RO_Tools \
  --include-data-dir=assets=assets \
  --windows-uac-admin \
  --windows-console-mode=disable \
  --windows-icon-from-ico=icon.ico \
  --enable-plugin=pyside6 \
  --company-name="Deco - decospdl@gmail.com" \
  --product-name="RO Tools" \
  --product-version=1.6.1.0 \
  main.py

cp servers.json dist/
cp -r assets/ dist/assets
cd dist
powershell -Command "Compress-Archive -Path RO_Tools.exe,servers.json,assets -DestinationPath RO_Tools_v1.6.1.0.zip"
cd ..