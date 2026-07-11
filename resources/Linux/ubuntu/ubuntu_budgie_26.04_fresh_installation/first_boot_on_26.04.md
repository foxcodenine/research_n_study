# First Boot on 26.04 — Getting Started

First steps after booting into the fresh Ubuntu Budgie 26.04 on `nvme1n1p4`.

<!-- --------------------------------------------------------------- -->

#### 1. Mount the foxfiles disk (the notes live there)

The migration checklist is on the foxfiles data disk, which is not mounted
on a fresh install:

    $ sudo mkdir -p /home/foxcodenine/foxfiles
    $ sudo mount UUID=bb64ca12-92b0-47ff-bf12-a65b4037f0ab /home/foxcodenine/foxfiles

Then make it permanent — add to `/etc/fstab` (storage disk too):

    # foxfiles data disk
    /dev/disk/by-uuid/bb64ca12-92b0-47ff-bf12-a65b4037f0ab  /home/foxcodenine/foxfiles  ext4  defaults  0  2

    # storage disk
    UUID=fb3028b7-984a-43dd-819b-40d9a2f1616d  /media/foxcodenine/storage  ext4  defaults  0  2

Verify:

    $ sudo mkdir -p /media/foxcodenine/storage
    $ sudo systemctl daemon-reload
    $ sudo mount -a

<!-- --------------------------------------------------------------- -->

#### 2. Access old configs on the 24.04 partition

24.04 is intact on `nvme1n1p5`. Mount it read-only to copy configs
(`.ssh`, `.bashrc`, `.gitconfig`, `.aws`, `.claude`, etc.):

    $ sudo mount -o ro /dev/nvme1n1p5 /mnt

Old home is then at:

    /mnt/home/foxcodenine/

Full list of what to copy: `migration_checklist_from_24.04.md` section 8.

When done:

    $ sudo umount /mnt

<!-- --------------------------------------------------------------- -->

#### 3. Follow the migration checklist

Everything to reinstall (apt, snaps, languages, VS Code extensions, docker):

    migration_checklist_from_24.04.md

<!-- --------------------------------------------------------------- -->

#### Notes

- No rush on MySQL dump / Docker volumes — 24.04 stays bootable on
  `nvme1n1p5`; boot back into it anytime if 26.04 has problems.
- Start Claude Code from this folder — it picks up `AGENTS.md` / `CLAUDE.md`
  context automatically.
