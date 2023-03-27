from setuptools import setup

#写一个基于py2app的setup.py文件，用于打包Aisttant_UI_agent.py文件，依赖openai和PyQt5, 并且将图标文件一起打包 
setup(
    app=['Aistant_UI_agent.py'],
    data_files=['216180_text_document_icon.icns'],
    options={
        'py2app': {
            'iconfile': '216180_text_document_icon.icns',
            'argv_emulation': True,
            'includes': ['openai', 'PyQt5', 'json', 'time', 'os', 'sys', 'threading']
        }
    },
    setup_requires=['py2app'],
)



# APP = ['Aistant_UI_agent.py']
# DATA_FILES = []
# OPTIONS = {
#     'iconfile': '8666753_message_circle_chat_icon.icns',
#     'argv_emulation': True,
# }

# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     setup_requires=['py2app'],
# )