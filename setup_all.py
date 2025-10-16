import os

files = {
    "main.py": """<main.py code here>""",
    "requirements.txt": """tkinter
pywin32
Pillow
pyinstaller
""",
    "build_script.bat": """@echo off
echo ===============================
echo   تحويل البرنامج إلى EXE ...
echo ===============================
pyinstaller --onefile --windowed --icon=icon.ico --name="صيدلية الدسوقي Labels" main.py
echo.
echo ✅ تم الإنشاء! الملف التنفيذي داخل مجلد dist
pause
""",
    "README.txt": """تشغيل المشروع:
1. نزل الملفات كلها.
2. شغل build_script.bat لتحويله إلى EXE.
3. الناتج سيكون في مجلد dist باسم صيدلية الدسوقي Labels.exe
""",
}

os.makedirs("Dessouky_Labels", exist_ok=True)
for name, content in files.items():
    with open(os.path.join("Dessouky_Labels", name), "w", encoding="utf-8") as f:
        f.write(content)

print("✅ تمت إضافة ملفات المشروع في مجلد Dessouky_Labels")
