## 링크드인 자동지원 봇 만들기

# 함수호출
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

email = ''
password = 'test'

path = '/Users/sky/Python/chromedriver'
driver = webdriver.Chrome(path)
driver.get('https://www.linkedin.com/jobs/search?keywords=Data%20Analyst&location=미국&locationId=&geoId=103644278&f_TPR=&f_E=1%2C2&position=1&pageNum=0')

# 로그인
sign_in_btn = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in_btn.click()

# 대기시간 설정
time.sleep(5)

email_field = driver.find_element(By.ID, 'username')
email_field.send_keys(email)
password_field = driver.find_element(By.ID, 'password')
password_field.send_keys(password)

# 엔터
password_field.send_keys(Keys.ENTER)




