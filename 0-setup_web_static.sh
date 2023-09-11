#!/usr/bin/env bash
#A bash script that sets up your web servers for the deployment of web_static

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "My test Configuration" | sudo tee /data/web_static/releases/test/index.html
sudo rm -f /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen \[::\]:80 default_server;/a \\n\tlocation /hbnb_static/ { \n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default

sudo service nginx restart
