# Eldessouky-Labels.spec
# ملف إعداد PyInstaller المضمون لتطبيق tkinter/customtkinter

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('C:\\hostedtoolcache\\windows\\Python\\3.11.*/x64\\Lib\\tkinter', 'tkinter'),
        ('C:\\hostedtoolcache\\windows\\Python\\3.11.*/x64\\Lib\\site-packages\\customtkinter', 'customtkinter'),
    ],
    hiddenimports=['tkinter', 'customtkinter', 'PIL'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Eldessouky-Labels',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='Icon.ico'  # احذف السطر لو مش عندك أيقونة
)
