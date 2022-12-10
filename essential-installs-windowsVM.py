# check if Discord is already installed
if [ ! -d "~/AppData/Local/Discord" ]; then
  # download and install Discord
  wget https://discordapp.com/api/download?platform=win
  mv download?platform=win discord-installer.exe
  ./discord-installer.exe
else
  # update Discord
  cd ~/AppData/Local/Discord
  git pull origin master
fi

# check if Brave is already installed
if [ ! -d "~/AppData/Local/BraveSoftware" ]; then
  # download and install Brave
  wget https://laptop-updates.brave.com/latest/winx64
  mv latest/winx64 brave-installer.exe
  ./brave-installer.exe
else
  # update Brave
  cd ~/AppData/Local/BraveSoftware
  git pull origin master
fi

# check if Windows Terminal is already installed
if [ ! -d "~/AppData/Local/Microsoft/Windows/Terminal" ]; then
  # download and install Windows Terminal
  wget https://github.com/microsoft/terminal/releases/download/v0.10/Microsoft.WindowsTerminal.Installer.appx
  mv Microsoft.WindowsTerminal.Installer.appx windows-terminal-installer.exe
  ./windows-terminal-installer.exe
else
  # update Windows Terminal
  cd ~/AppData/Local/Microsoft/Windows/Terminal
  git pull origin master
fi
