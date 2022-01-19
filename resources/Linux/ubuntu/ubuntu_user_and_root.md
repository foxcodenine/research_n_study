### ---- Enable ssh to root -----------------------------------------------------------------------------

	Edit the following file
		$ vi /etc/ssh/sshd_config
	Add the following line (it might already exist but commented out or set to Off):
		PermitRootLogin yes
	Save and exit and restart ssh server by :
		$ systemctl restart sshd 
	
	When using SSH Keys, you can set the PermitRootLogin value to `without-password` instead of yes. 
	Simply modify the following information noted in step 2 above instead:
		$ PermitRootLogin without-password
	
	To work you might also need to set the root password by:
		$ passwd root
		> ********
		> ******** 
		
---------------------------------------------------------------------------------------------------------		
	
	
