from selenium import webdriver
import time
from collections import Counter


firefox_profile = webdriver.FirefoxProfile()
adblockfile = r'/home/b1nary/Documents/scraping/src/adblock_plus-2.9.1-an+fx+sm+tb.xpi'
firefox_profile.add_extension (adblockfile)
firefox_profile.set_preference("extensions.adblockplus.currentVersion", "2.9")
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver= webdriver.Firefox(firefox_profile=firefox_profile)
driver.get("https://www.inshorts.com/en/read")

def button_click(number,time):
    for i in range(number):
        try:
            Button = driver.find_element_by_id('load-more-btn')
            Button.click()
            print(i)
            time.sleep(time)
        except:
            continue


def get_from_inshots():
    button_click(0,10)
    news = driver.find_elements_by_class_name('news-card')
    sources = []
    for i in range(len(news)):
        try:
            news_source = news[i].find_element_by_class_name('news-card-footer').find_element_by_css_selector('.read-more a')
            sources.append(news_source.text)
        except:
            print('Null')
    driver.close()
    counts = Counter(sources)
    print(counts)

get_from_inshots()
