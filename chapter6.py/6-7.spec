# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:/Users/82105/cv/chapter6.py/6-7.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/82105/cv/chapter6.py/nose.png', '.'), ('C:/Users/82105/cv/chapter6.py/xmas.jpg', '.'), ('C:/Users/82105/cv/chapter6.py/readme_6-5.md', '.'), ('C:/Users/82105/cv/chapter6.py/readme_6-7.md', '.'), ('C:/Users/82105/cv/chapter6.py/6-5.py', '.'), ('C:/Users/82105/cv/chapter6.py/6-7.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='6-7',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
