# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['webhook.py'],
    pathex=[],
    binaries=[],
    datas=[('img\\streamdeck_key1-alert.png', '.'), ('img\\streamdeck_key1.png', '.'), ('img\\streamdeck_key2-alert.png', '.'), ('img\\streamdeck_key2.png', '.'), ('img\\streamdeck_key3-alert.png', '.'), ('img\\streamdeck_key3.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='webhook',
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
