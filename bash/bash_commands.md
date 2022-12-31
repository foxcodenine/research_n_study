### rsync

    $ rsync -a --delete --exclude={'sub2','dir3'} a/* b

    $ rsync -arv --delete --exclude={'node_modules','vendor'} ~/Projects/iot/track-iot/ ~/git/repo/iot_solutions/track-iot

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
