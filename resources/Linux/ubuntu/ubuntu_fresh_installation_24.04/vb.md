
To install VirtualBox on Ubuntu Budgie 24.04, follow these steps:

1. **Update your system:** Open a terminal and run the following command to ensure your system is up to date:
    
    bash
    
    Copy code
    
    `sudo apt update && sudo apt upgrade`
    
2. **Install required dependencies:** Before installing VirtualBox, make sure you have the required dependencies installed by running:
    
    bash
    
    Copy code
    
    `sudo apt install build-essential dkms linux-headers-$(uname -r) libqt5opengl5`
    
3. **Add the Oracle VirtualBox repository:** VirtualBox is available in Ubuntu's default repositories, but it is often an older version. To get the latest version, add the Oracle repository.
    
    First, import Oracle’s public key to verify the package authenticity:
    
    bash
    
    Copy code
    
    `wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | sudo gpg --dearmor -o /usr/share/keyrings/oracle_vbox.gpg`
    
    Then, add the VirtualBox repository:
    
    bash
    
    Copy code
    
    `echo "deb [signed-by=/usr/share/keyrings/oracle_vbox.gpg] https://download.virtualbox.org/virtualbox/debian $(lsb_release -cs) contrib" | sudo tee /etc/apt/sources.list.d/virtualbox.list`
    
4. **Update the package list again:** After adding the VirtualBox repository, update your system's package list:
    
    bash
    
    Copy code
    
    `sudo apt update`
    
5. **Install VirtualBox:** Now you can install VirtualBox. To install the latest version (7.0 at the time of writing), run:
    
    bash
    
    Copy code
    
    `sudo apt install virtualbox-7.0`
    
6. **Install the VirtualBox Extension Pack (optional):** If you need extra features like USB 2.0/3.0 support or remote desktop, install the extension pack:
    
    bash
    
    Copy code
    
    `wget https://download.virtualbox.org/virtualbox/7.0.10/Oracle_VM_VirtualBox_Extension_Pack-7.0.10.vbox-extpack sudo VBoxManage extpack install Oracle_VM_VirtualBox_Extension_Pack-7.0.10.vbox-extpack`
    
7. **Launch VirtualBox:** You can launch VirtualBox from your applications menu or by typing:
    
    bash
    
    Copy code
    
    `virtualbox`
    


### Steps to Import Existing Virtual Machines into VirtualBox:

1. **Ensure the Partition is Mounted:** First, ensure that the partition containing your virtual machines is mounted. You can do this manually or use the file manager to mount the partition.
    
2. **Locate Your Virtual Machine Files:** Virtual machines typically consist of several files, the most important of which is the disk image file (usually a `.vdi`, `.vmdk`, `.vhd`, etc.). Look for a file like `machine-name.vbox` or `machine-name.vdi` in the partition where you saved your virtual machines.
    
3. **Add the Existing Virtual Machine in VirtualBox:**
    
    **Option 1: Importing via `.vbox` File (if you have one)**
    
    If you already have a `.vbox` file (which is the configuration file of a VirtualBox machine):
    
    - Open **VirtualBox**.
    - Click on the **"Machine"** menu, then choose **"Add..."**.
    - Browse to the location of your virtual machine (on the partition), select the `.vbox` file, and click **Open**.
    - VirtualBox will import the machine, and you can start using it right away.
    
    **Option 2: Creating a New Virtual Machine with Existing Disk (if you have only the disk file)**
    
    If you only have the virtual disk file (e.g., `.vdi`, `.vmdk`, or `.vhd`):
    
    - Open **VirtualBox**.
    - Click on the **"New"** button to create a new virtual machine.
    - During the virtual machine creation process, instead of creating a new hard disk, choose the option **"Use an existing virtual hard disk file"**.
    - Browse to the location of your virtual machine’s disk file and select it.
    - Finish the setup by configuring the hardware parameters (like memory, CPU, etc.) to match the original setup.
4. **Check and Adjust Settings:** After importing or creating the new virtual machine:
    
    - Go to **Settings** and make sure the configuration matches the original machine (CPU, RAM, network, etc.).
    - You may also need to adjust **shared folders**, **USB devices**, and **network adapters** to match your preferences.
5. **Start the Virtual Machine:** Once you've imported the machine, you should be able to start it from the VirtualBox interface.
    

By following these steps, you can successfully import your virtual machines from another partition into VirtualBox!