Provisioning a new site
=======================

## Required packages:

* nginx
* python 3
* git
* pip3
* virtualenv

eg, on Ubuntu

	sudo apt-get install nginx git python3 python3-pip
	sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, ssat-nms-vm7.cisco.com

## Folder structure:
Assume we have a user account at /home/username

ubuntu-mkwok@ssat-nms-vm7:~$ tree -L 3
.
└── sites
    └── ssat-nms-vm7.cisco.com
        ├── database
        ├── source
        ├── source_dummy
        ├── static
        └── virtualenv

