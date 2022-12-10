# Import the necessary modules
import os
import subprocess

# Set the URL of the repository
repo_url = "https://github.com/th-ch/youtube-music"

# Check if Git is installed
try:
    subprocess.run(["git", "--version"], check=True)
except subprocess.CalledProcessError:
    # Git is not installed, so install it
    subprocess.run(["winget", "install", "git"])

# Clone the repository
subprocess.run(["git", "clone", repo_url])

# Change the current working directory to the repository
os.chdir("youtube-music")

# Install the project
subprocess.run(["pip", "install", "."])
