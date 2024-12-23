from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

proxy_ip_port = '62.164.255.151:49178'
proxy_username = '5KFr01yS823ZxMd'
proxy_password = 'cDIeYuzHd9ip9ZC'

chrome_options = Options()
chrome_options.add_argument(f"--proxy-server={proxy_ip_port}")

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get('https://whatismyipaddress.com')
sleep(500)

driver.quit()
