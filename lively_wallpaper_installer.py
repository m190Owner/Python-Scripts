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

# Check if Git, pip, and Python are already installed
git_installed = shutil.which("git") is not None
pip_installed = shutil.which("pip") is not None
python_installed = shutil.which("python") is not None

# Install Git, pip, and Python using winget if they are not already installed
if not git_installed:
    subprocess.call(["winget", "install", "git"])

if not pip_installed:
    subprocess.call(["winget", "install", "pip"])

if not python_installed:
    subprocess.call(["winget", "install", "python"])

# Check if lively wallpaper is already installed
lively_installed = shutil.which("lively-wallpaper") is not None

# Delete the existing lively wallpaper installation if it is already installed
if lively_installed:
    subprocess.call(["pip", "uninstall", "-y", "lively-wallpaper"])

# Clone the lively wallpaper repository from GitHub
subprocess.call(["git", "clone", "https://github.com/rocksdanister/lively"])

# Change the current working directory to the cloned repository
os.chdir("lively")

# Install the lively wallpaper using pip
subprocess.call(["pip", "install", "."])

# Use lively wallpaper to set the desktop background
subprocess.call(["lively-wallpaper"])
