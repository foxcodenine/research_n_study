If when installing a snap package you get:

    ... cannot query the store for updates: got unexpected HTTP
    status code 408 via POST to "https://api.snapcraft.io/v2/snaps/refresh"

Example, when: 

    $ sudo snap installfirefox

Solution (download package with snap first and the install it):

    $ sudo snap download firefox

    $ sudo  snap ack firefox_1232.assert

    $ sudo snap install firefox_1232.snap