#!/usr/bin/env bash
# make ur web server works
dpkg -l | grep nginx > /dev/null 2>&1 || sudo apt -y update && sudo apt -y upgrade && sudo apt -y install nginx
ls /data/web_static/releases/test/ > /dev/null 2>&1 || sudo mkdir /data/web_static/releases/test/
ls /data/web_static/shared/ > /dev/null 2>&1 || sudo mkdir /data/web_static/shared/

echo "abdellah" > /data/web_static/releases/test/index.html

sudo rm -r /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu /data/

sudo sed -i '/server_name _;/a \\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

sudo service restart nginx
