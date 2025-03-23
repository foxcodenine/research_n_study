
# Fixing Monitor Resolution Issue in Ubuntu Budgie (Dynamic Display Setup)

This guide explains the steps taken to resolve monitor resolution issues when switching between different setups (dual HDMI monitors and a single USB-C Thunderbolt monitor) in Ubuntu Budgie 24.04.

---

## Steps

### 1. **Check Monitor Names**

Use `xrandr` to identify connected monitors and their names:

```bash
xrandr --listmonitors
```

Example outputs:
1. Dual HDMI setup:
    ```yaml
    Monitors: 2
      0: +*HDMI-1 3840/609x2160/355+3840+0  HDMI-1
      1: +HDMI-2 3840/597x2160/336+0+0  HDMI-2
    ```
2. USB-C setup:
    ```yaml
    Monitors: 1
      0: +*DP-1 3840/609x2160/355+0+0  DP-1
    ```

In this case:
- `HDMI-1` and `HDMI-2`: Dual HDMI monitors.
- `DP-1`: Monitor connected via USB-C.

---

### 2. **Backup the Configuration File**

Create a backup of the existing LightDM configuration file:

```bash
sudo cp /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf.bak
```

---

### 3. **Create a Dynamic Display Setup Script**

1. Create a script to dynamically configure the display based on connected monitors:
    ```bash
    sudo vi /usr/local/bin/custom-display-setup.sh
    ```

2. Add the following content to the script (press `i` to enter insert mode, paste the content, and press `Esc` to exit insert mode):

    ```bash
    #!/bin/bash

    # Define default resolution and refresh rate
    DEFAULT_MODE="3840x2160"
    DEFAULT_RATE="60"

    # Check connected displays
    HDMI_CONNECTED=$(xrandr | grep "HDMI-1 connected")
    HDMI2_CONNECTED=$(xrandr | grep "HDMI-2 connected")
    DP_CONNECTED=$(xrandr | grep "DP-1 connected")  # Adjusted for DP-1

    # Set up displays based on their connection status
    if [ -n "$HDMI_CONNECTED" ] && [ -n "$HDMI2_CONNECTED" ]; then
        xrandr --output HDMI-1 --mode $DEFAULT_MODE --rate $DEFAULT_RATE --output HDMI-2 --mode $DEFAULT_MODE --rate $DEFAULT_RATE
    elif [ -n "$DP_CONNECTED" ]; then
        xrandr --output DP-1 --mode $DEFAULT_MODE --rate $DEFAULT_RATE --primary  # Adjusted for DP-1
    else
        echo "No known display configuration detected."
    fi
    ```

3. Save and close the file (press `Esc`, type `:wq`, and hit `Enter`).

4. Make the script executable:
    ```bash
    sudo chmod +x /usr/local/bin/custom-display-setup.sh
    ```

---

### 4. **Edit the LightDM Configuration File**

1. Edit the LightDM configuration file:
    ```bash
    sudo vi /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf
    ```

2. Update the `display-setup-script` line to use the new script (press `i` to edit, and after editing, press `Esc`, type `:wq`, and hit `Enter`):
    ```ini
    [Seat:*]
    user-session=budgie-desktop
    allow-guest=false
    display-setup-script=/usr/local/bin/custom-display-setup.sh
    ```

---

### 5. **Restart LightDM**

Restart LightDM to apply the changes:

```bash
sudo systemctl restart lightdm
```

---

### 6. **Test the Changes**

1. For dual HDMI setup: Connect both HDMI monitors, reboot, and confirm they are correctly configured.
2. For USB-C setup: Disconnect HDMI monitors, connect the USB-C monitor, reboot, and confirm it is correctly configured.

---

### 7. **Restore the Backup (if needed)**

If you need to revert to the original configuration, restore the backup:

```bash
sudo mv /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf.bak /etc/lightdm/lightdm.conf.d/50_budgie-desktop.conf
sudo systemctl restart lightdm
```

---

## Summary

This guide outlines a dynamic solution to configure display settings automatically based on connected monitors using a custom `xrandr` script and LightDM's `display-setup-script` option. It eliminates the need for manual configuration changes when switching between dual HDMI and USB-C setups.

---
