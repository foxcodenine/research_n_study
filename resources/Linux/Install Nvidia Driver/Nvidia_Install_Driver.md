### [PROBLEM 1] I found that I my NVIDIA card wasn't installed properly when I have read this arlicle:

    Solved_ Thunderbolt Port not recognized in Linux Ubuntu Inspiron 16 7610 - Dell Community.pdf

### I have run this command and found that my graphic card was unclaimed:
### ('UNCLAIMED' means that no driver has been loaded for that card. )

    sudo lshw -c display

[lshw is a small tool to extract detailed information on the hardware configuration of the machine.]

### I have found this articl and followed the first solution, which is the following:

    $ ubuntu-drivers devices
    $ sudo ubuntu-drivers autoinstall
    $ sudo reboot

### A pdf of both articles is in this same directory. 
### I have also found this command which I need to look into it:
    dkms - Dynamic Kernel Module Support

<!-- --------------------------------------------------------------- -->

### [PROBLEM 2] I have switch GPU from NVIDIA to Intel from Nvidia settings to save power.
### However this created an issue and I was being logged off continuously
### Solution:

        $ sudo ubuntu-drivers devices
        $ sudo apt-get install <change to your recomanded driver ex: nvidia-352>

    To check which card is being used right now, run:

        $ prime-select query
    
    To switch to Nvidia card <-

        $ sudo prime-select nvidia
    
    To switch to Intel 

        $ sudo prime-select intel

    If prime-select does not work try:

        $ sudo apt install nvidia-prime

    
        

