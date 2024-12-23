from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile

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
        chrome_options.add_argument("--use-fake-ui-for-media-stream")
        chrome_options.add_argument("--disable-popup-blocking") 
        chrome_options.add_argument("--incognito")

        service = Service('chromedriver.exe') 
        browser = webdriver.Chrome(service=service,options=chrome_options)
        
        return browser
    
    def cleanup(self):
        """Xóa thư mục tạm nếu được tạo."""
        if self.profile_dir:
            import shutil
            shutil.rmtree(self.profile_dir, ignore_errors=True)