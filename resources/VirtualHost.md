

##### Flask VirtualHost:

Sample:
inside `www.mydomain.com.conf` at \etc\apache2\sites-available\

	1	<VirtualHost *:80>
	2	        ServerName cm.ridiculous-inc.com				
	3	        WSGIScriptAlias / /var/www/cm/flaskapp.wsgi
	4	        <Directory /var/www/cm>
	5	            Order allow,deny
	6	            Allow from all 
	7	        </Directory>
	8	        Alias /static /var/www/cm/static
	9	        <Directory /var/www/cm/static/>
	10	            Order allow,deny
	11	            Allow from all
	12	        </Directory>
	13	        ErrorLog ${APACHE_LOG_DIR}/error.log
	14	        LogLevel warn
	15	        CustomLog ${APACHE_LOG_DIR}/access.log combined
	16	</VirtualHost>


	1 	*:80  listen to all ip address on port 80.
	2 	domain listening to.
	3	WSGIScriptAlias -- this part is new, and it apples to flask so far.
		This will set up the homepage, and rules to the path/Dir below.
		You can name the file.wsgi anything, but it is good practise to keep it in the app file.

	8 	here we are tekking apache, whatever you find as /static servit at /var/www/cm/static
> https://httpd.apache.org/docs/2.4/mod/mod_alias.html#alias

	so:				http://example.com/static/image/foo.gif
	will go to:		/var/www/cm/static/image/foo.gif

	13 ErrorLog  you can view them by:

##### To view apache log errors

	$ sudo tail -f /var/log/apache2/error.log 


##### wsgi file (Web Server Gateway Interface)

Sample:

	1		#!/usr/bin/python
	2		activate_this = '/home/ubuntu/.local/share/virtualenvs/cm-Mg75QJy5/bin/activate_this.py'
	3		execfile(activate_this, dict(__file__=activate_this))
	4		import sys
	5		import logging
	6		logging.basicConfig(stream=sys.stderr)
	7		sys.path.insert(0,"/var/www/cm/")
	8		
	9		from coin_manager import app as application
	10		application.secret_key = '34qtGQ#T$tWEet#$reasgEWRdsfGSge' 

wsgi uses python code.

If you are using a virtual environment line 2 & 3 are to activate it. (Not need it if not using venv).

(2)  `activate_this` is a variable, and it take the `activate_this.py` of our venv or pipenv.

It need to be change  according  virtualenv dir.

If you are using pipenv and need path to activate_this.py

	$ pipenv 
	gives you all commands
	
	to get path:
	$ pipenv --venv
 	`/home/ubuntu/.local/share/virtualenvs/cm-Mg75QJy5`

(7) In this line you need to update the path to you app dir.

(9) Here you need to update the entry point {coin_manager} to you app running file. 

Generally it is the:
	
	$ python app.py  or  $ python run.py   .....etc
	
	in the above is the app  or  run

(10) Is setting up you secret_key


##### check you .conf file

	$ cd /etc/apache2/sites-available
	$ sudo apachectl -t

##### For WSGIScriptAlias we need package `libapache2-mod-wsgi`

	to check if it is already installed

	$ sudo apt -a list libapache2-mod-wsgi

Install wsgi module and enable

	$ sudo apt-get install libapache2-mod-wsgi
	$ sudo a2enmod wsgi

do a recheck:

	$ sudo apachectl -t

To enable ower site

	$ sudo a2ensite www.mydomain.com.conf
	$ sudo service apache2 reload  or  $ sudo systemctl reload apache2

restart the server:
	
	$ sudo service apache2 restart











##

#### Using apachectl to Control Apache Web Server in Linux
> https://www.configserverfirewall.com/linux-tutorials/apachectl-command/

`$ apachectl` get you all commands

	start 			Start the Apache HTTP Server.

	stop 			Stop the Apache HTTP Server.

	restart 		Restart the Apache Web Server, 
					If the Server is not running apachectl will start the server.

	fullstatus 		Display Full status report.

	status 			Display brief status of the web server.

	graceful 		graceful restart, reload the apache configuration 
					without interrupting currently established connections.

	graceful-stop 	Stop the server without aborting currently open connections.

	configtest 		Check the Apache configuration files for the syntax errors.


To start Apache:

	$ sudo apachectl start

To restart the Web Server, run:
	
	$ sudo apachectl restart

The graceful command will restart the apache web server without interrupting current open connections and Open connections are allowed to complete before being shut down. This is A better way to restart the web server after a change to the configuration file.

	$ sudo apachectl graceful



Even though you can start and restart apache server with apachectl command, I would highly recommend to use systemctl command instead.

On debian, Ubuntu Linux:

	$ systemctl start|restart|stop apache2.service

#### Apachectl Configtest: Test configuration files for errors

The configtest command will cause Apache to read the config files and report any configuration errors.

	$ sudo apachectl configtest  or  sudo apachectl -t 
	
	you sould be in the *.conf file dir (/etc/apache2/sites-available)

