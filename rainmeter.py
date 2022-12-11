# Install Rainmeter and Jaxcore on Windows 10

# Import the required module
import os

# Display a message to the user
print("This script will install Rainmeter and Jaxcore on your computer.")

# Prompt the user to start the script
response = input("Would you like to continue? (y/n) ")

# If the user enters "y", start the script
if response.lower() == "y":
  # Install Rainmeter
  os.system("msiexec /i rainmeter.msi /quiet")

  # Install Jaxcore
  os.system("msiexec /i jaxcore.msi /quiet")

  # Done
  print("Rainmeter and Jaxcore have been installed on this computer.")

# If the user enters "n", exit the script
else:
  print("Exiting script.")
