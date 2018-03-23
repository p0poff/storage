# docs - http://python-lab.ru/documentation/27/stdlib/unittest.html
import unittest
import sys
sys.path.append("../app")
import helper
import files
import main
import os

class Test(unittest.TestCase):
	# hello world
	def test_hello(self):
		self.assertEqual('%s - %s' % ('hello', 'world'), 'hello - world')
############################FILES#####################################
	def test_get_path_md5(self):
		f = files.files('test.jpg')
		self.assertEqual(f.getPathFile(), '/app/img/041/test.jpg')	

	#путь должен быть как в докере
	def test_base_path(self):
		f = files.files('test.jpg')
		self.assertEqual(f.BASEPATH, '/app/img')			

	#не должно быть папки /app/img
	def test_is_folder_img(self):
		self.assertEqual(os.path.isdir("../app/img"), False)
		

############################MAIN#######################################
	def test_not_is_form(self):	
		self.assertFalse('form' in dir(main))

	def test_server_param(self):
		self.assertEqual(main.port, 80)
		self.assertEqual(main.debug, False)

	def test_catch_all(self):
		self.assertEqual(main.catch_all(''), 'error')

if __name__ == '__main__':
	unittest.main()