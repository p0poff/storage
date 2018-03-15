from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
from flask import abort
import helper
app = Flask(__name__)
port = 80
debug = False

@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>')
def catch_all(path):
	w = helper.work()
	return w.sendError('error')

@app.route('/upload/key/<key>',  methods=['POST'])
def upload(key):
	file = request.files
	w = helper.work(data=file, key=key)
	return w.upload() if w.valid() else w.sendError('error valid key')

@app.route('/get/key/<key>/name/<name>',  methods=['GET'])
def get(key, name):
	w = helper.work(key=key)
	return w.get(name) if w.valid() else w.sendError('error valid key')

@app.route('/del/key/<key>/name/<name>',  methods=['GET'])
def delete(key, name):
	w = helper.work(key=key)
	return w.delete(name) if w.valid() else w.sendError('error valid key')

# @app.route('/upload',  methods=['GET'])
# def form():
# 	return render_template('form.html')

@app.route('/img/<path:path>',  methods=['GET'])
def resize(path):
	w = helper.work()
	args = w.parseNameForResize(path)
	_type, _file = w.resize(args=args)
	if _type == 'error':
		abort(404)
	else:
		return send_file(_file, mimetype=w.getImgType(_type))

if __name__ == '__main__':
	app.debug = debug
	app.run(host='0.0.0.0', port=port)