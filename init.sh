sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
gunicorn -b 0.0.0.0:8080 web.hello:app &
cd ~/web/ask/ask/
gunicorn -b 0.0.0.0:8000 wsgi
