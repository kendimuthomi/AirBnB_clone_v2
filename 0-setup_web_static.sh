#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static

#installing nginx
sudo apt-get -y update
sudo apt-get -y install nginx

# creating folders
sudo mkdir -p /data/web_static/releases/test/ /data/web-static/shared/

# adding test string
echo "<h2>www.realkendimuthomi.tech Let's GOOO!</h2>" > /data/web_static/releases/test/index.html

#creating a symbolic link
sudo rm -rf /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# changing ownership of the folder /data/
sudo chown -hR ubuntu:ubuntu /data/

# using sed and alias to update nginx configuration
sudo sed -i '48i \\tlocation \/hbnb_static/ {\n\t\t alias /data/web_static/current/;\n\t}' /etc/nginx/sites-available/default

#restarting nginx
sudo service nginx restart
