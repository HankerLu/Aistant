del build

del dist

PyInstaller -D Aistant_v3.py --icon aistant.ico -n Aistant_dev_v3.4

copy *.ico dist\Aistant_dev_v3.4

copy *.icns dist\Aistant_dev_v3.4