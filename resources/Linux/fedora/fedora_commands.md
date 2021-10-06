### Fedora Delete unnecessary installed dependencies

	       $ dnf autoremove
________________________________________________________________________________

### Fedora Go to Trash

	       $ cd ~/.local/share/Trash
________________________________________________________________________________

### Fedora Install Cups-Pdf

	       $ sudo dnf install cups-pdf

________________________________________________________________________________

### Finding the IP Address of a machine
Enter:

          $ ifconfig

The first inet should be the ip-address that (is not 127.0.0.1)

Else enter:

          $ ip addr

The first inet should be the ip-address that (is not 127.0.0.1)

________________________________________________________________________________

### Connect remotely with ssh
Check you have ssh on both machines by:

          $ ssh

Output should be similar to:

          > usage: ssh [-14ZzdGgFrLtnqsTdDvXxfgU] [-B bind_...

Fetch the Username and IP-Address of the machine you are trying to
connect (server) and enter:

          $ sudo ssh Username@ip_address

Ex:
          $sudo ssh redfoxsix@192.111.0.1

You will be ask for the password of the machine you are trying to (server).
And if it is the first time you are connecting you need to type 'yes'

________________________________________________________________________________
