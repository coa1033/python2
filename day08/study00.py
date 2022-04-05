#매크로
#find_element_by_id => id 속성을  사용하여 접근
#find_element_by_name => name 속성을 사용하여 접근
#find_element_by_xpath => xpath 속성을 사용하여 접근
#find_element_by_link_text => 앵커태그(a태그)에 사용되는 텍스트로 접근
#find_element_by_partial_link_text => 앵커태그(a태그)에 사용되는 일부 텍스트로 접근
#find_element_by_tag_name => 태그를 사용해서 접근
#find_element_by_class_name => 클래스를 사용해서 접근
#find_element_by_css_selector =>css선택자를 사용하여 접근

import selenium
from selenium import webdriver
import time

chorme_path = 'C:\\Users\\Administrator\\Desktop\\py2\\chromedriver.exe'
url = 'https://codepen.io/'

browser = webdriver.Chrome(chorme_path)
id = 'lgp920024@gmail.com'
pw = '!!!!!!!!!!!!'

browser.get(url)
time.sleep(3)
browser.find_element_by_xpath('//*[@id="react-page"]/div[1]/a[2]').click()
time.sleep(2)
browser.find_element_by_css_selector('#login-email-field').send_keys(id)
time.sleep(2)
browser.find_element_by_css_selector('#login-password-field').send_keys(pw)
time.sleep(2)
browser.find_element_by_xpath('//*[@id="log-in-button"]').click()



