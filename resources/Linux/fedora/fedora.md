### Set up Grub

When installing Fedora, Fedora will take over grub.

To set it back from Ubuntu you need to do the following steps:

(1) First install grub-customizer which is GRUB Customizer package.

      $ sudo dnf install -y grub-customizer

(2) Run grub-customizer on terminal. Or Open from apps.

      $ sudo grub-customizer

It should show you all the installations in the List configuration.
Ex Ubuntu, Windows, Fedora, Xubuntu ...
You need to copy the Fedora confiuration to Save it (or past it)
in to Ubuntu GRUB Customizer.

However if Fedora does not show on the List configurations try the following :

(3) Open /etc/default/grub with a text edito (nano, atom, etc...)

      $ atom /etc/default/grub

(4) and edit the following line from:

      GRUB_ENABLE_BLSCFG="true"
to:
      GRUB_ENABLE_BLSCFG="false"

You can check if it's value by:

      $ cat /etc/default/grub

(5) Reopen GRUB Customizer and copy the Fedora configuration.

(6) Restart and select Ubuntu.

(7) Open GRUB Customizer and Create a new Entry.
    And Save/Past the Fedora configuration.

(8) Arrange the order of installation and Close -> Update & Quit.

(9) Last step is to Re-install Grub to be set as default from Ubuntu.
    1st find you hard disk name using  $ lsblk and checking the /dev diectory
    The result should be (might be) like sd? or nvme???
    Then reinstall grub by:
      
      $ sudo grub-install /dev/your_hard_disk_name
      Ex:    
      $ sudo grub-install /dev/sda
      or
      $ sudo grub-install /dev/nvme0n1

(10) Next time you restart, grub should display all installation
     as set on GRUB Customizer on Ubuntu, including Fedora option.

________________________________________________________________________________
### Fedora Config Ex:

Name: Fedora (5.11.12-300.fc34.x86_64) 34 (Workstation Edition)
Type: Other

load_video
set gfxpayload=keep
insmod gzio
insmod part_gpt
insmod ext2
set root='hd0,gpt6'
if [ x$feature_platform_search_hint = xy ]; then
  search --no-floppy --fs-uuid --set=root --hint-bios=hd0,gpt6 --hint-efi=hd0,gpt6 --hint-baremetal=ahci0,gpt6  b19145f7-8384-482d-a36c-96df682b5a70
else
  search --no-floppy --fs-uuid --set=root b19145f7-8384-482d-a36c-96df682b5a70
fi
linux    /vmlinuz-5.11.12-300.fc34.x86_64 root=UUID=bbf2d932-55c7-4a5b-9f84-79a701b7feb9 ro rootflags=subvol=root rhgb quiet
initrd    /initramfs-5.11.12-300.fc34.x86_64.img

________________________________________________________________________________
