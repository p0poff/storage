# storage
images storage with resize

# build
docker build -t python-flask-storage .
docker run --name storage -v /home/data:/app/img -d -p 80:80 python-flask-storage
