#### Set Display 
Display > change to x200

­<!-- --------------------------------------------------------------- -->

#### Set livepatch
Software & Updates > Ubuntu Pro > Enable Ubuntu Pro > ubuntu.com/pro

Or got to ubuntu.com and sign-in >    Ubuntu.com log in with Ubuntu One 

email: foxcode9@gmail.com
password *******99

Get Ubuntu Pro > Your subscriptions



sudo pro attach C12sA8LAmii1UsNSkKjQAURq8*****

<!-- --------------------------------------------------------------- -->
#### install vscode

go to: https://code.visualstudio.com/docs/setup/linux

    $  sudo apt-get install wget gpg
    $  wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
    $  sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
    $  echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" |sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
    $  rm -f packages.microsoft.gpg
    $  sudo apt install apt-transport-https
    $  sudo apt update
    $  sudo apt install code

<!-- --------------------------------------------------------------- -->
#### Solaar - Manage Logitech’s Devices on Linux

    $ sudo apt install solaar
<!-- --------------------------------------------------------------- -->

#### Brave Browser

    $  sudo apt install curl
    $  sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
    $  echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list
    $  sudo apt update
    $  sudo apt install brave-browser
    $  history 

<!-- --------------------------------------------------------------- -->

#### Chrome Extentions

zoho vault

<!-- --------------------------------------------------------------- -->

#### Install vim

    $ sudo apt install vim

<!-- --------------------------------------------------------------- -->

#### Check & Remounting Swap

Get swap FSTYPE FSVER LABEL UUID

    $ lsblk --fs

    /dev/disk/by-uuid/b295588b-caba-4faa-98db-c02d0c7241c8 none swap sw 0 0
    

Check and update /etc/fstab

    sudo vi /etc/fstab

Compare the UUID 'b295588b-caba-4faa-98db-c02d0c7241c8' with that in lsblk --fs. And update if need it.

After Saving Check Syntax

    $ sudo mount -a

Or test specific mount by:

    $ sudo mount /path/to/mountpoint

<!-- --------------------------------------------------------------- -->

#### Format disk /dev/sda as ext4 and mount it at 

1. Ensure the disk is unmounted:

    $ sudo umount /dev/sda

2. Create an ext4 filesystem on the disk:

    $ sudo mkfs.ext4 /dev/sda

3. Create the mount point directory:

    $ mkdir -p /home/foxcodenine/foxfiles

4. Mount the disk:

    $ sudo mount /dev/sda /home/foxcodenine/foxfiles

5. Make the mount persistent across reboots by adding it to /etc/fstab:
First, get the UUID of the disk:

    $ sudo blkid /dev/sda

This command will output something like:

    /dev/sda: UUID="XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX" TYPE="ext4"

Note the UUID value.
Edit the /etc/fstab file:

    $ sudo vi /etc/fstab

Add the following line at the end of the file:

    UUID=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX /home/foxcodenine/foxfiles ext4 defaults 0 2

6. Verify the setup:

    $ sudo mount -a
    $ df -h

<!-- --------------------------------------------------------------- -->
#### TODO

update .bashrc

copy ~/.ssh/ssh_iot and ~/.ssh/ovh

install 
    pCloud
    dbeaver
    Obsidian
    vlc
    Atom
    Filezila

install go:
    just download the_go_file.tar.gz from web, 
    extract, 
    and move go dir to /usr/local

vscode 
    install extentions
    copy settings



<!-- --------------------------------------------------------------- -->
#### yubico

https://support.yubico.com/hc/en-us/articles/360016649039-Installing-Yubico-Software-on-Linux

https://snapcraft.io/yubioath-desktop

    $ sudo snap install yubioath-desktop

<!-- --------------------------------------------------------------- -->
#### Flatpack

    $ sudo apt install flatpak
    
<!-- --------------------------------------------------------------- -->

#### mysql

Install MySQL server:

    $ sudo apt update
    $ sudo apt install mysql-server

Secure the MySQL installation (did not do):

    $ sudo mysql_secure_installation

Start and enable MySQL service:

    $ sudo systemctl start mysql
    $ sudo systemctl enable mysql

Verify MySQL installation:

    $ sudo systemctl status mysql
    $ sudo mysql -u root -p
    $ ****99

Create a user:

    CREATE USER 's****'@'localhost' IDENTIFIED BY 'u****';

    GRANT ALL PRIVILEGES ON *.* TO 's****'@'localhost';

    FLUSH PRIVILEGES;



<!-- --------------------------------------------------------------- -->

#### Setting up calculator btn:
    $ dpkg -l | grep -i calculator

    > mate-calc

    I have install gnome-calculator and it was fixed

    $ apt search gnome-calculator

    $ sudo apt insrall gnome-calculator


#### Setting up screenshot btn:

Budgie Control Center > Keyboard > Keyboard Shortcuts

Search for : screenshot

I have updated the:
    Save screenshot of a window to Pictures     Shift+Alt+Super+S
    Save screenshot of an area to Pictures      Shift+Ctrl+Super+S
    Save screenshot of Pictures                 Shift+Super+S

<!-- --------------------------------------------------------------- -->

#### Set up Git

    $ sudo apt update
    $ sudo apt install git

    $ git config --global user.name "Your Name"
    $ git config --global user.email "your.email@example.com"

    $ git config --global --list

    $ git config --global core.editor vi

    $ git config --global color.ui auto

I have also coped ~/.ssh/id_ed25519 and ~/.ssh/id_ed25519.pub from 22.04

<!-- --------------------------------------------------------------- -->

#### nvm, node js and npm

Install NVM:

    
    $ curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

Reload shell configuration:
    
    $ source ~/.bashrc

Verify NVM installation:
    
    $ nvm --version

Install Node.js version 20:
    
    $ nvm install 20

Verify Node.js and NPM versions:
    
    $ node -v    
    $ npm -v

<!-- --------------------------------------------------------------- -->

#### Install php, php-fmt and apache

Update package index

    $ sudo apt update

Install Apache:

    $ sudo apt install apache2
    $ sudo systemctl start apache2
    $ sudo systemctl enable apache2

Install PHP and PHP-FPM

    $ sudo apt install php php-fpm
    $ sudo apt install libapache2-mod-fcgid


Enable Apache modules

    $ sudo a2enmod proxy_fcgi setenvif
    $ sudo a2enconf php8.3-fpm
    $ sudo a2enmod fcgid

Restart Apache

    $ sudo systemctl restart apache2

Create a PHP info file

    $ sudo vi /var/www/html/info.php

Add the following content to info.php:

    <?php
    phpinfo();


Open your web browser and navigate to:

    http://localhost/info.php

<!-- --------------------------------------------------------------- -->

#### Install Docker

1. Update package index:

        $ sudo apt update

2. (Did not do) Install packages to allow apt to use a repository over HTTPS:

        $ sudo apt install apt-transport-https ca-certificates curl software-properties-common

3. Add Docker’s official GPG key

        $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

4. Set Up the Docker Repository:

        $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

5. Update Package Index Again:

        $ sudo apt update

6. Install Docker Engine:

        $ sudo apt install docker-ce docker-ce-cli containerd.io

7. Start and Enable Docker:

        $ sudo systemctl start docker
        $ sudo systemctl enable docker

8. Verify Docker Installation:
    
        $ sudo docker run hello-world

#### Install Docker Compose

1. Download the Current Stable Release of Docker Compose:
    
        $ sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

2. Apply Executable Permissions to the Binary:

        $ sudo chmod +x /usr/local/bin/docker-compose

3. Verify Docker Compose Installation:

        $ docker-compose --version
  
 