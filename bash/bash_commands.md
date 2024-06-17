### rsync

    $ rsync -a --delete --exclude={'sub2','dir3'} a/* b

    # -a: This option is a short form of --archive and is used to preserve symbolic links, permissions, timestamps, ownerships, and groups, and to recursively copy directories. 

    # --delete: This option tells rsync to delete extraneous files from the receiving side (in directory b) that do not exist on the sending side (in directory a). 

    # --exclude={'sub2','dir3'}: This option excludes the specified directories (sub2 and dir3) from being synchronized.

    # a/*: This specifies the source directory from which files are to be copied. The asterisk * is a wildcard character that represents any character or group of characters.

    $ rsync -arv --delete --exclude={'node_modules','vendor'} ~/Projects/iot/track-iot/ ~/git/repo/iot_solutions/track-iot

    $ rsync -arv --delete --exclude={'node_modules','vendor'} ~/test_rsync ubuntu@ec2-3-73-39-96.eu-central-1.compute.amazonaws.com:~/test_rsync

    rsync -r -t -p -o -g -v --progress --delete --exclude={'node_modules','vendor','011_Fictional_University','.Trash-1000','debugbar'}  --ignore-existing -s /home/foxcodenine/foxfiles /media/foxcodenine/19AD-6262/foxfiles_backup
    
    sudo rsync -r -t -p -o -g -v --progress --exclude={'node_modules','vendor','011_Fictional_University','.Trash-1000','debugbar'}  --ignore-existing -s /home/foxcodenine/foxfiles /media/foxcodenine/19AD-6262/foxfiles_backup
    
     --recursive, -r          enable the recursive copying
     --times, -t              preserve modification times
     --delete                 delete extraneous files from dest dirs
     --perms, -p              preserve permissions
     --owner, -o              preserve owner (super-user only)
     --group, -g              preserve group
     --verbose, -v            increase verbosity

     -s                       this option is used to show the sizes of the files during the transfer
     -h                       this option enables human-readable file sizes, showing them in a more understandable format.

     --ignore-existing        this option tells rsync to skip files that already exist in the destination, avoiding overwriting any existing files.

    --bwlimit=5000K           this option limits the bandwidth used by rsync to transfer the file. In this case, it limits the transfer rate to 5000 kilobytes per second (or 5 megabytes per second), which can be helpful in controlling the impact on network performance during the transfer.

    rsync -ah --progress  --bwlimit=5000K /home/foxcodenine/Lubuntu-VB/11.mp4 /media/foxcodenine/corsair/

    $ sudo rsync -art --progress --exclude='/var/lib/flatpak/repo/objects' --exclude='/var/lib/docker/overlay2' --exclude='node_modules' --exclude='/var/lib/flatpak/runtime' --exclude='/var/lib/snapd/assertions' --exclude='/var/lib/swcatalog/icons' --bwlimit=50000K /var --ignore-existing /media/foxcodenine/ubuntu_root/main

    $ sudo rsync -art --progress  --bwlimit=50000K /etc --ignore-existing /media/foxcodenine/ubuntu_root/main
    

    $ rsync -art --progress  --bwlimit=50000K --exclude='VirtualBox VMs' --exclude='Lubuntu-VB' --exclude='*Cache*' --exclude='*cache*' --exclude='Docker.raw' --exclude='.android' --exclude='BraveSoftware' --exclude='.cache' --exclude='android-33' --exclude='EVO790plus' --exclude='node_modules' --exclude='pCloudDrive' --exclude='foxfiles' /home/foxcodenine  --ignore-existing /media/foxcodenine/ubuntu_root/main/home

    <!-- ------------------------------------------------------------------- -->
    
    <!-- as root -->

    <!-- copy etc -->
    rsync -artv --progress  --bwlimit=50000K /etc --ignore-existing '/media/foxcodenine/T7 Touch/backups/ubuntu_budgie_22.04'


    <!-- copy var -->
    rsync -artv --progress --exclude='/var/lib/flatpak/repo/objects' --exclude='/var/lib/docker/overlay2' --exclude='node_modules' --exclude='/var/lib/flatpak/runtime' --exclude='/var/lib/snapd/assertions' --exclude='/var/lib/swcatalog/icons' --bwlimit=50000K /var --ignore-existing '/media/foxcodenine/T7 Touch/backups/ubuntu_budgie_22.04';

    <!-- copy home -->
    rsync -artv --delete --progress  --bwlimit=50000K --exclude='VirtualBox VMs' --exclude='*Cache*' --exclude='*cache*' --exclude='Docker.raw' --exclude='.android' --exclude='BraveSoftware'  --exclude='.cache' --exclude='android-33' --exclude='EVO790plus' --exclude='node_modules' --exclude='pCloudDrive' --exclude='foxfiles' /home/foxcodenine  --ignore-existing '/media/foxcodenine/T7 Touch/backups/ubuntu_budgie_22.04/home';

    <!-- copy foxfiles -->
    rsync -artv --delete --progress  --bwlimit=50000K --exclude='befor-format' --exclude='foxfiles/git' --exclude='.Trash-1000' --exclude='vendor' --exclude='node_modules' /home/foxcodenine/foxfiles --ignore-existing '/media/foxcodenine/T7 Touch/backups';

    <!-- copy pCloudDrive -->
    rsync -artv --delete --progress  --bwlimit=50000K /home/foxcodenine/pCloudDrive --ignore-existing '/media/foxcodenine/T7 Touch/backups/'

    <!-- installations -->
    snap list  > snap_list.txt;
    flatpak list  > flatpak_list.txt;
    code --list-extensions > vscode_extention_list.txt;

    <!-- tar and copy git -->
    tar -czvf /media/foxcodenine/T7\ Touch/backups/git_backup.tar.gz /home/foxcodenine/foxfiles/git;





### gpg

    $ gpg -c .env

using find and passphrase-file:

    $ find *   -name my-file  -exec gpg --passphrase-file='./gpg_file' --pinentry-mode loopback -c  {} \;

Note: '--pinentry-mode loopback' is need else '--passphrase-file' will be ignored 
and bash will ask for password.

Decrypting: 

    $ gpg -d my-file.gpg > my-file

The phrase is cached by the GPG agent.
To clear the cache simply run

    $ gpg-connect-agent reloadagent /bye


### rename

    $ find *   -name aaa.a  -exec   rename 's/aaa.a/abc/' {} \;

### firewall

Check Firewall Status

    $ sudo ufw status
    $ sudo ufw status verbose

Display firewall rule numbers:

    $ sudo ufw status numbered

Delete the firewall rule number

    $ sudo ufw delete 4


### nping

    $ sudo nping --tcp -p {port} {host}

    $ sudo nping --tcp -p 443 www.cyberciti.biz

    $ sudo nping --tcp -p 6767 141.8.23.81


### ip address

for private:

    $ ip route get 1.2.3.4 | awk '{print $7}'
    $ hostname -I | awk '{print $1}'

for public:

    $ dig +short myip.opendns.com @resolver1.opendns.com

    $ curl ifconfig.co
    $ curl ifconfig.me
    $ curl icanhazip.com




### PostgreSQL via SSH Tunnel

Fowarding a port:

    $ ssh -L 1111:localhost:5432 user@remote.example.com


If this is expected to be a long-running tunnel, I would recommend using autossh
To connect using the psql client on the host where you are running the ssh client, use something like this:

    $ psql -h localhost -p 1111 -U your-db-username database-name

Alternately, you can add a line line the following to a file called .pgpass in your home directory on the client where you're running ps

    $ localhost:1111:database-name:your-db-user:your-db-password