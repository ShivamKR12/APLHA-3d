#!/bin/bash

# Update package list and install VNC server
sudo apt update
sudo apt install -y tightvncserver

# Start VNC server to set up a password
vncserver

# Kill the VNC server instance
vncserver -kill :1

# Create VNC configuration file
cat <<EOL > ~/.vnc/xstartup
#!/bin/bash
xrdb $HOME/.Xresources
startxfce4 &
EOL

# Make the configuration file executable
chmod +x ~/.vnc/xstartup

# Start the VNC server
vncserver :1

echo "VNC server setup is complete. You can connect to the VNC server using your VNC viewer with the address your_server_ip:1"
