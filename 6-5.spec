# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['chapter6.py\\6-5.py'],
    pathex=[],
    binaries=[],
    datas=[('chapter6.py/nose.png', '.'), ('chapter6.py/xmas.jpg', '.'), ('chapter6.py/readme_6-5.py', '.'), ('chapter6.py/readme_6-7.py', '.'), ('chapter6.py/6-5.py', '.'), ('chapter6.py/6-7.py', '.')],
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
    name='6-5',
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
