# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all
from PyInstaller.utils.hooks import copy_metadata
import sys
import os

datas = [('ikony', 'ikony')]

# Zabezpieczenie dodające ikony fizycznie do folderu _internal
if os.path.exists('icon.ico'):
    datas.append(('icon.ico', '.'))
if os.path.exists('icon.icns'):
    datas.append(('icon.icns', '.'))

binaries = []
hiddenimports = []

datas += copy_metadata('pymatting')
datas += copy_metadata('rembg')

tmp_ctk = collect_all('customtkinter')
datas += tmp_ctk[0]; binaries += tmp_ctk[1]; hiddenimports += tmp_ctk[2]

tmp_rembg = collect_all('rembg')
datas += tmp_rembg[0]; binaries += tmp_rembg[1]; hiddenimports += tmp_rembg[2]

a = Analysis(
    ['PyPhoto.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

# Dynamiczne ładowanie głównej ikony programu
icon_file = 'icon.ico' if sys.platform == 'win32' else 'icon.icns'
if not os.path.exists(icon_file):
    icon_file = None

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyPhoto',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_file,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyPhoto',
)

if sys.platform == 'darwin':
    app = BUNDLE(
        coll,
        name='PyPhoto.app',
        icon='icon.icns' if os.path.exists('icon.icns') else None,
        bundle_identifier='com.danielkaliski.pyphoto',
        info_plist={
            'NSHighResolutionCapable': 'True', 
            'LSBackgroundOnly': 'False',
            'CFBundleName': 'PyPhoto',
            'CFBundleDisplayName': 'PyPhoto Editor',
            'CFBundleVersion': '1.0.0',
            'CFBundleShortVersionString': '1.0.0',
            'NSRequiresAquaSystemAppearance': 'False',
            'NSHumanReadableCopyright': 'Copyright © 2026 Daniel Kaliski. All rights reserved.',
        },
    )