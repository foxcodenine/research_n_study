# Creating an Apache container:

    $ docker run -dit --name my-apache-app -p 8080:80 -v "$PWD":/usr/local/apache2/htdocs/ httpd:2.4

we are:

    run the container 'detach', 'interactive' and 'tty'
    naming it my-apache-app
    exposing port 80 to port 8080
    and bind mount the current directory to /usr/local/apache2/htdocs/
