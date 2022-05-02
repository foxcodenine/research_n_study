### To remove mysql if it is not working correctly

    $ sudo apt purge mysql-apt-config mysql-client-core-8.0 mysql-server-core-8.0 

### To re-install mysql

    $ sudo apt-get update; 
    $ sudo apt-get install mysql-server

### To remove snap if it is generatin 408 error - (bad solution)
    $ sudo apt purge snapd

### To re-install snap

    $ sudo apt install snapd
    
### If you are getting 408 error, download the snaps package 1st - (good solution)

    $ sudo snap download mysql-workbench-community

    $ sudo  snap ack mysql-workbench-community_9.assert

    $ sudo snap install mysql-workbench-community_9.snap

### To install MySQLWorkbench with snap

    $ sudo snap install mysql-workbench-community

### If you have installed MySQLWorkbench as a Snap package. 
### You want to store the database password(s) in the Gnome Passwords & Keys facility.
### You need to enter a command to allow this package to access the service. The command is:

    $ sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service