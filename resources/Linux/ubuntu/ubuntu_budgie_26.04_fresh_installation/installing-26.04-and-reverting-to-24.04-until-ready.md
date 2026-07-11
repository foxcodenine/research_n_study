#### Context

Already had two Ubuntu installs on `nvme1n1`:
- `nvme1n1p3` - old/unused Ubuntu install
- `nvme1n1p5` - working Ubuntu Budgie 24.04 (kept)

Installed Ubuntu Budgie 26.04 on `nvme1n1p4` (400G).

Did not like 26.04 (display settings changed significantly from 24.04).
Booted back into 24.04 on `nvme1n1p5` to fix GRUB and fstab.

<!-- --------------------------------------------------------------- -->

#### USB Installation Media

Created bootable USB using Rufus 4.15:
- ISO: `ubuntu-budgie-26.04-desktop-amd64.iso`
- Partition scheme: GPT
- Target system: UEFI (non CSM)
- File system: Large FAT32

<!-- --------------------------------------------------------------- -->

#### Partition Layout (nvme1n1)

| Partition    | Size  | Role                        |
|--------------|-------|-----------------------------|
| nvme1n1p1    | 1G    | EFI (shared)                |
| nvme1n1p2    | 64G   | swap (shared)               |
| nvme1n1p3    | 400G  | old unused Ubuntu install   |
| nvme1n1p4    | 400G  | Ubuntu Budgie 26.04 (new)   |
| nvme1n1p5    | 400G  | Ubuntu Budgie 24.04 (kept)  |

<!-- --------------------------------------------------------------- -->

#### Fix fstab (from 24.04 on nvme1n1p5)

After install, drive names shifted (nvme0n1 ↔ nvme1n1).
Updated `/etc/fstab` with correct UUIDs:

    $ sudo blkid
    $ sudo vi /etc/fstab

Updated entries:
- swap: `6d837122-9620-4eab-9652-78607d90f6d2` (nvme1n1p2)
- /boot/efi: `B879-11D1` (nvme1n1p1)

Check syntax:

    $ sudo mount -a

<!-- --------------------------------------------------------------- -->

#### Reinstall GRUB (from 24.04 on nvme1n1p5)

EFI partition is on `nvme1n1p1`. Mounted it and reinstalled GRUB:

    $ sudo umount /boot/efi
    $ sudo mount /dev/nvme1n1p1 /boot/efi
    $ sudo grub-install /dev/nvme1n1
    $ sudo update-grub

GRUB now detects all three Ubuntu installs on boot.

<!-- --------------------------------------------------------------- -->

#### TODO

    $ sudo apt update && sudo apt upgrade -y

Fix dual monitor (second monitor not detected — likely resolves after kernel update)

Set Display scaling to x200
