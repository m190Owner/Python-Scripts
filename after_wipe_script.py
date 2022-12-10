import os
import time
import winreg

# Prompt user to start script
start = input("Do you want to start the script? (y/n): ")
if start != "y":
    exit()

# Enable Hyper-V
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization", 0, winreg.KEY_WRITE)
winreg.SetValueEx(key, "MinVmVersionForCpuBasedVirt", 0, winreg.REG_SZ, "1.0")
winreg.SetValueEx(key, "HypervisorLaunchType", 0, winreg.REG_DWORD, 3)
winreg.CloseKey(key)

# Install YouTube Music
os.system('powershell (New-Object Net.WebClient).DownloadFile("https://github.com/th-ch/youtube-music/releases/download/v2.1.1/youtube-music-2.1.1.exe", "C:\YouTubeMusicSetup.exe")')
os.system('Start-Process C:\YouTubeMusicSetup.exe')

# Install Steam
os.system('powershell (New-Object Net.WebClient).DownloadFile("https://steamcdn-a.akamaihd.net/client/installer/SteamSetup.exe", "C:\SteamSetup.exe")')
os.system('C:\SteamSetup.exe')

# Install Discord
os.system('powershell (New-Object Net.WebClient).DownloadFile("https://discordapp.com/api/download?platform=win", "C:\DiscordSetup.exe")')
os.system('C:\DiscordSetup.exe')

# Install Brave browser
os.system('powershell (New-Object Net.WebClient).DownloadFile("https://laptop-updates.brave.com/latest/winx64", "C:\BraveSetup.exe")')
os.system('C:\BraveSetup.exe')

# Ask user to restart
print("Installation complete. Please restart your system for the changes to take effect.")

# Wait 5 seconds before closing
time.sleep(5)
