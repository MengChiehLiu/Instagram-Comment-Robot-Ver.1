"""
Instagram Comment Robot (Ver.1)
Created by MJ. Liu
2021/10/23
"""
#執行完後資料夾中會新增cookies.pkl檔，用來記錄登入資訊。

from selenium.webdriver.support import expected_conditions as EC  #pip install selenium
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import pickle

# ------ 取得網頁資訊 ------
browser = webdriver.Chrome(executable_path="geckodriver.exe")  #使用firefox瀏覽器，記得存在同個資料夾裡
url = 'https://www.instagram.com/'  
browser.get(url) 

# ------ 填入帳號與密碼 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.NAME, 'username')))

# ------ 網頁元素定位 ------
username_input = browser.find_elements_by_name('username')[0]
password_input = browser.find_elements_by_name('password')[0]

# ------ 輸入帳號密碼 ------
username_input.send_keys("account")   #你的IG帳號
password_input.send_keys("password")   #你的IG密碼

# ------ 登入 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[3]/button/div')))

# ------ 網頁元素定位 ------
login_click = browser.find_elements_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')[0]

# ------ 點擊登入鍵 ------
login_click.click()

# ------ 不儲存登入資料 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

# ------網頁元素定位 ------
store_click = browser.find_elements_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')[0]

# ------ 點擊不儲存鍵 ------
store_click.click()

# ------ 不開啟通知 ------
WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))

# ------ 網頁元素定位 ------                                                                                                    
notification_click = browser.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')[0]

# ------ 點擊不開啟通知 ------
notification_click.click()

# ------ 儲存登入資料 ------
pickle.dump(browser.get_cookies(), open("cookies.pkl","wb"))
