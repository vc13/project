import os
from flask import Flask, request, redirect, url_for
from test import init
from flask import send_file

app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET','POST'])
def hello():
	if request.method == 'POST':
		print "Got Request"
		file = request.files['file']
		file.save('hello.wav')
		init(mp3_file = 'hello.wav')
		return send_file('hello.png', mimetype='image/png')
	else:
		return "Get World"

if __name__ == "__main__":
    # app.run()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
