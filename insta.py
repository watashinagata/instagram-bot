import sys
import os
sys.path.append('/usr/local/lib/python3.7/dist-packages')

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import urllib.parse
import time

#Webdriver
driver_path = ChromeDriverManager(path='/Users/nagatashoya/chromedriver').install()
browser = webdriver.Chrome(driver_path)
#browser = webdriver.Chrome('/mnt/c/workspace/pydev/chromedriver.exe')

BASE_URL      = 'https://www.instagram.com/'
LOGIN_URL      = BASE_URL + 'accounts/login/?source=auth_switchwer'
TAG_SEARCH_URL = BASE_URL + 'explore/tags/{}/'

#selectors
NO_LIKE_FLAG = "/html/body/div[4]/div[2]/div/article/div[]/section[1]/span[1]/button/svg[@aria-label='いいね！'']"

NOTICE_BUTTON = "//button[@class='aOOlW   HoLwm ']"
LIKE_BUTTON   = "/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button"
#LIKE_BUTTON   = "//button[@class='dCJp8 afkep _0mzm-']"


MEDIA_SELECTOR      = 'div._9AhH0'
NEXT_PAGER_SELECTOR = 'a.coreSpriteRightPaginationArrow'

#USER INFO
username = 'id'
password = 'password'

#params
tagName = 'followmeto'
likedCounter = 0
likedMax = 100 # likeのMAX値

if __name__ == '__main__':

    # ログイン画面にアクセス
    browser.get(LOGIN_URL)
    time.sleep(3)

    # ログイン情報を入力してログイン
    usernameField = browser.find_element_by_name('username')
    usernameField.send_keys(username)
    passwordField = browser.find_element_by_name('password')
    passwordField.send_keys(password)
    passwordField.send_keys(Keys.RETURN)
    time.sleep(3)

    # 通知ボタンを押下
    browser.find_element_by_xpath(NOTICE_BUTTON).click()
    time.sleep(3)

    # 指定したハッシュタグを検索
    encodedTag = urllib.parse.quote(tagName)
    encodedURL = TAG_SEARCH_URL.format(encodedTag)
    print("encodedURL:{}".format(encodedURL))
    browser.get(encodedURL)
    time.sleep(3)

    # media click
    browser.implicitly_wait(15)
    browser.find_element_by_css_selector(MEDIA_SELECTOR).click()

    # 次へボタンが表示されないか、いいねがlikedMax分いくまでいいねし続ける
    while likedCounter < likedMax:
        time.sleep(15)
        try:
            #browser.find_element_by_xpath(NO_LIKE_FLAG)
            browser.find_element_by_xpath(LIKE_BUTTON).click()
            likedCounter += 1
            print("liked {}".format(likedCounter))
        except:
            #読み込まれなかったり既にいいねしているならパス
            print("pass")
            pass

        # 次へ
        try:
            browser.find_element_by_css_selector(NEXT_PAGER_SELECTOR).click()
        except:
            break
        print("You liked {} media".format(likedCounter))
