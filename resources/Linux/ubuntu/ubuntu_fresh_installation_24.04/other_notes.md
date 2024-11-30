# Install the GRUB bootloader on the NVMe drive located at /dev/nvme0n1, allowing the system to boot from that drive
     
     $ sudo grub-install /dev/nvme0n1

# Copy my .bashrc custom commands and any custom changes made to /etc/profile or files in /etc/profile.d/

# Check /etc/fstab for disk and partition mounting information

# Re-create the following Symbolic links:

     ln -s /home/foxcodenine/foxfiles/AWS AWS
     ln -s /home/foxcodenine/foxfiles/bin bin
     ln -s /home/foxcodenine/foxfiles/deployed_projects deployed_projects
     ln -s /home/foxcodenine/foxfiles/digitalocean digitalocean
     ln -s /home/foxcodenine/foxfiles/Documents Documents
     ln -s /home/foxcodenine/foxfiles/Downloads Downloads
     ln -s /home/foxcodenine/foxfiles/git git
     ln -s /home/foxcodenine/foxfiles/LPIC-1 LPIC-1
     ln -s /home/foxcodenine/foxfiles/Music Music
     ln -s /home/foxcodenine/foxfiles/MyDocker MyDocker
     ln -s /home/foxcodenine/foxfiles/MyDownloads MyDownloads
     ln -s /home/foxcodenine/foxfiles/my-recyle-bin my-recyle-bin
     ln -s /home/foxcodenine/foxfiles/PDF PDF
     ln -s /home/foxcodenine/foxfiles/Pictures Pictures
     ln -s /home/foxcodenine/foxfiles/Projects Projects
     ln -s /home/foxcodenine/foxfiles/Videos Videos
     ln -s /home/foxcodenine/foxfiles/Wallets Wallets


# Remember not to use sudo when installing new programs using flatpak and snap


# Install Essential Tools:

     sudo apt update
     sudo apt upgrade

     git 
     curl 
     grep
     wget
     vim
     zip
     unzip
     gnome-system-monitor
     build-essential
     make
     clamav
     chkrootkit
     rsync
     docker 
     docker-compose
     virtualbox
     nodejs and npm
     php and composer
     



    

