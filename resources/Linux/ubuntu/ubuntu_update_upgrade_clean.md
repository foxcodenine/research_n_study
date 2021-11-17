
------------------------------------------------------------------------

### Error 0 upgraded, 0 newly installed, 0 to remove and 474 not upgraded

    $ sudo apt upgrade

    >> Reading package lists... Done
    >> Building dependency tree       
    >> Reading state information... Done
    >> Calculating upgrade... Done
    >> The following packages have been kept back:
    >> libnvidia-cfg1-450 libnvidia-compute-450 libnvidia-compute-450:i386
    >> libnvidia-decode-450 libnvidia-decode-450:i386 libnvidia-encode-450
    >> ..........
    >> ..........
    >> 0 upgraded, 0 newly installed, 0 to remove and 22 not upgraded.

    $ sudo apt dist-upgrade libnvidia-cfg1-450

    {change libnvidia-cfg1-450 to package you need to update}

------------------------------------------------------------------------
### The following packages were automatically installed and are no longer required

    $ sudo apt autoremove
    or 
    $ sudo apt-get autoremove

------------------------------------------------------------------------