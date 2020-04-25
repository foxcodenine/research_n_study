##npm
### to initialization , --yes to accept all defaults:
	$ npm init --yes

## To install babel command-line and babel prest env:
	i is for install 
##### --save-dev to save these as a development dependency
	$ npm i --save-dev babel-cli babel-preset-env
	<!--  or to install them (command-line & babel prest env) separately -->
	$ npm i --save-dev babel-cli
	$ npm i --save-dev babel-preset-env

### npm-run-script 
### update the package.json script

	{
	  "name": "chapter2",
	  "version": "1.0.0",
	  "description": "= Learning JavaScript, 3rd Edition  == Chapter 2: JavaScript Development Tools",
	  "main": "index.js",
	  "scripts": {
	    "test": "echo \"Error: no test specified\" && exit 1",
	    "babelnode": "babel es6 -d dist",  <--
	    "babelbrowser": "babel public\\es6 -d public\\dist", <--
	  },
	  "keywords": [],
	  "author": "",
	  "license": "ISC",
	  "devDependencies": {
	    "babel-cli": "^6.26.0",
	    "babel-preset-env": "^1.7.0"
	  }
	}

### execute script from CLI
	$ npm run buildnode
	or/and
	$ npm run babelbrowser


#### list global packages
	$ npm list -g --depth 0

##
##

### unstage all from git
	$ git reset

### ls hidden files powershell
	$ ls -Force




## eslint

### install eslint in dev
	$ npm install --save-dev eslint

### or install eslint in g
	$ npm i -g eslint u

### to initializatio eslit
	$ npx eslint --init

### to check specific file
	$ npx eslint yourfile.js

### to check all files is directory and sub-directories
	$ npx eslint  **/*.js 

### to fix check and fix file or files
	$ npx eslint --fix yourfile.js     or     $ npx eslint --fix **/*.js 



### cloning a git repository OVER SSH:
	$ git clone ssh://git@bitbucket.org:teamsinspace/documentation-tests.git

## GIT to removing multiple commits (remove the last two commits)
	$ reset --hard HEAD~2 


## running a new ubuntu server

	$ sudo apt update

	$ sudo apt upgrade

	$ sudo apt install apache2

### display apache commands
	$ sudo service apache2 

### display apache status
	$ sudo service apachi2 status

### apache directory 
	$ cd /etc/apache2/
	$ ls -l

### sites-available dirc
	$ cd /etc/apache2/sites-available/
	
	$ ls
	http  file : 000-default.conf
	https file : default-ssl.conf
	
	$ nano 000-default.conf

### DocumentRoot
	/var/www/html

### check which binary git is:
	$ which git

### check git version on server:
	$ git --version

### to install git on server:
	$ sudo install git

### git clone into a folder (example to html)
	$ git clone https://github.com/robertbunch/jquery-todo.git html

### to just clone a repo
	$ sudo git clone https://github.com/robertbunch/todo-react-express.git

### switch to super user
	$ sudo su

### end su
	$ exit

### change file or folder ownershipp
$ sudo chown -R newUser folderName/

<br><br>


## add https to website:

	https://letsencrypt.org/
	https://certbot.eff.org/
	
	on certbot select the Software and System: 
	
	My HTTP website is running 'Software' on 'System'
	
	1. SSH into the server 
	From the terminal connect to the server 
	
	2.Add Certbot PPA 
	Enter the commands given, currenty:
	   $ sudo apt-get update
	   $ sudo apt-get install software-properties-common
	   $ sudo add-apt-repository universe
	   $ sudo add-apt-repository ppa:certbot/certbot
	   $ sudo apt-get update
	
	3.Install Certbot
	Run this command on the command line on the machine to install Certbot.
	
	   $ sudo apt-get install certbot python-certbot-apache

### Before going to next step, currently 4. you need to do the following.

	  $ cd /etc/apache2/sites-available
	  $ ls -l 
	
- Create a file with nano with the site name ending .conf 
- And insert the following:
- You need to update the DocumentRoot, ServerName & <Directory "****"> as required:

		$ sudo nano foxhost9.com.conf
	
		<VirtualHost *:80>
		    DocumentRoot /var/www/foxhost9
		    ServerName foxhost9.com 
		    <Directory "/var/www/foxhost9">
		        allow from all 
		        AllowOverride All 
		        Order allow,deny 
		        Options +Indexes
		    </Directory>
		</VirtualHost>
#### Change root / document dir name accordingly:
	  $ cd /var/www
	  $ sudo mv html foxhost9
	
	  $ cd /etc/apache2/sites-available
	  $ ls

#### Enter the following command, modify as required:

	https://www.digitalocean.com/community/tutorials/how-to-use-apache-as-a-reverse-proxy-with-mod_proxy-on-ubuntu-16-04

	This will enable the revers proxy,and adds support for proxying HTTP connections
	$ sudo a2enmod proxy_http
	To enable ower site
	$ sudo a2ensite foxhost9.com.conf
	$ sudo service apache2 reload  or  $ sudo systemctl reload apache2

##
	4.Choose how you'd like to run Certbot
	$ sudo certbot --apache

##### OR better or if doesn't work:

$ sudo certbot --authenticator standalone --installer apache -d foxhost9.com --pre-hook "systemctl stop apache2" --post-hook "systemctl start apache2"

  	

##### And select accordingly:

	5. On AWS or your webhost go to inbound rules and open  post 443 (for https traffic).

	$ cd /etc/apache2/sites-available
	$ ls
  
	See that a new file is create in this case foxhost9.com-le-ssl.conf

<br><br>
## To redirect www to non-www Address: 
#### example: www.foxhost9.com  to  foxhost9.com
  
	  1. add another A type record with the www example: www.foxhost9.com 
	  pointing to your IPv4 Public IP.
	
	  2. edit with nano your .conf file example: foxhost9.com.conf and add 
	  the following VirtualHost before your VirtualHost:  


	<VirtualHost *:80>
	    ServerName www.foxhost9.com
	    Redirect permanent / http://foxhost9.com/
	</VirtualHost>
	
	<VirtualHost *:80>
	  Docume........
	  ................
	  ....
	</VirtualHost>
	
	$ sudo service apache2 restart


> https://stackoverflow.com/questions/1100343/apache-redirect-from-non-www-to-www

	Using the rewrite engine is a pretty heavyweight way to solve this problem. 
	Here is a simpler solution:
	
	<VirtualHost *:80>
	    ServerName example.com
	    Redirect permanent / http://www.example.com/
	</VirtualHost>
	
	<VirtualHost *:80>
	    ServerName www.example.com
	    # real server configuration
	</VirtualHost>

	And then you'll have another <VirtualHost> section with ServerName www.example.com for 
	your real server configuration. Apache automatically preserves anything after the / when 
	using the Redirect directive, which is a common misconception about why this method won't 
	work (when in fact it does).
##
##

## Install mysql on ubuntu server
	$ sudo apt install mysql-server
### To set password if not asked
	$ mysql_secure_installation

<br>

## Install nodejs on ubuntu server
	https://tecadmin.net/install-latest-nodejs-npm-on-ubuntu/

	$ sudo apt-get install curl
	$ curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
	
	$ sudo apt-get install nodejs

	$ node -v
	$ npm -v

#### Install your nodejs dependences on Ubuntu server
	go to your project dir example: /var/www/something 
	it should have your package.json file and run:

	$ sudo npm install

### To install nodemon globally
	info > https://www.npmjs.com/package/nodemon

	$ sudo npm install nodemon -g

### Run nodemon 
	$ nodemon

<br>

## Mysql create new user to connect through ssh
	https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql

	$ sudo mysql -u root -p
	$ ******* 

To view a List of MySQL Users:

	mysql> SELECT User,Host FROM mysql.user;

To create a new user example: admin on localhost with password ****: 

	mysql> CREATE USER 'admin'@'localhost' IDENTIFIED BY '****';

To delete a user:

	mysql> DROP USER 'admin'@'localhost';

To update host:

	mysql> UPDATE mysql.user SET host="localhost" WHERE user="admin";

To Grant permissions to a user.

	mysql> GRANT ALL PRIVILEGES ON * . * TO 'admin'@'localhost';

Once you have finalized the permissions that you want to set up for your new users, always be sure to reload all the privileges.

	mysql> FLUSH PRIVILEGES;

to stop, start or restart mysql:

	$ sudo service mysql stop;
	$ sudo service mysql start;
	$ sudo service mysql restart;

### Setting up workbench:

	in work bech select  +  in MySQL Connection

	Connection Name: ubuntu_server				 < set a name 
	
	Connection Method: Standard TCP/IP over SSH
	
	SSH Hostname: 18.156.3.139                   <  you server IPv4
	
	SSG Username: ubuntu						 <  your username on server
	
	SSH Key File: P:/AWS/deploy_web_apps.pem	
	
	MySQL Hostname: localhost					 <  as set above, when create user
	
	MySQL Server Port: 3306						 <  need to open this post as 
													did for ssh http & https
	
	Username: admin								 <  as did above, when create user
	
	Password Store in Vauly.. :     < you can enter pass or enter it on connect
									  this is as set above, when create user

<br>
## To check if port is in use in
	https://www.cyberciti.biz/faq/unix-linux-check-if-port-is-in-use-command/

	$ sudo lsof -i -P -n | grep LISTEN
	or
	$ sudo netstat -tulpn | grep LISTEN

	sshd    85379     root    3u  IPv4 0xffff80000039e000      0t0  TCP 10.86.128.138:22 (LISTEN)

	sshd 			is the name of the application.
    10.86.128.138 	is the IP address to which sshd application bind to (LISTEN)
    22 				is the TCP port that is being used (LISTEN)
    85379 			is the process ID of the sshd process

### Find (and kill) process running on a certain port

	use lsof to find the process or port (if you have port enter port and vs):

	$ sudo lsof -i -P -n | grep LISTEN | grep 4444

	to stop process on port:
	$ kill `lsof -t -i:4444`


<br>
## Install PM2 on ubuntu (globally)
	$ sudo npm install pm2 -g

	start app www with pm2 and give it a bame ToDo
	$ sudo pm2 start bin/www --name "ToDo Api"

	pm2 list running apps 
	$ sudo pm2 list

## Python on Ubuntu

#### to install python 
	$ python
	*python-minimal
	*python3
	Try: sudo apt install <seleced package>

	& sudo apt install python3

to install pip:
	
	$ sudo apt install python-pip 
	or
	$ sudo apt install python3-pip

install pipenv

	$ pip install pipenv 
	or
	$ pip3 install pipenv


## Chmod 

	https://www.linuxquestions.org/questions/linux-software-2/chmod-codes-list-142654/
	https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/

to check permission of files in folder:

	$ ls -l

	drwx-xr-xr-x root ubuntu  4096 Aug 23  08:02  archive

	d is for dir
	rwx are user permision
	-xr are group permision
	r-x are others permision
	root is owner /user
	ubuntu us group

Chmod Codes list:
	


	u = user
	g = group
	o = other (not user or group)
	a = all

	+ = add permissions
	- = remove permissions

	r = read
	w = write
	x = execute
	t = sticky bit
	
	--- means no permissions have been granted at all
	rwx means full permissions have been granted

	so to add read permissiones for people in the files group:
	$ sudo chmod g+r filename.py

	--- “=” operator means we wipe out any existing permissions and set the ones specified.
	$ chmod u=rw,og=r new_file.txt

	___________________________________________________________

	0 == --- == no access
	1 == --x == execute
	2 == -w- == write
	3 == -wx == write / execute
	4 == r-- == read
	5 == r-x == read / execute
	6 == rw- == read / write
	7 == rwx == read / write / execute

	OWNER  GROUP   OTHER
	r w x  r w x   r w x 
	1 1 1  1 0 1   1 0 1 
	  7      5       5  
	  |______|_______|
	         |   
	        755

	so to set `read / write / execute` for owner and `read / execute` for group and all:
	
	$ sudo chmod 755 filname.py

	
	