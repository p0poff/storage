# storage
images storage with resize

# build
docker build -t python-flask-storage .
docker run --name storage -v /home/data:/app/img -e DOMAIN="http://domain.com" -e ACCESSKEY="secretword" -d -p 80:80 python-flask-storage

> **/home/data** - _your local storage directory_

# Environment variables

* DOMAIN - _your domain name_
* ACCESSKEY - _secret word to access to GET, UPLOAD, DELETE options_


