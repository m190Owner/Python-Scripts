import steam
import discord
import getpass

def login_to_steam(username, password):
    steam_client = steam.Client()
    steam_client.login(username=username, password=password)
    return steam_client

def send_discord_webhook(webhook_url, steam_client):
    user_info = steam_client.get_user_info()
    discord_client = discord.Client()
    discord_client.send_message(webhook_url, user_info)

username = input("Enter your Steam username: ")
password = getpass.getpass("Enter your Steam password: ")

webhook_url = input("Enter the Discord webhook URL: ")

steam_client = login_to_steam(username, password)
send_discord_webhook(webhook_url, steam_client)