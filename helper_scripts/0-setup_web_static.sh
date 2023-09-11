#!/usr/bin/env bash
#A bash script that installs and configures nginx webserver
#This script checks if nginx is already installed or not.
#	If already installed, the script will not install
#	nginx but will only configure nginx with below
#	requirements.
#	If not installed, the script will install and con-
#	figure nginx with below requirements

configure_nginx () {
	sudo mkdir -p /data/
	sudo mkdir -p /data/web_static/
	sudo mkdir -p /data/web_static/releases/
	sudo mkdir -p /data/web_static/shared/
	sudo mkdir -p /data/web_static/releases/test/
	echo "My test Configuration" | sudo tee /data/web_static/releases/test/index.html
	sudo rm -f /data/web_static/current
	sudo ln -s /data/web_static/releases/test/ /data/web_static/current
	sudo chown -R ubuntu:ubuntu /data/
	sudo sed -i '/index   index.html index.htm;/a \\n\tlocation /hbnb_static/ { \n\talias /data/web_static/current/;\n\t}' /etc/nginx/sites-enabled/default
}

if command -v nginx &> /dev/null
then
	configure_nginx
	sudo service nginx restart
else
	sudo apt-get update
	sudo apt-get -y install nginx
	sudo service nginx start
	configure_nginx
	sudo service nginx restart
fi
