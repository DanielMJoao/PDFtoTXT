# PDFtoTXT
One file executable to convert PDF to TXT

# How does it work?
PDFtoTXT.exe converts all PDF files from the folder that it is located to a TXT file with the same name on the "PDFtoTXT_Convertidos" folder. As simple as that.
The executable version works without any installation required, but if you want to rebuild it on Python3.8 please follow the steps bellow.

# Install
Git clone it, create venv and then:
>pip install requirements.txt

# How to build the executable file
>pyinstaller --onefile PDFtoTXT.py
