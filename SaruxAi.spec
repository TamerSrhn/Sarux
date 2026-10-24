# -*- mode: python ; coding: utf-8 -*-
from pathlib import Path

from PyInstaller.utils.hooks import collect_all


ROOT = Path(SPECPATH).resolve()
datas = [
    (str(ROOT / "core" / "prompt.txt"), "core"),
    (str(ROOT / "Saruxpengu.jpg"), "."),
    (str(ROOT / "saruxpengukonus.jpg"), "."),
]
binaries = []
hiddenimports = []
google_datas, google_binaries, google_hiddenimports = collect_all("google.genai")
datas += google_datas
binaries += google_binaries
hiddenimports += google_hiddenimports

a = Analysis(
    [str(ROOT / "main.py")],
    pathex=[str(ROOT)],
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
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="SaruxAi",
    icon=str(ROOT / "sarux.ico"),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
