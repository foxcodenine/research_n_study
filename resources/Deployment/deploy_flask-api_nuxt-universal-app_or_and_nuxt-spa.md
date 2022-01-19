### APPENDEX
How to set environment variables for your web apps (for SECRET_KEY etc)
https://help.pythonanywhere.com/pages/environment-variables-for-web-apps/

Host Multiple Domains on One Server or IP with Apache or Nginx
https://geekflare.com/multiple-domains-on-one-server-with-apache-nginx/

node-mp2
https://pm2.keymetrics.io/docs/usage/quick-start/
https://futurestud.io/tutorials/pm2-use-npm-to-start-your-app
https://coderrocketfuel.com/article/how-to-run-a-npm-start-script-with-pm2
https://www.npmjs.com/package/pm2

https://www.digitalocean.com/community/tutorials/how-to-use-apache-as-a-reverse-proxy-with-mod_proxy-on-ubuntu-16-04
_______________________________

    .env file

    FLASK_ENV = 'production'
    SECRET_KEY = 'e24af90e9e1348248e2608b826bf2f9B'

    NUXT_PROJECT_DB = 'mysql+pymysql://CovSdqWkvi:2iYSrMxaM4@remotemysql.com:3306/CovSdqWkvi'
    NUXT_PROJECT_DB_PRO = 'mysql+pymysql://admin:Admin@localhost/nuxt_api'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
_______________________________

    config.py file

    import os

    class Config():
        SECRET_KEY = os.getenv('SECRET_KEY')
        DEBUG = False
        TESTING = False

    class ConfigDev(Config):
        DEBUG = True
        CHECK_ENV = 'develeopment_env'
        SQLALCHEMY_DATABASE_URI = os.getenv('NUXT_PROJECT_DB')
        SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

    class ConfigPro(Config):
        CHECK_ENV = 'production_env'
        SQLALCHEMY_DATABASE_URI = os.getenv('NUXT_PROJECT_DB_PRO')
        SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

_______________________________

    run.py file

    from my_app import app
    from flask_cors import CORS, cross_origin
    import os

    CORS(app)

    if __name__ == "__main__":    
        app.run(host='0.0.0.0', port=4448)

_______________________________

    flaskapp.wsgi file

    #!/usr/bin/python3.8
    activate_this = '/home/ubuntu/.local/share/virtualenvs/nuxt_api_flask-gPgGeqg6/bin/activate_this.py'

    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))
    import sys
    import logging

    import os
    from dotenv import load_dotenv
    project_folder = os.path.expanduser('/var/www/nuxt_api_flask')
    load_dotenv(os.path.join(project_folder, '.env'))


    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0,"/var/www/nuxt_api_flask/")

    from run import app as application
_______________________________

### BACKEND

##### 1 Created New EC2 instance

	a. I used current key file – you can create a new one
	b. Updated the Inbound rules and opened port 80 (http) and port 443 (https) to 0.0.0.0/0
	c . Check that ssh (port 22) is open.

##### 2 Hosted zone (Route 53) created new record

	a. inserted public ip Address of instance

##### 3 Connect to instance (ssh)

	a. EC2 I select instance and press connect.
	b. And followed the instructions:
		i. Open ssh client (terminal)
		ii. cd to private key file.
		iii. Run 	$ sudo chmod 400 deploy_web_apps.pem
		iV. Run example provided 	
		$ sudo ssh -i "deploy_web_apps.pem" ubuntu@ec2-52-59-227-217.eu-central-1.compute.amazonaws.com

##### 4 Update instance:
    
    $ sudo apt update
	$ sudo apt upgrade

##### 5 Install apache2

		$ sudo apt install apache2
	a. Display apache commands:
		$ sudo service apache2
	b. Display apache status:
		$ sudo service apache2 status

##### 6 Install mySQL

	a. $ sudo apt install mysql-server
	b. Open my sql:
		$ sudo mysql -u root
		$ exit;
	c. To set password if not asked
		$ sudo mysql_secure_installation
		(password used in project Root)
		$ sudo mysql -u root -p
		$ ****
		$ exit;

##### 5. Mysql create new user to connect through ssh

        $ sudo mysql -u root -p
        $ *******

        a. To view a List of MySQL Users:
            mysql> SELECT User,Host FROM mysql.user;

        b. To create a new user example: admin on localhost with 	password ****:
            mysql> CREATE USER admin@localhost IDENTIFIED BY '****' ;
            (password used in project Admin)

        c. To delete a user:
            mysql> DROP USER admin@localhost;

        d. To update host:
            mysql> UPDATE mysql.user SET host="localhost" WHERE user="admin";

        e. To Grant permissions to a user.
            mysql> GRANT ALL PRIVILEGES ON * . * TO admin@localhost;

##### 6. Install python

        a. $ sudo apt install python3
        b. $ sudo apt install python3-pip

##### 7. Install mod-wsgi and enable it:

        a. $ sudo apt-get install libapache2-mod-wsgi-py3
        b. $ sudo a2enmod wsgi


##### 8. Python project – update the following files

        a. .env, run.py, config.py, flaskapp.wsgi
        b. delete Pipfile.lock

##### 9. Change ownership of folder var/www  from root to ubuntu

        a. $ sudo chown -R ubuntu /var/www

##### 10. Copy project to var/www/project_folder using filezila

        a. Open filezila and open the Site Manager (icon is at top left corner)
        b. Protocol: SFTP – SHH File Transfer Protocol
        c. Host: 3.121.29.168 ← (change to your instance public IPv4address)
        d. Logon Type: Key file
        e. User: ubuntu
        f. /media/foxcodenine/INTENSO/ ← (change to  key file location .ppk file is made 	from the .pem file)
        g. Select connect.
        h. move file from pc to instance.

        Or use scp

        sudo scp -i ./deploy_web_apps.pem -r /home/foxcodenine/Desktop/nuxt/nuxt_api_flask ubuntu@ec2-52-59-227-217.eu-central-1.compute.amazonaws.com:/var/www/


##### 11. Install pipenv

        a. sudo pip3 install pipenv
        b. $ cd myproject
        c. $ pipenv --python 3.9
        d. $ sudo pipenv install 'package_name'

        # if Pipenv fails to install psycopg2
        # sudo apt-get install libpq-dev
        # and retry

        d. $ pipenv --venv
        /home/ubuntu/.local/share/virtualenvs/nuxt_api_flask-gPgGeqg6  

        e. Copy path and update flaskapp.wsgi  file.

##### 12. Set activate_this.py to read and execute.

        a. cd to activate_this.py ex:
        /home/ubuntu/.local/share/virtualenvs/nuxt_api_flask-gPgGeqg6 /bin/ activate_this.py

        b. sudo chmod 755  activate_this.py
        c. check also that its path from / is set at list to read.

##### 13. Enable Virtualhost

        a. copy your virtualhost file to /etc/apache2/site-avalible
        b. $ sudo a2ensite www.mydomain.com.conf ← (update to your virtualhost file)
        c. $ sudo systemctl reload apache2
        d. $ sudo service apache2 restart

##### 14. To view apache log errors.
	$ sudo tail -f /var/log/apache2/error.log


_______________________________


### FRONTEND  NUXT APPLICATION


##### 1. Install node-js and npm.

    $ sudo apt-get install nodejs npm

##### 2. Build project and Remove node_modules folder.

    On pc run: 
        $ npm run  build 

    And when complete remove node_modules.
    (You can build project also after on the inctance)

##### 3. Copy/upload frontend project/folder using scp or filzila

    

    To copy files between your computer and your instance you can use an FTP 
    service like FileZilla or the command scp which stands for secure copy.

    To use scp with a key pair use the following command: 
    $ scp -i path/to/key file/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/file.

    To use it without a key pair, just omit the flag -i and type in the 
    password of the user when prompted.

    To copy an entire directory, add the -r recursive option: 
    $ scp -i path/to/key -r directory/to/copy user@ec2-xx-xx-xxx-xxx.compute-1.amazonaws.com:path/to/directory.



    linux:
    $ sudo scp -i ./deploy_web_apps.pem -r /home/foxcodenine/Desktop/chapter8-deploy_app/nuxt_app_front_end ubuntu@ec2-52-59-227-217.eu-central-1.compute.amazonaws.com:/var/www/

    windows:
    $ scp -i ./deploy_web_apps.pem –r ../Projects/tutorials/Udemy/nuxt_/chapter8-deploy_app/nuxt_app_front_end/ ubuntu@ec2-52-59-227-217.eu-central-1.compute.amazonaws.com:/var/www/


##### 4. Install npm packages on the inctanse.


    $ cd /var/www/project_folder
    $ sudo npm install

##### 5. Install Process_Manager_2 globally

    $ sudo npm install pm2 -g

#####6. Start nuxt app

    NPM Start Script:
    $ pm2 start npm -- start

    or 

    NPM Start Script With the App Name Option:
    $ pm2 start --name=NUXT_BLOG npm -- start


    To Managing Processes:

    pm2 list
    pm2 reload NUXT_BLOG
    pm2 stop NUXT_BLOG
    pm2 restart NUXT_BLOG
    pm2 delete NUXT_BLOG

    Instead of app_name you can pass:

    'all' to act on all processes
    'id'  to act on a specific process id

    $ pm2 [list|ls|status]

    Additional info:
    https://pm2.keymetrics.io/docs/usage/quick-start/
    https://futurestud.io/tutorials/pm2-use-npm-to-start-your-app
    https://coderrocketfuel.com/article/how-to-run-a-npm-start-script-with-pm2
    https://www.npmjs.com/package/pm2

##### 7. Copy frontend virtualhost 

    Copy virtualhost to /etc/apacete2/sites-avalible

    www.foxhost9.com.conf file
#####
    <VirtualHost *:80>
        ServerName www.foxhost9.com
        <Location "/">
            ProxyPreserveHost On
            ProxyPass http://localhost:8181/
            ProxyPassReverse http://localhost:8181/
        </Location>
    </VirtualHost>

##### 8. Enable virtualhost

    To enable these four modules, execute the following commands in succession:

    $ sudo a2enmod proxy
    $ sudo a2enmod proxy_http
    $ sudo a2enmod proxy_balancer
    $ sudo a2enmod lbmethod_byrequests

    We only need proxy and proxy_http

    To enable virtualhost:
    $ sudo a2ensite www.foxhost9.com.conf

    Reload apache:    
    $ sudo systemctl reload apache2


_______________________________

### Apache2
https://hostadvice.com/how-to/how-to-enable-apache-mod_rewrite-on-an-ubuntu-18-04-vps-or-dedicated-server/




The following is Trava VirtualHost which have a 'nust SPA' and a 'flask api':

<VirtualHost *:80>
ServerName foxcode.io

        Alias /001/nuxt /var/www/projects/001_trava/dist/nuxt   # <- (A)
        Alias /001 /var/www/projects/001_trava/dist             # <- (B)
        RequestHeader append "API-KEY" "123#456#789"            # <- (C)
        <Directory "/var/www/projects/001_trava/dist" >
            allow from all
            AllowOverride All
            Order allow,deny
            Options +Indexes
        </Directory>


        WSGIScriptAlias /api/001 /var/www/projects/001_trava/backend_flask_deploy/flaskapp.wsgi     # <- (D)
        <Directory /var/www/projects/001_trava/backend_flask_deploy>
            Order allow,deny
            Allow from all
        </Directory>


        ErrorLog ${APACHE_LOG_DIR}/error.log
        LogLevel warn
        CustomLog ${APACHE_LOG_DIR}/access.log combined

        RewriteEngine on                                        # <- (E)
</VirtualHost>


_______________________________

(A) Redirect Static file/folder

If you have a static folder in your app that is holding files as images ccs and js files.
Apache may not find them automaticaly and give an error in you console:

    GET http://foxcode.io/_nuxt/eb7ccd7.js 
    net::ERR_ABORTED 404 (Not Found)


In the above example at "A" we redirected:
    /001/nuxt 
 to:   
    /var/www/projects/001_trava/dist/nuxt
with an "Alias"


NB: also in nuxt.config.js we set it to rename the static folder 
    form _nuxt to nuxt since apache my drop the underscores by:

        build: {
            publicPath: '/nuxt/',
            // ...
        },


_______________________________

(B) Multiple Apps on same domain

if your domain is 'foxcode.io' 
& your are hosting the app on 'foxcode.io/001'

you need to redirect /001 with an Alias as shown above at "B"


NB: also in nuxt you need set the route.base property in nuxt.config.js:

        router: {
            base: '/001/',
        },

_______________________________

(C) Enable mod_headers

You can add "Header" or "RequestHeader" in you VirtualHost 
And pass commands as "set", "add", "append", "remove" etc
To enable it: 

    $ sudo a2enmod headers
    $ sudo systemctl restart apache2

_______________________________

(D) Enable mod_wsgi

If you set "WSGIScriptAlias"
To enable it:

    $ sudo apt-get install libapache2-mod-wsgi-py3
    $ sudo a2enmod wsgi
    $ sudo systemctl restart apache2

_______________________________

(E) Enable mod_rewrite

If you set "RewriteEngine on"
To enable it:

    $ sudo a2enmod rewrite
    $ sudo systemctl restart apache2
_______________________________

### THE END
_______________________________












	


