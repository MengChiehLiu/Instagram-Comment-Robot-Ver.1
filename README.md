# Instagram Comment Robot Ver.1

Instagram自動留言機器人，一次大約可對36篇貼文隨機留言。

第一次使用時先執行cookies.py，執行完後資料夾中會新增cookies.pkl檔，用來記錄登入資訊，第二次開始便可直接執行comment.py。


# 環境資訊:

python == 3.8.10

firefox == 93.0.0.7940 (使用Firefox瀏覽器可回覆表情符號)

geckodriver.exe == 94.0.4606.61


# 程式需更改處: 

cookies.py

(27行) username_input.send_keys("account")    #你的IG帳號

(28行) password_input.send_keys("password")   #你的IG密碼

comment.py

(17行) random_comments=["留言1","留言2",...] #放入留言

(33行) url_main_page = 'https://www.instagram.com/XXXXXXXXX/'   #目標網址(個人首頁)

# 其他

可自行加入按讚功能，請參考: https://github.com/MengChiehLiu/Instagram-Like-Robot-Ver.1
