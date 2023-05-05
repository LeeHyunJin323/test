import selenium

from selenium import webdriver
from selenium.webdriver import ActionChains

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
import time

URL = 'https://www.musinsa.com/categories/item/001005'

driver = webdriver.Chrome()
driver.get(URL)


time.sleep(2)

for i in range(1, 10):
    name = driver.find_elements(By.XPATH, "//*[@id='searchList']/li[{}]/div/div[2]/p[2]/a".format(i))
    if len(name) > 0:
        print(f"i: {i}, length of name: {len(name)}")
        print(name[0].text)

driver.close()


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time   #시간 지연 
# import urllib.request


# driver = webdriver.Chrome()
# driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
# elem = driver.find_element_by_name('q') #검색창을 찾음
# elem.send_keys("조코딩") #키보드 입력값
# elem.send_keys(Keys.RETURN)  #입력값 엔터

# SCROLL_PAUSE_TIME = 0.5

# # Get scroll height 
# last_height = driver.execute_script("return document.body.scrollHeight")

# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)

#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")   #[0].click() #클래스 0번째 이미지 클릭
# count = 1 # 이름 지정

# for image in images:
#     image.click()
#     time.sleep(3) #3초 ㄱㄷ
#     imgUrl = driver.find_element_by_css_selector(".r48jcc.pT0Scc.iPVvYb").get_attribute("src") #attri 이부분이 이미지src
#     urllib.request.urlretrieve(imgUrl, str(count) +".jpg") #이미지 다운로드
#     count = count +1
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()