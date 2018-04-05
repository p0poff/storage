import requests
URL = 'http://example.com'
SECRETKEY = 'secret_key'

def send(fName):
    f = open(fName, 'rb')
    files = {'fileToUpload': (fName, f)}
    url = '%s/upload/key/%s' % (URL, SECRETKEY)
    response = requests.post(url, files=files)
    return response.text

def main():
    print(send('cat.jpg'))

if __name__ == '__main__':
    main()