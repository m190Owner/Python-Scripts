# Import the required modules
import subprocess
import os
import shutil
import ctypes

# Check if the script is running with administrator privileges
if ctypes.windll.shell32.IsUserAnAdmin() == 0:
    # Re-run the script with administrator privileges
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)

# Check if Git is already installed
git_installed = shutil.which("git") is not None

# Install Git using winget if it is not already installed
if not git_installed:
    subprocess.call(["winget", "install", "git"])

# Clone the lively wallpaper repository from GitHub and install the package
try:
    subprocess.call(["git", "clone", "https://github.com/rocksdanister/lively"])
    os.chdir("lively")
    subprocess.call(["git", "install", "."])

# Handle any exceptions that may be raised by the git clone or git install commands
except Exception as e:
    print(f"An error occurred while installing lively wallpaper: {e}")

# Use lively wallpaper to set the desktop background
subprocess.call(["lively-wallpaper"])
