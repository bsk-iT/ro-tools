version_str = "1.4.0"
name = "RO Tools"

version_parts = tuple(map(int, (version_str.split(".") + ["0", "0"])[:4]))

version_txt_content = f"""VSVersionInfo(
  ffi=FixedFileInfo(
    filevers={version_parts},
    prodvers={version_parts},
    mask=0x3f,
    flags=0x0,
    OS=0x4,
    fileType=0x1,
    subtype=0x0,
    date=(0, 0)
  ),
  kids=[
    StringFileInfo([
      StringTable(
        '040904B0',
        [
          StringStruct('CompanyName', 'Deco - uniaodk@gmail.com'),
          StringStruct('FileDescription', '{name}'),
          StringStruct('FileVersion', '{version_str}'),
          StringStruct('InternalName', '{name}'),
          StringStruct('OriginalFilename', '{name}.exe'),
          StringStruct('ProductName', '{name}'),
          StringStruct('ProductVersion', '{version_str}')
        ]
      )
    ]),
    VarFileInfo([VarStruct('Translation', [1033, 1200])])
  ]
)
"""
with open("version.txt", "w", encoding="utf-8") as f:
    f.write(version_txt_content)
