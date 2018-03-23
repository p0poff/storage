FROM tiangolo/uwsgi-nginx-flask:flask-python3.5-index

COPY /app /app/
RUN pip install pillow-simd

COPY nginx.conf /etc/nginx/conf.d/nginx.conf
