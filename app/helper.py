import files
from PIL import Image
import PIL
from flask import send_file
import resize
import re
import os
class work:
	def __init__(self, **args):
		self.__validKey = os.environ.get('ACCESSKEY', 'access key')
		self.__data = args.get('data', False)
		self.__key = args.get('key', '')

	def sendError(self, text):
		return text

	def send(self, text):
		return text

	def valid(self):
		return self.__key == self.__validKey

	def get(self, name):
		f = files.files(name)
		return self.send(f.getSitePathFile())

	def upload(self):
		filename = self.__data['fileToUpload'].filename
		if len(filename)==0:
			return self.sendError('is no file')
		self.delete(filename)
		f = files.files(filename)
		if f.isPath() == False:
			f.createDir(f.getPath())
		curFile = f.getPathFile()
		self.__data['fileToUpload'].save(curFile)
		return self.send(f.getSitePathFile())

	def resize(self, **args):
		name = args['args'].get('name', 'none')
		w = args['args'].get('w', 0)
		h = args['args'].get('h', 0)
		f = files.files(name)
		if f.isFile():
			img = Image.open(f.getPathFile())
			newSize = resize.getNewSize(img.size, w=w, h=h)
			img.resize(newSize, PIL.Image.BICUBIC).save(f.getPathFileResize(w, h))
			return img.format, f.getPathFileResize(w, h)	
		else:
			return 'error', ''

	def parseNameForResize(self, name):
		# парсим строку типа ddb/ubuntu-43794-2560x1600-w90-h50.jpg
		d = {}
		patern = re.compile('.*-w(\\d+)-h(\\d+).*', re.VERBOSE)
		m = patern.findall(name)
		if len(m)>0:
			d['w'] = m[0][0]
			d['h'] = m[0][1]
		else:
			d['w'] = '0'
			d['h'] = '0'
		d['name'] = name[4:].replace('-w%s-h%s' % (d['w'], d['h']), '')
		return d


	def getImgType(self, _type):
		d = {}
		d['JPEG'] = 'image/jpeg'
		d['PNG'] = 'image/png'
		d['GIF'] = 'image/gif'
		return d.get(_type, 'none')

	def delete(self, name):
		f = files.files(name)
		f.deleteFile()
		# delete sub files
		lSubFiles = f.getListResizeFilesToDir()
		for __file in lSubFiles:
			f.deleteFile(__file)
		return 'ok'

