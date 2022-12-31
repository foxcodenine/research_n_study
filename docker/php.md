# note 'myphp' is the container name

# Run a new php container, version 8.1, name it and in inteactive mode.
$ docker run --name myphp  -it php:8.1

# First start the php container and then List all installed php extentions (like $ php -m).
$ docker start myphp
$ docker exec myphp php -m

# Install an extention (exif) using 'docker-php-ext-install' command.
$ docker exec myphp docker-php-ext-install exif

# Start php attached and interactive (like $ php -a).

$ docker start -ai myphp
