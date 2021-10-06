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
(1) ----- Check you have ssh on both machines by:
Note your machine is the client, machine you are trying to connect is server

Enter:
		$ ssh          

Output should be similar to:

         > usage: ssh [-14ZzdGgFrLtnqsTdDvXxfgU] [-B bind_...

Else enter:

		$ sudo dnf install openssh

(2) ----- Then on both machines enter:

		$ sudo dnf list --installed | grep openssh

On server you should have

		> openssh...
		> openssh-server...

And on client you should have

		> openssh...
		> openssh-client...

if not enter:

		$ sudo dnf install openssh-server

		or / and:

		$ sudo dnf install openssh-client



(3) ----- Fetch the Username and IP-Address of the server:
username by:
				$ whoami

ip address by:
				$ ip addr

(4) ----- And from the client enter:

          $ sudo ssh Username@ip_address

Ex:
          $sudo ssh redfoxsix@192.111.0.1

If it is the first time you are connecting you need to type 'yes' when asked.
You will be ask for the server password.


________________________________________________________________________________
