# Migration Checklist — Ubuntu Budgie 24.04 (nvme1n1p5) → 26.04 (nvme1n1p4)

Snapshot of everything installed/configured on the 24.04 system, taken 2026-07-11.
Nothing here is auto-generated on the new system — this is the reinstall list.

---

## 1. Third-party APT repositories (add before installing)

| Repo | Source file on 24.04 | Provides |
|---|---|---|
| Docker | `docker.list` | docker-ce, docker-ce-cli, containerd.io |
| Brave | `brave-browser-release.sources` | brave-browser |
| VS Code (Microsoft) | `vscode.sources` | code |
| Ubuntu Budgie backports PPA | `ubuntubudgie-ubuntu-backports-noble.sources` | budgie extras/applets |

> Note: MySQL uses `mysql-apt-config` (installed as a package). VirtualBox 7.2, GitKraken, DBeaver, MongoDB Compass, Zoom, MySQL Workbench were most likely installed from downloaded `.deb` files — re-download from their sites.

## 2. APT packages (manually installed)

### Browsers / Internet
- brave-browser
- filezilla
- thunderbird (also installed as snap — pick one)
- zoom (.deb from zoom.us)

### Development — editors & IDE tools
- code (VS Code)
- gitkraken (.deb)
- dbeaver-ce (.deb)
- mysql-workbench-community (.deb)
- mongodb-compass (.deb)
- kitty (terminal)
- tilix (terminal — NOT included by default on 26.04, install with apt; settings live in dconf, covered by the dconf dump in section 8)
- vim
- git, git-filter-repo

### Development — languages / build
- build-essential
- php, php-fpm, php8.3-mysql, php8.3-pgsql, php8.3-sqlite3, php8.3-xml
- composer
- libmysqlclient-dev, libmysqlcppconn-dev, libvips-dev

### Servers / databases
- apache2, libapache2-mod-fcgid
- mysql-server (+ mysql-apt-config)
- mongodb-mongosh

### Docker / virtualization
- docker-ce, docker-ce-cli, containerd.io
- virtualbox-7.2 (Oracle .deb/repo) + dkms
- docker-compose v1 binary lives in `/usr/local/bin/docker-compose` (legacy 1.29.2)

### Media / graphics
- vlc, mpv, obs-studio, krita, cheese
- gnome-screenshot, gnome-calculator
- ubuntu-restricted-addons

### Hardware / peripherals
- epson-inkjet-printer-escpr2 (Epson printer)
- printer-driver-cups-pdf
- skanlite (scanner)
- solaar (Logitech)
- trezor-udev (Trezor udev rules)
- lm-sensors, smartmontools
- adb, jmtpfs, mtp-tools (Android/MTP)

### Budgie desktop extras
- budgie-calendar-applet
- budgie-cputemp-applet
- gnome-shell-extension-desktop-icons-ng
- moka-icon-theme

### Chess (hobby)
- pychess, scid, stockfish, python3-pygame

### Misc utilities
- curl, wget, net-tools, neofetch, plocate, cowsay
- flatpak
- binwalk

## 3. Snap packages

- firefox
- postman
- redisinsight
- restfox
- smplayer
- kooha (screen recorder)
- teams-for-linux
- onenote-desktop
- whatsapp-linux-desktop
- gtk-theme-pocillo (usually pulled in by Budgie)
- canonical-livepatch (re-attach Ubuntu Pro if used)

## 4. Flatpak apps

- md.obsidian.Obsidian (also have AppImage — pick one)
- io.atom.Atom (dead project — probably skip)

## 5. AppImages (in `~/foxfiles/AppImages` — on separate disk, survives reinstall)

- Cursor (aliased in .bashrc)
- Beekeeper-Studio (aliased in .bashrc)
- pCloud (+ autostart entry)
- Obsidian
- Trezor Suite, Ledger Live, Sync2 (in `~/foxfiles/Wallets`)
- Telegram (aliased in .bashrc, binary at `~/foxfiles/AppImages/Telegram`)

> AppImages live on the foxfiles disk so no reinstall needed — just recreate the .bashrc aliases and the pCloud autostart entry.

## 6. Programming languages & toolchains (manual installs)

| Tool | Version on 24.04 | Install method |
|---|---|---|
| Go | 1.25.4 | tarball in `/usr/local/go`, PATH in .bashrc |
| Node | v22.17.1 (+ v20.18.0) | **nvm** (`~/.nvm`) |
| Rust | 1.91.1 | rustup (`~/.rustup`, `~/.cargo`) |
| Bun | 1.3.12 | official installer (`~/.bun`) |
| PHP | 8.3 | apt |
| Python | 3.12 (system) | apt |
| Composer | 2.7.1 | apt |
| Terraform | — | binary in `/usr/local/bin/terraform` (+ bash completion in .bashrc) |
| AWS CLI | — | `/usr/local/bin/aws` (official installer) |
| Claude Code | — | `/usr/local/claude/claude` (PATH in .bashrc) |
| Anki | — | `/usr/local/bin/anki` |

### Go tools (`~/go/bin` — reinstall with `go install`)
- gopls, staticcheck, errcheck, garble

### Global npm packages
- @openai/codex
- live-server
- corepack

## 7. Docker (recreate on new system)

Running container:
- **portainer** (`portainer/portainer-ce:latest`) — see repo notes "added portainer install notes"

Images in use (pull as needed):
- mongodb/mongodb-community-server:8.0-ubi8, redis:latest, rabbitmq:3-management, mariadb:10.6.11, nginx:1.27-alpine

> ⚠️ Check for docker volumes with data worth exporting before wiping 24.04: `docker volume ls`

## 8. Configs to COPY from 24.04 partition (nvme1n1p5)

### Shell / git / ssh (highest priority)
- `~/.bashrc` — custom section at bottom: Go PATH, bun, claude, cargo env, aliases (`hist`, `git-add-foxcodenine`, `git-add-chrisfarrugiadev`, `cursor`, `telegram`, `beekeeper`), `gacp()` function, terraform completion
- `~/.gitconfig`
- `~/.ssh/` — **entire folder**: `id_ed25519`, `chris_farrugia_dev_git/`, `ovh`, `ssh_iot`, `config`, `authorized_keys`
- `~/.gnupg/` (GPG keys)

### App configs (`~/.config/...`)
- `~/.config/Code/User/` (VS Code settings/keybindings) — extensions list in section 9
- `~/.config/kitty/`
- `~/.config/filezilla/` (saved site credentials!)
- `~/.config/autostart/` (pcloud.desktop, plank.desktop)
- `~/.config/monitors.xml` (display layout)
- `~/.config/plank/` (dock layout)
- `~/.config/budgie-desktop/`, `~/.config/budgie-extras/` (panel layout — or use Budgie Desktop Settings export)
- `~/.config/obs-studio/` (scenes/profiles)
- `~/.config/GitKraken/`, `~/.config/beekeeper-studio/`
- dconf dump for desktop settings: `dconf dump / > dconf-backup.ini` (restore: `dconf load / < dconf-backup.ini`)

### Credentials / cloud
- `~/.aws/` (AWS credentials)
- `~/.claude/` + `~/.claude.json`
- `~/.docker/config.json` (registry logins)
- `~/.terraform.d/`

### Other
- `/usr/local/bin/custom-display-setup.sh` (xrandr 4K display script — see 24.04 notes on monitor resolution fix)
- `~/.vim/` if customized
- VirtualBox VMs: `~/VirtualBox_VMs` + `~/.config/VirtualBox`
- Thunderbird profile: `~/snap/thunderbird/` or `~/.thunderbird`

### Data exports (do BEFORE wiping 24.04)
- MySQL databases: `mysqldump --all-databases`
- Docker volumes (see section 7)
- `~/.mongodb`, `~/.dbclient`, `~/.rest-client` if they hold saved connections

## 9. VS Code extensions

Reinstall loop: `while read e; do code --install-extension "$e"; done < vscode-extensions.txt`

```
1natsu.insert-br-tag
amazonwebservices.aws-toolkit-vscode
amiralizadeh9480.laravel-extra-intellisense
anthropic.claude-code
bmewburn.vscode-intelephense-client
bradlc.vscode-tailwindcss
burkeholland.simple-react-snippets
casualjim.gotemplate
codingyu.laravel-goto-view
cweijan.dbclient-jdbc
cweijan.vscode-mysql-client2
dakshmiglani.hex-to-rgba
diogogmt.jet
docker.docker
drblury.protobuf-vsc
eamodio.gitlens
formulahendry.auto-rename-tag
golang.go
greven.umbra
hashicorp.hcl
hashicorp.terraform
hollowtree.vue-snippets
humao.rest-client
mariorodeghiero.vue-theme
mrmlnc.vscode-apache
ms-azuretools.vscode-containers
ms-azuretools.vscode-docker
ms-kubernetes-tools.vscode-kubernetes-tools
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
ms-python.vscode-python-envs
onecentlin.laravel-blade
onecentlin.laravel5-snippets
openai.chatgpt
phproberto.vscode-php-getters-setters
redhat.vscode-xml
redhat.vscode-yaml
ritwickdey.liveserver
ryannaddy.laravel-artisan
sdras.vue-vscode-snippets
shadowblood.tailwind-moon
shd101wyy.markdown-preview-enhanced
shufo.vscode-blade-formatter
sidthesloth.html5-boilerplate
silasnevstad.gpthelper
stkb.rewrap
txpipe.aiken
vincaslt.highlight-matching-tag
vue.volar
wayou.vscode-icons-mac
wayou.vscode-todo-highlight
```

## 10. fstab — extra mounts to re-add on 26.04

(adjust root/EFI lines to the new install; these two are the ones to carry over)

```
# foxfiles data disk
/dev/disk/by-uuid/bb64ca12-92b0-47ff-bf12-a65b4037f0ab  /home/foxcodenine/foxfiles  ext4  defaults  0  2

# storage disk
UUID=fb3028b7-984a-43dd-819b-40d9a2f1616d  /media/foxcodenine/storage  ext4  defaults  0  2
```

## 11. System services / hardware setup

- Docker: `sudo usermod -aG docker foxcodenine`
- VirtualBox: add user to `vboxusers` group
- Epson printer + CUPS-PDF setup
- Trezor udev rules (`trezor-udev` package)
- `sudo sensors-detect` (lm-sensors)
- Ubuntu Pro / livepatch attach (if used)
- Monitor resolution fix at login screen — see `../ubuntu_budgie_24.04_fresh_installation/fixing_monitor_resolution_issue_in_ubuntu_budgie_logging_screen.md` and `fixing_monitor_resolution_dynamic_setup.md`

## 12. Existing notes to reference

- `../ubuntu_budgie_24.04_fresh_installation/new-ubuntu-installation.md`
- `../ubuntu_budgie_24.04_fresh_installation/vscode.md` + `install-vscode-extensions.sh`
- `../ubuntu_budgie_24.04_fresh_installation/vb.md` (VirtualBox)
- `../ubuntu_budgie_24.04_fresh_installation/other_notes.md`
- `../ubuntu_update_upgrade_clean.md`, `../ubuntu_user_and_root.md`, `../usefull_tools.txt`
