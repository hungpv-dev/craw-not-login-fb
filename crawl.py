import signal
import multiprocessing
import os
import shutil
from selenium.common.exceptions import WebDriverException
from base.browser import Browser
from facebook.crawlid import CrawlId
from facebook.crawl import Crawl
from time import sleep
from helpers.inp import get_user_input


def process_crawl():
    browser = None
    manager = None
    try:
        manager = Browser()
        browser = manager.start()
        browser.get("https://facebook.com")
        crawl = CrawlId(browser)
        crawl.handle()
        # page = {
        #     'id': 1,
        # }
        # his = {
        #     'id': '123',
        # }
        # post = {
        #     'id': 'pfbid02yfirs1pVz5SPBb7BMoxPdDTkTsxNBd6hVhNEFR3bE2ntSyYcAUwANaqGnGC9Vsn4l',
        #     'link': 'https://www.facebook.com/permalink.php?story_fbid=pfbid02yfirs1pVz5SPBb7BMoxPdDTkTsxNBd6hVhNEFR3bE2ntSyYcAUwANaqGnGC9Vsn4l&id=61558432464057'
        # }
        # browser.get(post['link'])
        # crawl = Crawl(browser)
        # crawl.crawlContentPost(page,post,his)
        
    except Exception as e:
        print(f"Lỗi trong Crawl: {e}")
    finally:
        if browser:
            browser.quit()
            manager.cleanup()

if __name__ == "__main__":
    try:
        countGet = get_user_input()
        processes = []
        for count in range(countGet):
            crawl_process = multiprocessing.Process(target=process_crawl)
            processes.extend([crawl_process])  
            crawl_process.start()
            sleep(2)

        for process in processes:
            process.join()

        print("Tất cả các tài khoản đã được xử lý.")
    except Exception as e:
        print(f"Lỗi không mong muốn: {e}")
