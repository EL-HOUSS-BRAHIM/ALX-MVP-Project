#!/bin/bash

# Update package repositories
sudo apt-get update

# Install Nginx
sudo apt-get install -y nginx

# Install MySQL
sudo apt-get install -y mysql-server

# Secure MySQL installation
sudo mysql_secure_installation

# Install Python3 and pip3
sudo apt-get install -y python3 python3-pip

# Install Flask and its dependencies
pip3 install flask flask-sqlalchemy flask-bcrypt pyjwt

# Install Node.js and npm
sudo apt-get install -y nodejs npm

# Install React and its dependencies
sudo npm install -g create-react-app
sudo npm install react-router-dom axios

# Install PHP and its dependencies
sudo apt-get install -y php-fpm php-mysql

# Install phpMyAdmin
sudo apt-get install -y phpmyadmin
sudo ln -s /usr/share/phpmyadmin /var/www/html/phpmyadmin

# Install HAProxy
sudo apt-get install -y haproxy

# Generate self-signed SSL certificate using HAProxy
sudo mkdir -p /etc/haproxy/ssl
sudo chmod 700 /etc/haproxy/ssl
sudo openssl req -new -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/haproxy/ssl/haproxy.pem -out /etc/haproxy/ssl/haproxy.pem

# Configure HAProxy for SSL termination and HTTPS enforcement
sudo tee /etc/haproxy/haproxy.cfg >/dev/null <<EOF
global
    log /dev/log local0
    log /dev/log local1 notice
    chroot /var/lib/haproxy
    stats socket /run/haproxy/admin.sock mode 660 level admin expose-fd listeners
    stats timeout 30s
    user haproxy
    group haproxy
    daemon

defaults
    log global
    mode http
    option httplog
    option dontlognull
    timeout connect 5000
    timeout client 50000
    timeout server 50000

frontend http
    bind *:80
    redirect scheme https code 301 if !{ ssl_fc }

frontend https
    bind *:443 ssl crt /etc/haproxy/ssl/haproxy.pem
    default_backend servers

backend servers
    server server1 127.0.0.1:3000 check
    server server2 127.0.0.1:5000 check
EOF

sudo systemctl restart haproxy

# Configure Nginx to proxy requests to HAProxy
sudo rm /etc/nginx/sites-enabled/default
sudo tee /etc/nginx/conf.d/proxy.conf >/dev/null <<EOF
server {
    listen 80;
    server_name 146.190.150.212;
    location / {
        proxy_pass http://127.0.0.1:443;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

sudo systemctl restart nginx

# Start Flask development server
cd /root/ALX-MVP-Project/backend
flask run --host=0.0.0.0 &

# Start React development server
cd /root/ALX-MVP-Project/frontend
npm start &

echo "Installation and configuration completed successfully."
