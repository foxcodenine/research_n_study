### I found that I my NVIDIA card wasn't installed properly when I have read this arlicle:

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