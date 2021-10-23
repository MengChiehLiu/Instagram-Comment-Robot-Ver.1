"""
Instagram Comment Robot (Ver.1)
Created by MJ. Liu
2021/10/23
"""
#先執行cookies.py後再執行此程式。

from selenium.webdriver.support import expected_conditions as EC  #pip install selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pickle
import random
browser = webdriver.Firefox(executable_path="geckodriver.exe")  #使用firefox瀏覽器，記得存在同個資料夾裡
random_comments=[] #放入留言

# ------ 用cookie登入 ------
url = 'https://www.instagram.com/'  
browser.get(url) 
cookies = pickle.load(open("pickles/cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get(url)

# ------ 不開啟通知 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))                                                                                              
notification_click = browser.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')[0]
notification_click.click()

# ------ 前往個人首頁 ------
url_main_page = 'https://www.instagram.com/eateat_bao5252/'
browser.get(url_main_page)

# ------ 取得貼文網址 ------ 
post = browser.find_elements_by_class_name('v1Nh3')
hashtag_url_list = []
for i in post:
    post_url = i.find_element_by_tag_name('a').get_attribute('href') 
    hashtag_url_list.append(post_url)

for url in hashtag_url_list:
    browser.get(url)
    # ------ Find Textarea ------ 
    find_comment_box = (By.XPATH, '/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
    WebDriverWait(browser, 30).until(EC.presence_of_element_located(find_comment_box))
    comment_box = browser.find_element(*find_comment_box)
    WebDriverWait(browser, 30).until(EC.element_to_be_clickable(find_comment_box))
    comment_box.click()
    time.sleep(1)
    comment_box = browser.find_element(*find_comment_box)
    comment_box.send_keys(random.choice(random_comments))

    # ------ Press Button ------ 
    browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]").click()
    time.sleep(random.randint(2, 4))  #2~5秒後進入下一篇貼文
    #Reference: https://github.com/redianmarku/instagram-comment-bot

