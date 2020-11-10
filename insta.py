#https://note.com/instagram___/n/nfd84e83f5ed6

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

def login():
	driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
	f = open('insta.txt','a')
	f.write("instagramにアクセスしました\n")
	f.close()
	time.sleep(1)

 #メアドと、パスワードを入力
	driver.find_element_by_name('username').send_keys('watashinagata')
	time.sleep(1)
	driver.find_element_by_name('password').send_keys('19960923')
	time.sleep(1)

 #ログインボタンを押す
	driver.find_element_by_class_name('L3NKy       ').click()
	time.sleep(random.randint(2, 5))
	f = open('insta.txt','a')
	f.write("instagramにログインしました\n")
	f.close()
	time.sleep(1)

def tagsearch(tag):
	instaurl = 'https://www.instagram.com/explore/tags/'
	driver.get(instaurl + tag)
	time.sleep(random.randint(2, 10))
	f = open('insta.txt','a')
	f.write("listtagより、tagで検索を行いました\n")
	f.close()
	time.sleep(1)

def clicknice():
	target = driver.find_elements_by_class_name('_9AhH0')[10]
	actions = ActionChains(driver)
	actions.move_to_element(target)
	actions.perform()
	f = open('insta.txt','a')
	f.write("最新の投稿まで画面を移動しました\n")
	f.close()
	time.sleep(random.randint(1, 20))

	try:
		driver.find_elements_by_class_name('_9AhH0')[9].click()
		time.sleep(random.randint(2, 10))
		f = open('insta.txt','a')
		f.write("投稿をクリックしました\n")
		f.close()
		time.sleep(1)
		driver.find_element_by_class_name('fr66n').click()
		f = open('insta.txt','a')
		f.write("投稿をいいねしました\n")
		f.close()
		time.sleep(1)

	except WebDriverException:
		f = open('insta.txt','a')
		f.write("エラーが発生しました\n")
		f.close()
		return

	for i in range(random.randint(3, 5)):
		try:
			driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click()
			f = open('insta.txt','a')
			f.write("次の投稿へ移動しました\n")
			f.close()
			time.sleep(random.randint(random.randint(2, 5), random.randint(10, 15)))

		except WebDriverException:
			f = open('insta.txt','a')
			f.write("２つ目の位置でエラーが発生しました\n")
			f.close()
			time.sleep(5)

		try:
			driver.find_element_by_class_name('fr66n').click()
			f = open('insta.txt','a')
			f.write("投稿をいいねしました\n")
			f.close()
			time.sleep(2)
		except WebDriverException:
			f = open('insta.txt','a')
			f.write("3acつ目の位置でエラーが発生しました\n")
			f.close()

if __name__ == '__main__':

	taglist = ['f4f', 'l4l','like4like', 'instagood','followme', 'follow', 'いいね返し']

	driver_path = ChromeDriverManager(path='.').install()
	options = Options()
	options.add_argument('--headless')

	while True:
		driver = webdriver.Chrome(driver_path, options=options)

		time.sleep(1)
		login()

		tagsearch(random.choice(taglist))
		clicknice()

		driver.close()

		abc = random.randint(random.randint(20, 100), random.randint(120, 1800))
		f = open('insta.txt','a')
		f.write(str(abc)+"秒待機します\n")
		f.close()
		time.sleep(abc)