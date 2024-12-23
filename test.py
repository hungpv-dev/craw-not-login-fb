from time import sleep
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Thiết lập proxy
proxy_ip_port = '62.164.255.151:49178'
proxy_username = '5KFr01yS823ZxMd'
proxy_password = 'cDIeYuzHd9ip9ZC'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = proxy_ip_port
proxy.http_proxy = f"http://{proxy_username}:{proxy_password}@{proxy_ip_port}"
proxy.https_proxy = f"https://{proxy_username}:{proxy_password}@{proxy_ip_port}"
proxy.ssl_proxy = proxy_ip_port

# Cấu hình options
chrome_options = Options()
chrome_options.proxy = proxy

# Cấu hình dịch vụ và khởi tạo WebDriver
service = Service('chromedriver.exe')  # Đảm bảo rằng đường dẫn tới chromedriver.exe đúng
driver = webdriver.Chrome(service=service, options=chrome_options)

# Truy cập trang web và in ra địa chỉ IP
driver.get('https://whatismyipaddress.com')
sleep(500)  # Chờ một chút để trang web tải xong

# Đóng trình duyệt
driver.quit()
