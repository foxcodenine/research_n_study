### install xdebug
    $ sudo apt install php-xdebug

### set-up xdebug
    $ cd /etc/php/8.0/mods-available/

    $ ls

    $ sudo nano xdebug.ini

        after:
            zend_extension=xdebug.so

        past:
            xdebug.mode=debug
            xdebug.client_host=localhost
            xdebug.remote_port=9003
            xdebug.idekey="netbeans-xdebug"

    $ sudo systemctl restart php8.0-fpm.service

    $ sudo service apache2 restart 