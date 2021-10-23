"""
Instagram Comment Robot (Ver.1)
Created by MJ. Liu
2021/10/23
"""

from selenium.webdriver.support import expected_conditions as EC  #pip install selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import pickle
import random
browser = webdriver.Firefox(executable_path="geckodriver.exe")  #記得存在同個資料夾裡
random_comments=[
"我的愛😍",
"超！好！吃！",
"趕快收藏起來下次吃❤️"
"這個我想吃很久了😂",
"我今天才討論到這個😂",
"看了好爽啊❤️我也想要吃",
"最近一直被這個燒到欸😍",
"真的超推",
"拍得好美喔😍",
"心動了",
"這個很可以！",
"還不綽",
"看起來超讚！",
"❤️❤️❤️",
"超 級 推 薦",
"想吃😍😍😍",
"感覺不錯欸❤️",
"哇哇😍😍我要去買！",
"感覺豪好吃 😋😋",
"太誘人了😍😍😍",
"已收藏😍",
"感覺很好吃耶🤤"
]

# ------ 用cookie登入 ------
url = 'https://www.instagram.com/'  
browser.get(url) 
cookies = pickle.load(open("pickles/cookies.pkl", "rb"))
for cookie in cookies:
    browser.add_cookie(cookie)
browser.get(url)

# ------ 不開啟通知 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

# ------ 網頁元素定位 ------                                                                                                    
notification_click = browser.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')[0]

# ------ 點擊不開啟通知 ------
notification_click.click()

# ------ 前往個人首頁 ------
url_main_page = 'https://www.instagram.com/eateat_bao5252/'
browser.get(url_main_page)

# 取得貼文網址
# 用find_elements_by_class_name找到放貼文地方
post = browser.find_elements_by_class_name('v1Nh3') # 最新貼文都套用v1Nh3這class
hashtag_url_list = [] # 等等放網址
for i in post:
    # 在每個post找到標籤a後取得herf(網址)屬性
    post_url = i.find_element_by_tag_name('a').get_attribute('href') 
    hashtag_url_list.append(post_url) # 放入網址

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
    time.sleep(random.randint(2, 5))
    #Reference: https://github.com/redianmarku/instagram-comment-bot



