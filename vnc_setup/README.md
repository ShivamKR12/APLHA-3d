# VNC Setup

This document provides instructions for setting up a VNC server in a separate directory outside the main game directory. The VNC server will run independently and will not interfere with the main game files.

## Prerequisites

- A Linux-based operating system
- Root or sudo access

## Steps

1. **Create a new directory for VNC setup:**

   ```bash
   mkdir -p ~/vnc_setup
   cd ~/vnc_setup
   ```

2. **Install VNC server:**

   ```bash
   sudo apt update
   sudo apt install -y tightvncserver
   ```

3. **Configure VNC server:**

   - Start the VNC server to set up a password:

     ```bash
     vncserver
     ```

   - Kill the VNC server instance:

     ```bash
     vncserver -kill :1
     ```

   - Create a VNC configuration file:

     ```bash
     nano ~/.vnc/xstartup
     ```

     Add the following lines to the file:

     ```bash
     #!/bin/bash
     xrdb $HOME/.Xresources
     startxfce4 &
     ```

   - Make the file executable:

     ```bash
     chmod +x ~/.vnc/xstartup
     ```

4. **Start the VNC server:**

   ```bash
   vncserver :1
   ```

5. **Access the VNC server:**

   - Use a VNC viewer to connect to the VNC server. The address will be `your_server_ip:1`.

6. **Stop the VNC server:**

   ```bash
   vncserver -kill :1
   ```

## Notes

- Ensure that the VNC server runs independently and does not interfere with the main game files.
- Document any issues encountered during the setup process and their resolutions.

By following these steps, you will have a VNC server set up in a separate directory outside the main game directory, running independently without causing any major connections or errors in the main files.
