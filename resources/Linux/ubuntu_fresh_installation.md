### Installing Visual Studio Code on Debian
    download vscode .deb file from vscode site
    cd to folder

    $ sudo hapt update
    $ sudo apt install ./code*.deb

    if you get the following when $ sudo apt-get update

    N: Skipping acquire of configured .... doesn't support architecture 'arm64'
    N: Skipping acquire of configured .... 'armhf'

    edit: /etc/apt/sources.list.d/vscode.list. 
    Remove any unwanted architectures from between the brackets and it should end up like this:

    deb [arch=amd64] http://packages.microsoft.com/repos/vscode stable main

<!-- --------------------------------------------------------------- -->
##
### How to stop Nemo 20.04 (Ubuntu Budgie 20.04) double-click behavior
    $ gsettings set org.nemo.preferences click-double-parent-folder false

    $ sudo gsettings set org.nemo.preferences click-double-parent-folder false

<!-- --------------------------------------------------------------- -->
##

### Ubuntu - Install Fira Code Font

    $ sudo apt install fonts-firacode

<!-- --------------------------------------------------------------- -->
##
### Install Grub Customizer in Ubuntu 20.04 LTS
    
    $ sudo apt update
    $ sudo apt install grub-customizer

<!-- --------------------------------------------------------------- -->
##

### Rebinding Alt+Q

    $ /usr/share/budgie-extras-daemon

Find "tilix_alt.bde" and edit line:

    shortcut=<Alt>Q

I have changed it to:

    shortcut=<Alt>T

by:

    $ sudo nano tilix_alt.bde

And restart pc


<!-- --------------------------------------------------------------- -->
##
    

### install git

    $ sudo apt install git

### github ssh authentication

    $ cd ~/git
    $ git config --global user.email "foxcode9@gmail.com"
    $ git config --global user.name "chris"

    $ cd ~/.ssh or mkdir ~/.shh   (and cd to it)

    $ ssh-keygen -t rsa -C "foxcode9@gmail.com"

    press enter to accept the default file
    enter passphrase

    $ ls -al
    $ code id_rsa.pub

    copy content and go to your git account. Go to settings. 
    Select SSH and GPG keys, currently at the side menu

    New SSH key

    Enter a Title and in the Key past the id_rsa.pub content 

    Ass SSH key


<!-- --------------------------------------------------------------- -->
##

### install python
    $ sudo apt-get update
    $ sudo apt-get install python3.9

    $ sudo apt install python3-pip

    $ pip3 install pipenv


<!-- --------------------------------------------------------------- -->
##

### Change the Python3 default version in Ubuntu

    $ sudo update-alternatives --config python

Will show you an error:

    $ update-alternatives: error: no alternatives for python3 

You need to update your update-alternatives , then you will be able to set your default python version, Assign the different version with different numbers .

    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1
    $ sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2

Then run :

    $ sudo update-alternatives --config python

    and select the assigned number to set it as default 

then update new config for python3

    $ sudo update-alternatives --config python3

Finally, check default python3 version:

    $ python3 --version

<!-- --------------------------------------------------------------- -->
##

Install npm on Ubuntu

    $ sudo apt install npm nodejs
    $ npm --version

<!-- --------------------------------------------------------------- -->
##

### install Live server

    $ sudo npm install -g live-server

<!-- --------------------------------------------------------------- -->
##

### Install MySQL on Ubuntu 20.04
// https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql

    $ sudo apt install mysql-server

Configuring MySQL

    $ sudo mysql_secure_installation  

Creating a Dedicated MySQL User and Granting Privileges  

    $ sudo mysql -u root   
    
    OR  

    $ sudo mysql -u root -p 
    *******

     

    mysql> CREATE USER username@localhost IDENTIFIED BY 'password';
    mysql> GRANT ALL PRIVILEGES ON * . * TO username@localhost;
    mysql> FLUSH PRIVILEGES;
    mysql> sSELECT host, user FROM mysql.user;



    --------------------------------------------------------------

    if MySQL – ERROR 1819 (HY000): Your password does not satisfy the current policy requirements

    mysql> Show variables like 'validate_password%';

    mysql> SET GLOBAL validate_password_length = 6; 
    mysql> SET GLOBAL validate_password_number_count = 0; 
    mysql> SET GLOBAL validate_password.policy = LOW;

    --------------------------------------------------------------

<!-- --------------------------------------------------------------- -->
##

### Installing Brave Browser

https://brave.com/linux/


<!-- --------------------------------------------------------------- -->
##

### Installing Daedalus (Mainnet) on Linux

1. Download the installer from the offical website.

    https://daedaluswallet.io/

2. Open a terminal, navigate to the folder where you saved the installer
and give executable permissions to the installer: 

    $ chmod +x ./daedalus-2.2.0-mainnet-14276.bin.

3. Run the installer (for example): 

    $ ./daedalus-2.2.0-mainnet-14276.bin. ...
    
After doing that try running the installer again.

<!-- --------------------------------------------------------------- -->
##

### Install Apache2
https://ubuntu.com/tutorials/install-and-configure-apache#2-installing-apache
 
    $ sudo apt update
    $ sudo apt install apache2

### Install php8
https://linuxize.com/post/how-to-install-php-8-on-ubuntu-20-04/

Enabling PHP Repository

    $ sudo apt install software-properties-common
    $ sudo add-apt-repository ppa:ondrej/php
    

Installing PHP 8.0 with Apache

    $ sudo apt update
    $ sudo apt install php8.0 libapache2-mod-php8.0

    $ sudo systemctl restart apache2

Configure Apache with PHP-FPM

    $ sudo apt update
    $ sudo apt install php8.0-fpm libapache2-mod-fcgid

    By default PHP-FPM is not enabled in Apache. To enable it, run:

    $ sudo a2enmod proxy_fcgi setenvif
    $ sudo a2enconf php8.0-fpm

    $ systemctl restart apache2

Installing PHP extensions

    PHP extensions are compiled libraries that extend the core functionality of PHP. 
    Extensions are available as packages and can be easily installed with apt :

    sudo apt install php8.0-[extname]

    the following are commen extentions:

        $ sudo apt install php8.0-common php8.0-mysql php8.0-xml php8.0-curl php8.0-gd php8.0-imagick php8.0-cli php8.0-dev php8.0-imap php8.0-mbstring php8.0-opcache php8.0-soap php8.0-zip -y

        $ sudo service apache2 restart

Testing PHP Processing

    To test whether the web server is configured properly for PHP processing, 
    create a new file named info.php inside the /var/www/html directory with 
    the following code:

        /var/www/html/info.php

            <?php

            phpinfo();

    visit: http://your_server_ip/info.php

<!-- --------------------------------------------------------------- -->
##

### Configure PHP 8 for Apache
https://docs.presscustomizr.com/article/171-fixing-maximum-upload-and-php-memory-limit-issues

    $ sudo nano /etc/php/8.0/apache2/php.ini

    Hit F6 for search inside the editor and update the following values for better performance.

    upload_max_filesize = 32M 
    post_max_size = 48M 
    memory_limit = 256M 
    max_execution_time = 600 
    max_input_vars = 3000 
    max_input_time = 1000


    $ sudo service apache2 restart


<!-- --------------------------------------------------------------- -->
##





### Setup email Geary

For yahoo:
    Generate and manage third-party app passwords
    https://help.yahoo.com/kb/generate-third-party-passwords-sln15241.html


<!-- --------------------------------------------------------------- -->
##

### Install phpmyadmin Manualy

https://www.digitalocean.com/community/questions/how-to-install-manually-phpmyadmin-on-ubuntu

Step 1 - Install the additional PHP modules:

    $ sudo apt update

    $ sudo apt install php-mbstring
    $ sudo apt-get install gettext

    $ sudo phpenmod mbstring

Step 2 - Download the source files

    https://www.phpmyadmin.net/downloads/

    Note: if you don’t have upzip already installed you can install it with:
    $sudo apt install unzip

    $ unzip phpMyAdmin-5.0.2-all-languages.zip


    Rename the folder

    $ mv phpMyAdmin-5.0.2-all-languages phpmyadmin


    Move the phpMyAdmin folder to your document root:

    $ sudo mv phpmyadmin /var/www/html/phpmyadmin


Step 3.1 - Configure phpMyadmin

    $ cd /var/www/html

    $ sudo chmod 777 phpmyadmin

    $ nano ./phpmyadmin/config.inc.php

    update this line, fill between '' with a secret key/string:

    $cfg['blowfish_secret'] = ''; /* YOU MUST FILL IN THIS FOR COOKIE AUTH! */ 


Step 3.2 - Create a mysql user with password and grant privilages

    You should do this in mysql, check above in mysql section.

Step 4 - Securing your phpMyAdmin Instance

    $ sudo nano /etc/apache2/sites-available/000-default.conf

    and add at the bottom:

    <Directory /var/www/html/phpmyadmin>
        Options FollowSymLinks
        DirectoryIndex index.php
        AllowOverride All
    </Directory>

    $ sudo nano /var/www/html/phpmyadmin/.htaccess

    AuthType Basic
    AuthName "Restricted Files"
    AuthUserFile /etc/apache2/.htpasswd
    Require valid-user

    $ sudo htpasswd -c /etc/apache2/.htpasswd username

<!-- --------------------------------------------------------------- -->
##


### Install Atom

    https://linuxize.com/post/how-to-install-atom-text-editor-on-ubuntu-20-04/

    $ sudo snap install atom --classic

<!-- --------------------------------------------------------------- -->
##

### Installing FileZilla from command line

    https://www.computernetworkingnotes.com/linux-tutorials/how-to-install-filezilla-ftp-client-in-ubuntu.html

    $ sudo apt update
    $ sudo apt install filezilla

<!-- --------------------------------------------------------------- -->
### How to view WebP images in Ubuntu and other Linux

    $ sudo apt-get install gthumb

Once installed, you can simply rightly click on the WebP image and select gThumb to open it

Make gThumb the default application for WebP images in Ubuntu to display thumbnail.
    

<!-- --------------------------------------------------------------- -->

### Install Docker

    $ sudo apt-get update
    $ sudo apt install docker.io

    $ docker --version

    $ sudo systemctl status docker
    $ sudo systemctl enable --now docker
    $ sudo systemctl disable --now docker

    <!-- $ sudo docker run hello-world -->

<!-- --------------------------------------------------------------- -->

### Reinstall Grub
    $ sudo grub-install /dev/sda



<!-- --------------------------------------------------------------- -->

### VSCode Extention List

    $ code --list-extensions

<!-- --------------------------------------------------------------- -->

### Digital Ocean connect ssh

    $ ssh -i /home/foxcodenine/digitalocean/digitalOcean.txt root@167.172.163.199

