# Install PowerToys on Windows 10

# Import the required modules
import os
import subprocess
import webbrowser

# Display a message to the user
print("This script will install PowerToys on your computer.")

# Prompt the user to start the script
response = input("Would you like to continue? (y/n) ")

# If the user enters "y", start the script
if response.lower() == "y":
  # Install Chocolatey if it is not already installed
  choco_check = subprocess.check_output(["choco", "--version"])
  if "not found" in choco_check:
    os.system("powershell Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))")

  # Install PowerToys using Chocolatey
  os.system("choco install powertoys -y")

  # Open a web page in the default web browser
  webbrowser.open("https://learn.microsoft.com/en-us/windows/powertoys/")

  # Done
  print("PowerToys has been installed on this computer.")

# If the user enters "n", exit the script
else:
  print("Exiting script.")
