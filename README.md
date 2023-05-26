# image-to-text-desktop 
- create a virtual environment in your term or cmd:

`$ python3 -m venv venv`

- activate the virtual environment

`$ source venv/bin/activate`

- install the requirements

`$ pip install -r requirements.txt`

- install tesseract-orc from: https://tesseract-ocr.github.io/tessdoc/Installation.html

- in ubuntu use

`$ sudo apt install tesseract-ocr`
`$ sudo apt install libtesseract-dev`

- in macOS

`$ sudo port install tesseract`

- in windows go to the https://github.com/UB-Mannheim/tesseract/wiki and download the .exe

- then compile the app running in your term or cmd:

`$ pyinstaller --windowed --onefile main.py`

- go to the dist folder and run the app with double click

