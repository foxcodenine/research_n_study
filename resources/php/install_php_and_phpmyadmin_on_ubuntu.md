How to Install PHP 8 and phpmyadmin on Ubuntu

https://www.cloudbooklet.com/how-to-install-php-8-on-ubuntu/
https://www.youtube.com/watch?v=vazRx1Ei8VA

### NB: There is a more UPDATED version at the lunux folder: ubuntu_fresh_install.md

### Getting Started

    $ sudo apt update
    $ sudo apt upgrade


### Add PPA for PHP 8
    $ sudo apt install software-properties-common
    $ sudo add-apt-repository ppa:ondrej/php
    $ sudo apt update

CAVEATS:
1. If you are using php-gearman, you need to add ppa:ondrej/pkg-gearman
2. If you are using apache2, you are advised to add ppa:ondrej/apache2
3. If you are using nginx, you are advised to add ppa:ondrej/nginx-mainline
   or ppa:ondrej/nginx


### Install PHP 8 for Apache

    $ sudo apt install php8.0

### Install PHP 8 Extensions

    $ sudo apt install php8.0-common php8.0-mysql php8.0-xml php8.0-curl php8.0-gd php8.0-imagick php8.0-cli php8.0-dev php8.0-imap php8.0-mbstring php8.0-opcache php8.0-soap php8.0-zip -y

    $ sudo service apache2 restart

### Configure PHP 8 for Apache

    $ sudo nano /etc/php/8.0/apache2/php.ini

Hit F6 for search inside the editor and update the following values for better performance.

    upload_max_filesize = 32M 
    post_max_size = 48M 
    memory_limit = 256M 
    max_execution_time = 600 
    max_input_vars = 3000 
    max_input_time = 1000


    $ sudo service apache2 restart


### installing phpmyadmin

    $ sudo apt install phpmyadmin


you need to uncomment a line in php.ini:

    $ sudo nano /etc/php/8.0/apache2/php.ini

    find ;  extension=mysqli ans remove the ; to uncomment it

and write a line at the end of apache2.conf

    $ sudo nano /etc/apache2/apache2.conf 

    go to the end and add the following:

    Include /etc/phpmyadmin/apache.conf

and restart apache

    $ sudo service apache2 restart


### to show error messages

https://www.youtube.com/watch?v=0wIUci7s3gM

    $ sudo nano /etc/php/8.0/apache2/php.ini

    find:

        error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT

    and change it to:
    
        error_reporting = E_ALL 

    and also find:

        display_errors = Off

    and change it to:

        display_errors = On

    Save and restart apache

        $ sudo service apache2 restart



### to opne from a Built-in web server
follow:
https://www.php.net/manual/en/features.commandline.webserver.php