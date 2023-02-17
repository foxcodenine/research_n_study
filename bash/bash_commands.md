### rsync

    $ rsync -a --delete --exclude={'sub2','dir3'} a/* b

    $ rsync -arv --delete --exclude={'node_modules','vendor'} ~/Projects/iot/track-iot/ ~/git/repo/iot_solutions/track-iot

    $ rsync -arv --delete --exclude={'node_modules','vendor'} ~/test_rsync ubuntu@ec2-3-73-39-96.eu-central-1.compute.amazonaws.com:~/test_rsync

    rsync -r -t -p -o -g -v --progress --delete --exclude={'node_modules','vendor','011_Fictional_University','.Trash-1000','debugbar'}  --ignore-existing -s /home/foxcodenine/foxfiles /media/foxcodenine/19AD-6262/foxfiles_backup
    
    sudo rsync -r -t -p -o -g -v --progress --exclude={'node_modules','vendor','011_Fictional_University','.Trash-1000','debugbar'}  --ignore-existing -s /home/foxcodenine/foxfiles /media/foxcodenine/19AD-6262/foxfiles_backup
    
     --recursive, -r          recurse into directories
     --times, -t              preserve modification times
     --delete                 delete extraneous files from dest dirs
     --perms, -p              preserve permissions
     --owner, -o              preserve owner (super-user only)
     --group, -g              preserve group
     --verbose, -v            increase verbosity



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