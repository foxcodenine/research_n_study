# Fixing Monitor Resolution Issue in Ubuntu Budgie (Logging Screen)
## Superseded 
##### Use fixing_monitor_resolution_dynamic_setup.md

This guide explains the steps taken to resolve a monitor resolution issue with a portable monitor (`HDMI-2`) in Ubuntu Budgie 24.04.

---

## Steps

### 1. **Check Monitor Names**

Use `xrandr` to identify connected monitors and their names:

```bash
`xrandr --listmonitors`
```

Example output:

```yaml
Monitors: 2  0: +*HDMI-1 3840/609x2160/355+3840+0  HDMI-1  1: +HDMI-2 3840/597x2160/336+0+0  HDMI-2
```

In this case:

- `HDMI-1`: Primary monitor
- `HDMI-2`: Portable monitor

---

### 2. **Backup the Configuration File**

Create a backup of the LightDM configuration file:

```bash
sudo cp /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf.bak
```
---

### 3. **Edit the Configuration File**

Edit the LightDM configuration file:

```bash
sudo vi /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf
```

Add or update the following lines:

```ini
[Seat:*]
user-session=budgie-desktop
allow-guest=false
display-setup-script=/usr/bin/xrandr --output HDMI-2 --mode 3840x2160 --rate 60 --output HDMI-1 --mode 3840x2160 --rate 60
```
---

### 4. **Restart LightDM**

Apply the changes by restarting LightDM:

```bash
`sudo systemctl restart lightdm`
```

---

### 5. **Test the Changes**

Log out and log back in to verify that the portable monitor (`HDMI-2`) displays correctly.

---

### 6. **Restore the Backup (if needed)**

If you need to revert to the original configuration, restore the backup:

```bash
`sudo mv /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf.bak /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf sudo systemctl restart lightdm`
```
---

## Summary

This guide fixes a monitor skewing issue during login on Ubuntu Budgie by explicitly setting resolutions and refresh rates for both monitors using `xrandr` in the LightDM configuration file.