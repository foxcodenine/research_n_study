
<!-- --------------------------------------------------------------- -->

### At pc start/restart from Grub menu

        * Windows
        * Ubuntu
        * ......
        * ...

    press 'c' to enter the Grub cli


    to display all drives:
        
        grub> ls
    
    to check / list file and folder on a specific drive:

        grub> root(hd0,gpt1)tab

    to get the drive uuid:

        grib> ls (hd0,gpt1)



    to boot from a specifed drive (ex: bood image drive)

        grib> insmod part_gpt

        grib> insmod fat

        grib> insmod search_fs_uuid

        grib> insmod chain

        grib> search --fs-uuid --set=root 3A28-CE43

            change 3A28-CE43 to your uuid

        grib> chainloader /efi/boot/bootx64.efi

        grib> boot

<!-- --------------------------------------------------------------- -->


## To set another boot option at pc start in grub menu

    open grub Customizer

    Create a new Entry

    in Name: 
        Set you option Name

    in Type: 
        Other

    in Boot sequence insert the above sequence we did at grub menu with 
    the correct uuid:

        grib> insmod part_gpt

        grib> insmod fat

        grib> insmod search_fs_uuid

        grib> insmod chain

        grib> search --fs-uuid --set=root 3A28-CE43

            change 3A28-CE43 to your uuid

        grib> chainloader /efi/boot/bootx64.efi

        grib> boot

    
