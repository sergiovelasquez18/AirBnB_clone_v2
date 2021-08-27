#!/usr/bin/env bash
#script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
sed -i "47 a \\tlocation /hbnb_static {\n\talias /data/web_static/current/;\n\tautoindex off;\n\t}\n" /etc/nginx/sites-available/default
service nginx restart
