# Update all applications on Windows 10

# Import the required modules
import os
import subprocess

# Get the list of installed applications
installed_apps = subprocess.check_output(["wmic", "product", "get", "name"]).strip().split("\n")[1:]

# Iterate over the list of installed applications
for app in installed_apps:
  # Check for updates for the current app
  update_check = subprocess.check_output(["wusa.exe", "/quiet", "/norestart", "/find:{}".format(app)])

  # If updates are available, install them
  if "Updates found" in update_check:
    os.system("wusa.exe /quiet /norestart /install")

# Done
print("All applications on this computer are now up to date.")
