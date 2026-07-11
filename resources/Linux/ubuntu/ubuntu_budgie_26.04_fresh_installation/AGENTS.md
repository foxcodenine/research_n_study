# Context for AI agents

This directory holds notes for migrating from Ubuntu Budgie 24.04 to 26.04.

## Situation

- Ubuntu Budgie **24.04** is on `nvme1n1p5` — this is the currently used, working system.
- Ubuntu Budgie **26.04** is freshly installed on `nvme1n1p4` — not yet set up; had problems (display settings differ a lot from 24.04), so the user booted back into 24.04 until 26.04 is ready.
- `nvme1n1p3` is an old unused Ubuntu install. EFI (`nvme1n1p1`) and swap (`nvme1n1p2`) are shared.
- User data lives on a separate disk mounted at `~/foxfiles` (survives reinstalls). Second data disk at `/media/foxcodenine/storage`.

## Files

- `first_boot_on_26.04.md` — first steps on fresh 26.04: mount foxfiles disk, mount 24.04 partition read-only for configs.
- `migration_checklist_from_24.04.md` — full snapshot of apps, languages, and configs on 24.04 to reinstall/copy onto 26.04. Taken 2026-07-11; if run on a later date, re-verify before trusting versions.
- `installing-26.04-and-reverting-to-24.04-until-ready.md` — install notes, partition layout, and the GRUB/fstab fixes done from 24.04.
- `../ubuntu_budgie_24.04_fresh_installation/` — the equivalent notes from the previous (24.04) migration; useful reference, especially the monitor-resolution fixes.

## Rules

- These are documentation notes. When asked to inventory or inspect the system, **read-only** — do not install, remove, or reconfigure anything unless explicitly asked.
- Which OS you are running on matters: check `lsb_release -a` / the root partition before assuming 24.04 vs 26.04.
- Before anything destructive toward the 24.04 partition, remember it holds data not yet migrated (MySQL databases, Docker volumes).
