# Puppet for setup
exec {'web_static':
  command  => 'sudo apt-get -y update && sudo apt-get -y install nginx && sudo service ngnix start && sudo mkdir -p /data/ && /data/web_static && /data/web_static/releases/shared/ && /data/web_static/releases/test/ && sudo echo "Holberton School" | tee /data/web_static/releases/test/index.html && ln -sf /data/web_static/releases/test/ /data/web_static/current && chown -R ubuntu:ubuntu /data/ && var="location /hbnb_static {\n alias /data/web_static/current/;\n}\n" && sudo sed -i "43i$var" /etc/nginx/sites-available/default && service nginx restart',
  provider => 'shell'
}
