from selenium import webdriver
import time
import csv
from selenium.webdriver.common.keys import Keys


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')
# driver = webdriver.Firefox(firefox_profile=firefox_profile)
driver_new = webdriver.Firefox(firefox_profile=firefox_profile)
# driver.get("https://www.inshorts.com/en/read")

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
def get_from_livemint(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        try:
            driver_new.find_element_by_class_name('btn_disagree').click()
        except:
            print('hmm')
        text = driver_new.find_element_by_class_name('mainArea').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
        l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')# print(text)

def get_from_timesnow(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('artical-description').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))


        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_hindustantimes(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        time.sleep(5)
        try:
            driver_new.find_element_by_class_name('btn_disagree').click()
        except:
            print('hmm')
        text = driver_new.find_element_by_class_name('story-details').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            if(i!=(len(text)-1) and i!=(len(text)-2)):
                print(text[i].get_attribute('textContent'))
                l.append(text[i].get_attribute('textContent'))
        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_newindianexpress(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_id('storyContent').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))


        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_guardian(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('content__standfirst').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))


        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_crictracker(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('meta-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            if(i!=(len(text)-1)):
                print(text[i].get_attribute('textContent'))
                l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_indiacom(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('articleBody').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_dailymail(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_xpath('//*[@itemprop="articleBody"]').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_thenewsminute(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_xpath('//*[@itemprop="articleBody"]').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_ani(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_xpath('//*[@itemprop="articleBody"]').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_quint(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('story-article__cards').find_elements_by_css_selector('.story-article__content__element--text p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_bloombergquint(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('paywall').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_inc42(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('entry-content').find_elements_by_class_name('selectionShareable')
        l = []
        for i in range(len(text)):
            if(text[i].get_attribute('textContent').find("Related Article:") == -1):
                print(text[i].get_attribute('textContent'))
                l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')

def get_from_reuters(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('StandardArticleBody_body').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))
        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_financialexpress(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('leftstory').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_rt(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('article__text').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_freepressjournal(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('story-element-text').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_thewire(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('postComplete__description').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            if(text[i].get_attribute('textContent').find("Also read:") == -1):
                print(text[i].get_attribute('textContent'))
                l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')

def get_from_engadget(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_id('page_body').find_elements_by_css_selector('.article-text p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_vogueindia(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('description').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_entrackr(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_xpath('//*[@data-widget_type="theme-post-content.default"]').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_pti(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_elements_by_class_name('fulstorytext')
        l = []
        for i in range(len(text)):
            print(text[i].get_attribute('textContent'))
            l.append(text[i].get_attribute('textContent'))

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_bollywoodhungama(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('entry-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_pinkvilla(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_id('ct1').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_cricketcountry(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('cc-main-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_whitehouse(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('page-content__content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_yourstory(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('quill-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_cricketaustralia(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('news-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_ftc(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('field-item').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_delhiplanet(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('story-detail').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_phys(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('article-main').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_pri(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('node-story').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_bgr(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('article-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_pnas(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('pane-highwire-panel-tabs-container').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_purdue(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('maincontent').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
def get_from_techcircle(link,index,news_title,news_summary,source_name):
    try:
        driver_new.get(link)
        text = driver_new.find_element_by_class_name('article-content').find_elements_by_css_selector('p')
        l = []
        for i in range(len(text)):
            print(text[i].text)
            l.append(text[i].text)

        article = ''.join(l)
        add_to_csv(index,news_title,news_summary,source_name,article,link)
    except:
        print('umm')
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


def others():
    print('Null')

def get_from_source(link,index,news_title,news_summary,link_name):
    print(link)
    print(link_name)
    if(link_name=='TechCrunch' or link_name=='Tech Crunch'):
        get_from_techCrunch(link,index,news_title,news_summary,link_name)
    elif(link_name=='Livemint'):
        get_from_livemint(link,index,news_title,news_summary,link_name)
    elif(link_name=='FTC'):
        get_from_ftc(link,index,news_title,news_summary,link_name)
    elif(link_name=='Delhi Planet'):
        get_from_delhiplanet(link,index,news_title,news_summary,link_name)
    elif(link_name=='Phys.org'):
        get_from_phys(link,index,news_title,news_summary,link_name)
    elif(link_name=='PRI'):
        get_from_pri(link,index,news_title,news_summary,link_name)
    elif(link_name=='BGR' or link_name=='BGR India'):
        get_from_bgr(link,index,news_title,news_summary,link_name)
    elif(link_name=='PNAS'):
        get_from_pnas(link,index,news_title,news_summary,link_name)
    elif(link_name=='TechCircle'):
        get_from_techcircle(link,index,news_title,news_summary,link_name)
    elif(link_name=='Purdue University'):
        get_from_purdue(link,index,news_title,news_summary,link_name)
    elif(link_name=='Times Now'):
        get_from_timesnow(link,index,news_title,news_summary,link_name)
    elif(link_name=='Hindustan Times'):
        get_from_hindustantimes(link,index,news_title,news_summary,link_name)
    elif(link_name=='The New Indian Express'):
        get_from_newindianexpress(link,index,news_title,news_summary,link_name)
    elif(link_name=='The Guardian'):
        get_from_guardian(link,index,news_title,news_summary,link_name)
    elif(link_name=='CricTracker'):
        get_from_crictracker(link,index,news_title,news_summary,link_name)
    elif(link_name=='India.com'):
        get_from_indiacom(link,index,news_title,news_summary,link_name)
    elif(link_name=='Daily Mail'):
        get_from_dailymail(link,index,news_title,news_summary,link_name)
    elif(link_name=='The News Minute'):
        get_from_thenewsminute(link,index,news_title,news_summary,link_name)
    elif(link_name=='ANI' or link_name=='ANI News'):
        if link.find("twitter.com") == -1:
            get_from_ani(link,index,news_title,news_summary,link_name)
        else:
            others()
    elif(link_name=='The Quint'):
        get_from_quint(link,index,news_title,news_summary,link_name)
    elif(link_name=='Bloomberg Quint' or link_name=='BloombergQuint'):
        get_from_bloombergquint(link,index,news_title,news_summary,link_name)
    elif(link_name=='Inc42'):
        get_from_inc42(link,index,news_title,news_summary,link_name)
    elif(link_name=='Reuters'):
        get_from_reuters(link,index,news_title,news_summary,link_name)
    elif(link_name=='The Financial Express' or link_name=='Financial Express'):
        get_from_financialexpress(link,index,news_title,news_summary,link_name)
    elif(link_name=='RT'):
        get_from_rt(link,index,news_title,news_summary,link_name)
    elif(link_name=='Free Press Journal' or link_name=='The Free Press Journal'):
        get_from_freepressjournal(link,index,news_title,news_summary,link_name)
    elif(link_name=='The Wire'):
        get_from_thewire(link,index,news_title,news_summary,link_name)
    elif(link_name=='Engadget'):
        get_from_engadget(link,index,news_title,news_summary,link_name)
    elif(link_name=='Vogue India'):
        get_from_vogueindia(link,index,news_title,news_summary,link_name)
    elif(link_name=='Entrackr'):
        get_from_entrackr(link,index,news_title,news_summary,link_name)
    elif(link_name=='SpotboyE' or link_name=='SpotBoyE'):
        get_from_spotboye(link,index,news_title,news_summary,link_name)
    elif(link_name=='PTI'):
        get_from_pti(link,index,news_title,news_summary,link_name)
    elif(link_name=='Bollywood Hungama'):
        get_from_bollywoodhungama(link,index,news_title,news_summary,link_name)
    elif(link_name=='Pinkvilla'):
        get_from_pinkvilla(link,index,news_title,news_summary,link_name)
    elif(link_name=='Cricket Country'):
        get_from_cricketcountry(link,index,news_title,news_summary,link_name)
    elif(link_name=='The White House'):
        get_from_whitehouse(link,index,news_title,news_summary,link_name)
    elif(link_name=='YourStory'):
        get_from_yourstory(link,index,news_title,news_summary,link_name)
    elif(link_name=='Cricket Australia'):
        get_from_cricketaustralia(link,index,news_title,news_summary,link_name)
    else:
        others()


def get_from_inshots():
    button_click(1000,10)
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
    with open('documentsummaries.csv', 'r') as f:
          reader = csv.reader(f,delimiter=',')
          your_list = list(reader)
          for i in range(len(your_list)):
              get_from_source(your_list[i][4],your_list[i][0],your_list[i][1],your_list[i][2],your_list[i][3])
    # print(your_list)


get_from_csv()
# get_from_inshots()
# get_from_livemint('.')
# sumTitle = driver.find_elements_by_xpath('//*[@itemprop="headline"]')
# sumArticle = driver.find_elements_by_xpath(
#     '//*[@itemprop="articleBody"]')
# articleLink = driver.find_elements_by_xpath(
#     "//div[@class='read-more']//a[@class='source']")
# print(links.find_element_by_xpath('//div[@class="result results_links_deep highlight_d result--url-above-snippet"]'))

# try:
#     print(i)
#     print(sumTitle[i].text)
#     print(sumArticle[i].text)
#     print(articleLink[i].get_attribute('href'))
# except:
#     print('none')

# find_element_by_xpath('//div[@class="result results_links_deep highlight_d result--url-above-snippet"]')
