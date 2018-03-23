import hashlib
import os
import fnmatch

class files:
	def __init__(self, name):
		self.BASEPATH = os.environ.get('BASEPATH', '/app/img')
		self.SITEPATH = os.environ.get('SITEPATH', '/img')
		self.DOMAIN = os.environ.get('DOMAIN', 'http://example.domain')
		self.__name = name

	def __getMD5DirName(self):
		m = hashlib.md5()
		m.update(self.__name.encode('utf-8'))
		return m.hexdigest()[0:3]

	def getPathFile(self, subFile=False):
		return '%s%s' % (self.getPath(), self.__name if subFile == False else subFile)

	def getPathFileResize(self, w, h):
		_name = self.__name.split('.')
		return '%s%s-w%s-h%s.%s' % (self.getPath(), _name[0], w, h, _name[1])

	def getPath(self):
		return '%s/%s/' % (self.BASEPATH, self.__getMD5DirName())

	def getSitePathFile(self):
		return '%s%s/%s/%s' % (self.DOMAIN, self.SITEPATH, self.__getMD5DirName(), self.__name)

	def isPath(self):
		return os.path.exists(self.getPath())

	def isFile(self, subFile=False):
		return os.path.exists('%s/%s' % (self.getPath(), self.__name if subFile == False else subFile))

	def createDir(self, directory):
		if not os.path.exists(directory):
			os.makedirs(directory)

	def deleteFile(self, subFile=False):
		if self.isFile(subFile):
			os.remove(self.getPathFile(subFile))

	def getListResizeFilesToDir(self):
		def getPattern():
			pattern = '%s-w*' % (self.__name[:-4])
			return pattern
		listOfFiles = os.listdir(self.getPath())  
		pattern = getPattern()
		return [x for x in listOfFiles if fnmatch.fnmatch(x, pattern)]


def test():
	f = files('ubuntu-43794-2560x1600.jpg')
	print(f.getPath())
	print(f.getPathFile())
	l = f.getListResizeFilesToDir()
	print(l)
	f.deleteFile(l[0])
if __name__ == '__main__':
	test()


