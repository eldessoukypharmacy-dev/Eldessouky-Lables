@echo off
echo ===============================
echo جاري إنشاء ملف EXE للبرنامج...
echo ===============================
pyinstaller --onefile --windowed --icon=icon.ico --name="صيدلية الدسوقي Labels" main.py
echo --------------------------------
echo تم إنشاء الملف داخل مجلد dist
pause
