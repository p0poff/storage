FROM tiangolo/uwsgi-nginx-flask:flask-python3.5-index

COPY /app /app/
COPY entrypoint.sh /
RUN chmod 744 /entrypoint.sh
RUN pip install pillow-simd

COPY nginx.conf /etc/nginx/conf.d/nginx.conf
