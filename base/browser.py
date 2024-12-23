from seleniumwire import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile
from time import sleep
class Browser:
    def __init__(self,account = 'hung'):
        self.account = account
        if account != 'hung':
            self.profile_dir = tempfile.mkdtemp(prefix=f"account_{account}_")
        
    def start(self):
        chrome_options = Options()
        if self.account != 'hung':
            chrome_options.add_argument(f"--user-data-dir={self.profile_dir}")
        chrome_options.add_argument("--disable-notifications") 
        chrome_options.add_argument("--disable-geolocation")
        chrome_options.add_argument('--ignore-certificate-errors')
        chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        service = Service('chromedriver.exe') 
        # browser = webdriver.Chrome(service=service,options=chrome_options)
        
        proxy_username = '5KFr01yS823ZxMd'
        proxy_password = 'cDIeYuzHd9ip9ZC'
        proxy = "62.164.255.151:49178"

        sw_options = {
            'proxy': {
                'http': f'http://{proxy_username}:{proxy_password}@{proxy}',
                'https': f'https://{proxy_username}:{proxy_password}@{proxy}',
            }
        }
        
        driver = webdriver.Chrome(service=service,options=chrome_options,seleniumwire_options=sw_options)

        return driver
        # return browser
    
    def cleanup(self):
        """Xóa thư mục tạm nếu được tạo."""
        if self.profile_dir:
            import shutil
            shutil.rmtree(self.profile_dir, ignore_errors=True)