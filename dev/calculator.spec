# -*- mode: python ; coding: utf-8 -*-
import os
import pathlib
import sys

sys.path.insert(0, os.path.abspath('src'))

from calculator import metadata as meta


# WINDOWS EXECUTABLE INFO
# =======================
INFO = f"""VSVersionInfo(
ffi=FixedFileInfo(
filevers={tuple(map(int, meta["version"][1:].split('.') + [0]))},
prodvers={tuple(map(int, meta["version"][1:].split('.') + [0]))},
mask=0x3f,
flags=0x0,
OS=0x40004,
fileType=0x1,
subtype=0x0,
date=(0, 0)
),
kids=[
StringFileInfo(
  [
  StringTable(
    '040904B0',
    [
      StringStruct('CompanyName', 'calculator'),
      StringStruct('FileDescription', 'calculator {meta['version']}'),
      StringStruct('LegalCopyright', '\251 {meta["copyright"]}'),
      StringStruct('LegalTrademarks', '{meta["license"]}'),
      StringStruct('OriginalFilename', 'calculator.exe'),
      StringStruct('ProductName', 'calculator Graphical-User Interface'),
      StringStruct('ProductVersion', '{meta['version']} ({meta['status']})')
    ]
  )
  ]),
VarFileInfo([VarStruct('Translation', [0x409, 0])])
]
)"""


def generate_rc():
    with open("dev/.pyinstaller.rc", 'w', encoding='utf-8') as file:
        file.write(INFO)
    return ".pyinstaller.rc"


# PYINSTALLER
# ===========
BLOCK_CIPHER = None


analysis = Analysis(['../src/calculator/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[
        ("../src/", "src/"),
        ("../src/calculator/gui/img/", "src/calculator/gui/img/"),
        ("../src/calculator/gui/uis/", "src/calculator/gui/uis/"),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=BLOCK_CIPHER,
    noarchive=False,
)


pyz = PYZ(
    analysis.pure,
    analysis.zipped_data,
    cipher=BLOCK_CIPHER,
)


exe = EXE(
    pyz,
    analysis.scripts,
    [],
    exclude_binaries=True,
    name='calculator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon="../src/calculator/gui/img/pypi.ico",
    version=generate_rc(),
)


coll = COLLECT(
    exe,
    analysis.binaries,
    analysis.zipfiles,
    analysis.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='calculator',
)


# remove temporary windonws file info
os.remove("dev/.pyinstaller.rc")
