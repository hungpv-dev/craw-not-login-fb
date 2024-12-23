from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import tempfile

class Browser:
    def __init__(self,account = 'hung'):
        self.account = account
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
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)

        service = Service('chromedriver.exe') 
        browser = webdriver.Chrome(service=service,options=chrome_options)
        
        # Che giấu thuộc tính `webdriver`
        browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            'source': '''
                Object.defineProperty(navigator, 'webdriver', {
                    get: () => undefined
                });
            '''
        })
        
        return browser
    
    def cleanup(self):
        """Xóa thư mục tạm nếu được tạo."""
        if self.profile_dir:
            import shutil
            shutil.rmtree(self.profile_dir, ignore_errors=True)