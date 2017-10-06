# Virtual Host configuration for example.com
#
# You can move that to a different file under sites-available/ and symlink that
# to sites-enabled/ to enable it.
#
server {
	listen 80;
        ## listen [::]:80;

	server_name ssat-nms-vm7.cisco.com;

	## root /var/www/example.com;
	## index index.html;

	location /static {
		alias /home/ubuntu-mkwok/sites/ssat-nms-vm7.cisco.com/static;
	}

	location / {
                proxy_set_header Host $host;
		## proxy_pass http://localhost:8000;
		proxy_pass http://unix:/tmp/ssat-nms-vm7.cisco.com.socket;
	}
}
