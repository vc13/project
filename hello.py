import os
from flask import Flask, request, redirect, url_for
from test import init

app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def hello():
	if request.method == 'POST':
		file = request.files['file']
		file.save('hello.mp3')
		init(mp3_file = 'hello.mp3')
		return '''<html><head></head><body><img src="hello.png"></body></html>'''
	else:
		return "Get World"

if __name__ == "__main__":
    app.run()
