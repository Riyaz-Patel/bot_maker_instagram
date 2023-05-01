#IMPORTS

import sys, os, random, requests, time, pyperclip
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent

import requests
import time
from stem import Signal
from stem.control import Controller

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import subprocess
import requests
import psutil
from stem import Signal
from stem.control import Controller
from multiprocessing import Pool
from stem import Signal
from stem.control import Controller

import undetected_chromedriver as uc

#print(webdriver.Chrome().capabilities['chrome']['chromedriverVersion'])

# color

class color:
    PURPLE = '\033[95m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    CWHITE = '\33[37m'




# Fake useragent

# ua = UserAgent()
# userAgent = ua.random

# options.add_argument(f'user-agent={userAgent}')

# Headless mode (set as true to use)


# Don't close the browser
# options.add_experimental_option("detach", True)

# Proxy (highly required)
# attention demarrer tor avant : dossier C:\Users\patel\Desktop\Tor Browser\Browser\TorBrowser\Tor
# entrer cmd dans la barre d'adresse puis entrer "tor" dans l'invite de commande

#####################################################################
# Pour installer tor service                                        #
# cd C:\Users\patel\Desktop\Tor Browser\Browser\TorBrowser\Tor      #
# tor --service install                                             #
# tor --service start                                               #
# tor --service stop                                                #
# installer privoxy en tant que service                             #
#####################################################################

# import subprocess
# return_code = subprocess.call(["C:/Users/patel/Desktop/Tor Browser/Browser/TorBrowser/Tor/tor.exe"])
#
# if return_code == 0:
#     print("Success!")
# else:
#     print("Error!")

#ouvrir tor.exe
#
# result = subprocess.Popen(["tor"], shell=True, cwd="C:/Users/patel/Desktop/Tor Browser/Browser/TorBrowser/Tor")
# time.sleep(8)
#
# # riyazrog = 16:B7C7A90BD9E********************************
# #
# # 16:A5049A961A5********************************
# # 16:BE08C7BC9E8********************************
# # parametres et test du proxy / si proxies=proxy ne foncionne pas alors tor est bien fermé
# #proxy = {}     #désactive le proxy
#
# proxy ={'http':'socks5h://127.0.0.1:9050',
#     'https':'socks5h://127.0.0.1:9050'}
#
# res = requests.get('http://ip-api.com/json/',proxies=proxy)
# print(res.content)
#
# # quitter tor
# def kill_task(process_name):
#     for process in psutil.process_iter():
#         if process.name() == process_name:
#             process.kill()
#             print(f'Process {process_name} killed')
#
# kill_task('tor.exe')

###########################################################################################################
###########################################################################################################
###########################################################################################################
### Rotate IP
#
# def get_tor_session():
#     # initialize a requests Session
#     session = requests.Session()
#     # this requires a running Tor service in your machine and listening on port 9050 (by default)
#     session.proxies = {
#         "http": "socks5://127.0.0.1:9150",
#         "https": "socks5://127.0.0.1:9150",
#     }
#     return session
#
# def renew_connection():
#     with Controller.from_port(port=9051) as controller:
#         # welcome password should be generated in the machine,
#         # read the README file to know how to create it
#         controller.authenticate(password="riyaz")
#         controller.signal(Signal.NEWNYM)
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11"
# }
#
# def send_request(url_list):
#     for url in url_list:
#         try:
#             renew_connection()
#             session = get_tor_session()
#             html_content = session.get(url, headers=headers).text
#             print(url)
#             print(
#                 "IP rotated to:",
#                 session.get("https://ident.me", headers=headers).text,
#             )
#             # your html parsing code goes here
#             # html_content ....
#         except Exception as e:
#             print(e)
#             pass
#
#
# if __name__ == "__main__":
#     # IP address before IP rotation
#     print("Your Public IP:", requests.get("https://ident.me").text)
#
#     urls = [
#         "https://www.google.com",
#         "https://www.facebook.com",
#         "https://www.youtube.com",
#         "https://www.amazon.com",
#         "https://www.reddit.com",
#         "https://www.instagram.com",
#         "https://www.linkedin.com",
#         "https://www.wikipedia.org",
#         "https://www.twitter.com",
#     ] * 10
#
#     send_request(urls)

    # send requests in parallel using multiprocessing
    # with Pool(processes=20) as pool:
    #     pool.map(send_request, [urls[i : i + 10] for i in range(0, len(urls), 10)])
    #     pool.close()
    #     pool.join()

###########################################################################################################
############################################################################################################
###########################################################################################################
# driver = webdriver.Chrome('"C:/Users/patel/Desktop/chromedriver.exe"')
# driver.get("http://httpbin.org/ip")
# time.sleep(12)
# driver.quit()

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

prox.http_proxy = "http://127.0.0.1:9051"
prox.socks_proxy = "http://127.0.0.1:9051"
prox.ssl_proxy = "http://127.0.0.1:9051"
prox.socks_version = 5

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities)

#chrome_options = Options()
#chrome_options.add_argument('--socks-version=5')
#chrome_options.add_argument('--proxy-server=socks5h://127.0.0.1:9050')
#driver = webdriver.Chrome(options=chrome_options)

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=socks5h://127.0.0.1:9051,')
options.add_argument('--socks-version=5')
options.add_argument('--proxy-server=http://127.0.0.1:9051')
options.add_argument('--proxy-server=https://127.0.0.1:9051')


driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.youtube.com/')

# replace 'your_absolute_path' with your chrome binary absolute path
#options.add_argument('proxy-server=127.0.0.1:9050')

driver = uc.Chrome(chrome_options=options)
# driver.get('https://whatismyipaddress.com')

# driver = webdriver.Chrome('C:/Users/patel/Desktop/chromedriver.exe', options=chrome_options, desired_capabilities=capabilities)
proxy = {'http':'socks5h://127.0.0.1:9051',
     'https':'socks5h://127.0.0.1:9051'}

res = requests.get('http://ip-api.com/json/',proxies=proxy)
print(res.content)

################################################################################################################

socks_proxy = "socks5h://127.0.0.1:9051"
http_proxy = "http://127.0.0.1:9051"
https_proxy = "https://127.0.0.1:9051"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=" + socks_proxy)
chrome_options.add_argument("--proxy-server=" + http_proxy)
chrome_options.add_argument("--proxy-server=" + https_proxy)
driver = webdriver.Chrome(chrome_options=chrome_options)

################################################################################################################
################################################################################################################
#CEST CA LE BON CODE

prox = Proxy()
prox.proxy_type = ProxyType.MANUAL

prox.http_proxy = "127.0.0.1:9051"
prox.socks_proxy = "127.0.0.1:9051"
prox.ssl_proxy = "127.0.0.1:9051"
prox.socks_version = 5

capabilities = webdriver.DesiredCapabilities.CHROME
prox.add_to_capabilities(capabilities) # Remove '#' to use proxy




# Fake useragent
options = Options()
# user agent
ua = UserAgent()
userAgent = ua.random

options.add_argument(f'user-agent={userAgent}')

#Headless mode (set as true to use)
options.headless = True

#Don't close the browser
options.add_experimental_option("detach", True)

CHROME_DIR = "C:/Users/patel/Desktop/chromedriver.exe"

browser = webdriver.Chrome(CHROME_DIR, options=options, desired_capabilities=capabilities)  #rajouter les options user agent


url = "https://www.instagram.com/accounts/emailsignup/"

#Open ig signup url

browser.get(url)

#COOKIES
try:
    cookie = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Uniquement autoriser les cookies essentiels']"))).click()
except:
    pass

################################################################################################################
################################################################################################################
#pour tester si le proxy fonctionne
#
# proxy_server_ip = "http://127.0.0.1"
# import os
# response = os.system("ping -c 1 " + proxy_server_ip)
# if response == 0:
#     print(proxy_server_ip, 'is up!')
# else:
#     print(proxy_server_ip, 'is down!')
#
# ################################################################################################################
# proxy_server_port ="9050"
# import socket
# try:
#     sock = socket.create_connection((proxy_server_ip, proxy_server_port), timeout=5)
#     print(proxy_server_ip + ':' + str(proxy_server_port) + ' is reachable')
#     sock.close()
# except socket.error as e:
#     print(proxy_server_ip + ':' + str(proxy_server_port) + ' is not reachable')
#
# ################################################################################################################
# import requests
# try:
#     proxies = {"http": proxy_server_ip + ":" + str(proxy_server_port), "https": proxy_server_ip + ":" + str(proxy_server_port)}
#     r = requests.get("http://example.com", proxies=proxies, timeout=5)
#     print(proxy_server_ip + ':' + str(proxy_server_port) + ' is reachable')
# except requests.exceptions.RequestException as e:
#     print(proxy_server_ip + ':' + str(proxy_server_port) + ' is not reachable')

################################################################################################################
################################################################################################################





####################################################################################################
####################################################################################################

# Open ig signup url

# url = "https://www.instagram.com/accounts/emailsignup/"
# browser.get(url)
# print()
# print( color.GREEN + "[+] " + color.CWHITE + "Using useragent as : " + userAgent)
# elements

time.sleep(3.517)
#email = browser.find_element(By.CSS_SELECTOR,
#                             'div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
email = browser.find_element("name", "emailOrPhone")
#fullname = browser.find_element(By.CSS_SELECTOR,
#                                'div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
fullname = browser.find_element("name", "fullName")

#username = browser.find_element(By.CSS_SELECTOR,
#                                'div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
username = browser.find_element("name", "username")

#Password = browser.find_element(By.CSS_SELECTOR,
#                                'div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
Password = browser.find_element("name", "password")


# Create temporary email
browser.execute_script("window.open('');")

browser.switch_to.window(browser.window_handles[1])

browser.get("https://mail.tm")
time.sleep(5.2)
# enlever agree disagree cookies
try:
agree_button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, "//button[@mode='primary']//span[text()='AGREE']"))).click()
except:
    pass

time.sleep(6)

#copy_button = browser.find_element(By.XPATH, """//*[@id="address"]""")
copy_button = browser.find_element("id", "DontUseWEBuseAPI")

copy_button.click()

generated_email = pyperclip.paste()

print()
print("Generated Email : " + generated_email)

browser.switch_to.window(browser.window_handles[0])

# Create Random username

time.sleep(0.500)


#\\\\\\\\\\\\\\\\\\\\\\\\\   créer le fichier usernames.txt
username_file = open(os.getcwd() + "/usernames.txt", "r")
lines = [line.rstrip() for line in username_file]

chose_random_username_list = random.sample(lines, k=1)

random_username_string = ''.join(chose_random_username_list)

random_username_number = str(random.randint(100000, 200000))

generated_random_username = random_username_string + random_username_number

print(color.GREEN + "[!] " + color.CWHITE + "Generated username = " + generated_random_username)

# Create random password to avoid detection (not really required)

time.sleep(0.500)

chose_random_password_list = random.sample(lines, k=1)

random_password_string = ''.join(chose_random_password_list)

random_password_number = str(random.randint(10000, 20000))

generated_random_password = random_password_string + random_password_number

print(color.GREEN + "[!] " + color.CWHITE + "Generated password = " + generated_random_password)

# Fields to use

my_email = generated_email
my_fullname = 'BOT KILLER'
my_username = generated_random_username
my_password = generated_random_password

# Fill the page

email.send_keys(my_email)
time.sleep(0.517)
fullname.send_keys(my_fullname)
time.sleep(0.312)
username.send_keys(my_username)
time.sleep(0.125)
Password.send_keys(generated_random_password)
time.sleep(2)

# SUBMIT
submit_button = browser.find_element(By.XPATH, "//button[text()='Suivant']")

submit_button.click()

time.sleep(5)

# elements next page

# birthday_month = browser.find_element(By.CSS_SELECTOR,
#                                       '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(1) > select > option:nth-child(9)')
#
# birthday_day = browser.find_element(By.CSS_SELECTOR,
#                                     '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(2) > select > option:nth-child(25)')
# birthday_year = browser.find_element(By.CSS_SELECTOR,
#                                      '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.DhRcB > div > div > span > span:nth-child(3) > select > option:nth-child(26)')
# birthday_next_button = browser.find_element(By.CSS_SELECTOR,
#                                             '#react-root > section > main > div > div > div:nth-child(1) > div > div.qF0y9.Igw0E.IwRSH.eGOV_._4EzTm.lC6p0.g6RW6 > button')
#
#

# Find the birthday date dropdown element MONTH
select_element = Select(browser.find_element(By.XPATH,"//select[starts-with(@title, 'Mois')]"))
# dropdown_select = Select(select_element)

# sélectionner l'option souhaitée en utilisant le texte visible MONTH
select_element.select_by_visible_text('janvier')

#DAY
select_element = Select(browser.find_element(By.XPATH,"//select[starts-with(@title, 'Jour')]"))
select_element.select_by_visible_text('13')

#YEAR
select_element = Select(browser.find_element(By.XPATH,"//select[starts-with(@title, 'Année')]"))
select_element.select_by_visible_text('1998')


# Fill the page


birthday_month.click()
time.sleep(0.120)
birthday_day.click()
time.sleep(0.114)
birthday_year.click()
time.sleep(2)
birthday_next_button.click()

submit_button_2 = browser.find_element(By.XPATH, "//button[text()='Suivant']")
submit_button_2.click()

# Display countdown

browser.switch_to.window(browser.window_handles[1])
print()
print(color.GREEN + "[!] " + color.CWHITE + "Waiting for otp ")

print(color.GREEN + "[!] " + color.CWHITE + "Opening mail box in 15 seconds")

for remaining in range(15, 0, -1):
    sys.stdout.write("\r")
    sys.stdout.write("{:2d} seconds remaining.".format(remaining))
    sys.stdout.flush()
    time.sleep(1)

sys.stdout.write("\rComplete!            \n")
browser.refresh()
time.sleep(2)

# otp page element

read_otp = browser.find_element(By.XPATH,
                                '//*[@id="__layout"]/div/div[2]/main/div/div[2]/ul/li/a/div/div[1]/div[2]/div[2]/div/div[1]').text

# Read otp from mail

# Save response to response.Text

with open("response.text", "w") as file:
    file.write(str(read_otp))

read_otp_file = open("response.text")

lines = read_otp_file.readlines()

for line in lines:
    my_otp = str(line[0:6])

print(color.GREEN + "[!] " + color.CWHITE + "OTP Recieved : " + my_otp)

# fill otp
print(my_otp)
type(my_otp)
my_otp_2= int(my_otp)
browser.switch_to.window(browser.window_handles[0])
time.sleep(1)
confirmation_code = browser.find_element(By.NAME,"email_confirmation_code")
confirmation_code.send_keys(my_otp_2)
time.sleep(2)
confirmation_code.send_keys(Keys.ENTER)

# Write generated account

print(color.GREEN + '[!] ' + color.CWHITE + 'Saving account info as account_generated.txt ')
print()

with open("account_generated.txt", "a+") as file:
    file.write("\n")
    file.write(my_email + " : " + my_password)

#browser.quit()

