

def getNewSize(size, **args):
	try:
		w = int(args.get('w', 0))
		h = int(args.get('h', 0))
	except:
		raise Exception('error getNewSize', 'parameters is no integers')
	
	if w==0 and h==0:
		raise Exception('error getNewSize', 'have no parameters')

	try:
		isLen2 = len(size) == 2
	except:
		isLen2 = False
	if not isLen2:
		raise Exception('error getNewSize', 'no SIZE')
	
	try:
		intSize = (int(size[0]), int(size[1]))
	except:
		raise Exception('error getNewSize', 'size tuple is no integers')

	if w > 0 and h > 0:
		return w, h

	fW = lambda x,y,h: int(x*h/y)
	fH = lambda x,y,w: int(y*w/x)

	if w==0:
		return fW(intSize[0], intSize[1], h), h

	if h==0:
		return w, fH(intSize[0], intSize[1], w)

	raise Exception('error getNewSize', 'parameters low zero')

def test():
	print(getNewSize((600, '300'), h='200', w=40))


if __name__ == '__main__':
	test()
