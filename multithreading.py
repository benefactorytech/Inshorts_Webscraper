from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys
import threading
import datetime

exitFlag = 0


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver_new = webdriver.Firefox(firefox_profile=firefox_profile)



class myThread (threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print("\nStarting " + self.name)
        # Acquire lock to synchronize thread
        threadLock.acquire()
        print_date(self.name, self.counter)
        # Release lock for the next thread
        threadLock.release()
        print("Exiting " + self.name)

def print_date(threadName, counter):
    datefields = []
    timestamp = 1545730073
    today = datetime.datetime.fromtimestamp(timestamp)
    datefields.append(today)
    print("{}[{}]: {}".format( threadName, counter, datefields[0] ))


def button_click(number,time):
    for i in range(number):
        try:
            Button = driver.find_element_by_id('load-more-btn')
            Button.click()
            print(i)
            time.sleep(time)
        except:
            continue
def add_to_csv(index,news_title,news_summary,source_name,news_article,link):
    with open('document.csv','a') as fd:
        writer = csv.writer(fd)
        writer.writerow([index,news_title,news_summary,source_name,news_article,link])

# ==Thread1 for article source 1 begins

def get_from_techCrunch(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        # driver_new.find_element_by_class_name('exit-close').click()
        text = driver_new.find_element_by_class_name('article-content').find_elements_by_css_selector('p')
        l=[]
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))


        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')

# ==Thread1 for article source 1 ends

# ==Thread2 for article source 2 begins

def get_from_spotboye(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_elements_by_id('mvp-content-main')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')

# ==Thread2 for article source 2 ends

threadLock = threading.Lock()
threads = []

# Create new threads
thread1 = myThread("Thread", 1)
thread2 = myThread("Thread", 2)

# Start new Threads
thread1.start()
thread2.start()

# Add threads to thread list
threads.append(thread1)
threads.append(thread2)

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("\nExiting the Program!!!")



def get_from_inshots():
    button_click(10000,10)
    news = driver.find_elements_by_class_name('news-card')
    for i in range(len(news)):
        print(i)
        news_summary_title = news[i].find_element_by_class_name('news-card-title').find_element_by_css_selector('a').text
        print(news_summary_title)
        news_summary = news[i].find_element_by_class_name('news-card-content').text
        print(news_summary)
        try:
            news_source = news[i].find_element_by_class_name('news-card-footer').find_element_by_css_selector('.read-more a')
            get_from_source(news_source,i,news_summary_title,news_summary)
        except:
            print('Null')
    driver.quit()
    driver_new.quit()


def get_from_csv():
    with open('multithreading.csv', 'r',errors='ignore') as f:
          reader = csv.reader(f,delimiter=',')
          your_list = list(reader)
          for i in range(len(your_list)):
            try:
                get_from_source(your_list[i][4],your_list[i][0],your_list[i][1],your_list[i][2],your_list[i][3])
            except:
                print(your_list[i])
            

            # print(your_list[i])
            # print("-"*70)
    # print(your_list)


get_from_csv()