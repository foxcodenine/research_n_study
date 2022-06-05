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

```bash
    #$ sudo snap connect mysql-workbench-community:password-manager-service :password-manager-service
    
    $ sudo snap connect mysql-workbench-community:password-manager-service
    $ sudo snap connect mysql-workbench-community:ssh-keys
    $ sudo snap connect mysql-workbench-community:cups-control
    $ sudo snap connect mysql-workbench-community:removable-media
```

### set remote connection

    connection method   ->  Standard TCP/IP over SSH
    SSH Hostname        ->  ec2-**-***-**-***.XX-central-*.compute.amazonaws.com
    SSH Key File        ->  /home /path_to/key_file.pem
    MySQL Hostname      -> 127.0.0.1
    Mysql Server Port   -> 3306
    Username            -> mysql_username

    Press Test Connection / You might need to logout or restart before connecting

### Using nslookup to get SSH Hostname

    $ nslookup domainname
    > get ip_address

    $ nslookup ip_address
    > get ssh_hostname


