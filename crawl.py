import signal
import multiprocessing
import os
import shutil
from selenium.common.exceptions import WebDriverException
from base.browser import Browser
from facebook.crawlid import CrawlId
from time import sleep
from helpers.inp import get_user_input


def process_crawl():
    browser = None
    browserStart = None
    try:
        browserStart = Browser()
        browser = browserStart.start()
        browser.get("https://facebook.com")
        crawl = CrawlId(browser)
        crawl.handle()
        
    except Exception as e:
        print(f"Lỗi trong Crawl: {e}")
    finally:
        if browser:
            browser.quit()
        if browserStart and os.path.exists(browserStart.profile_dir):
            shutil.rmtree(browserStart.profile_dir)

if __name__ == "__main__":
    try:
        countGet = get_user_input()
        processes = []
        for count in range(countGet):
            crawl_process = multiprocessing.Process(target=process_crawl)
            processes.extend([crawl_process])  
            crawl_process.start()

        for process in processes:
            process.join()

        print("Tất cả các tài khoản đã được xử lý.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
