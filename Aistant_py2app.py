from setuptools import setup

APP = ['Aistant_UI_agent.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': '8666753_message_circle_chat_icon.icns',
    'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)