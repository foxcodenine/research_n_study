How To Use the .htaccess File
https://www.digitalocean.com/community/tutorials/how-to-use-the-htaccess-file

Apache redirect www to non-www and HTTP to HTTPS
https://simonecarletti.com/blog/2016/08/redirect-domain-http-https-www-apache/

Start / Stop and Restart Apache 2 Web Server Command
https://www.cyberciti.biz/faq/star-stop-restart-apache2-webserver/
  <!---
  ______________________________________________________________________________

  /etc/apache/sites-available/foxhost9.com.conf

      <VirtualHost *:80>    
            ServerName foxhost9.com

            WSGIScriptAlias /mfp /var/www/mfp/flaskapp.wsgi
            <Directory /var/www/mfp>
                Order allow,deny
                Allow from all
            </Directory>
            Alias /static /var/www/mfp/app/static
            <Directory /var/www/mfp/apa/static/>
                Order allow,deny
                Allow from all
            </Directory>


            WSGIScriptAlias /trendy /var/www/trendy/flaskapp.wsgi
            <Directory /var/www/trendy>
                Order allow,deny
                Allow from all
            </Directory>
            Alias /static /var/www/trendy/static
            <Directory /var/www/trendy/static/>
                Order allow,deny
                Allow from all
            </Directory>


            WSGIScriptAlias /test_page /var/www/test_page/flaskapp.wsgi
            <Directory /var/www/test_page>
                AllowOverride All
                Order allow,deny
                Allow from all
            </Directory>
            Alias /static /var/www/test_page/static
            <Directory /var/www/test_page/static/>
                AllowOverride All
                Order allow,deny
                Allow from all
            </Directory>

    </VirtualHost>

  ______________________________________________________________________________

  /var/www/test_page/.htaccess

  RewriteEngine On
  RewriteCond %{HTTPS} off [OR]
  RewriteCond %{HTTP_HOST} ^www\. [NC]
  RewriteRule ^ https://foxhost9.com%{REQUEST_URI} [L,NE,R=301]

  ______________________________________________________________________________
 --->
