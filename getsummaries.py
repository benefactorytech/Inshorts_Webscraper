from selenium import webdriver
import time
import csv


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver.get("https://www.inshorts.com/en/read")

def button_click(number,time):
    for i in range(number):
        try:
            Button = driver.find_element_by_id('load-more-btn')
            Button.click()
            print(i)
            time.sleep(10)
        except:
            continue
def add_to_csv(index,news_title,news_summary,source_name,link):
    with open('documentsummaries.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow([index,news_title,news_summary,source_name,link])

def get_from_inshots():
    button_click(10000,10)
    news = driver.find_elements_by_class_name('news-card')
    news_list=[]
    for i in range(len(news)):
        print(i)
        news_summary_title = news[i].find_element_by_class_name('news-card-title').find_element_by_css_selector('a').text
        print(news_summary_title)
        news_summary = news[i].find_element_by_class_name('news-card-content').text
        print(news_summary)
        try:
            news_source = news[i].find_element_by_class_name('news-card-footer').find_element_by_css_selector('.read-more a')
            add_to_csv(i,news_summary_title,news_summary,news_source.text,news_source.get_attribute('href'))
            news_list.append([i,news_summary_title,news_summary,news_source.text,news_source.get_attribute('href')])
        except:
            print('Null')
    print(news_list)
    driver.quit()

get_from_inshots()
