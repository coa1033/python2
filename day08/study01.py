#Keys.ENTER => Enter
#Keys.RETURN => 엔터
#Keys.ARROW_UP => 방향키 위쪽
#Keys.ARROW_DOWN => 방향키 아래쪽
#Keys.ARROW_LEFT => 방향키 왼쪽
#Keys.ARROW_RIGHT => 방향키 오른쪽
#Keys.BACK_SPACE => 지우기
#Keys.DELETE => 지우기(딜리트)
#Keys.CONTROL => Ctrl
#Keys.ALT => Alt
#Keys.SHIFT => Shift
#Keys.TAB => Tab
#Keys.PAGE_UP => 스크롤 업
#Keys.PAGE_DOWN => 스크롤다운
#Keys.F1~9 =>F1~9 까지


import selenium
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time

chorme_path = 'C:\\Users\\Administrator\\Desktop\\py2\\chromedriver.exe'
url = 'https://www.naver.com/'

browser = webdriver.Chrome(chorme_path)

browser.get(url)
time.sleep(3)
St ='서울 석촌호수'
browser.find_element_by_xpath('//*[@id="query"]').send_keys(St,Keys.ENTER)
time.sleep(2)

# window_handles[0]
# window_handles[-1]
# 예시 
# 맨처음 탭으로 이동
# browser.switch_to.window(window_handles[0])
# 새롭게 열린창,팝업,탭으로 전환
# browser.swith_to.window(window_handles[-1])

# 스크린샷(현재 켜져있는 클모 창의 화면 캡쳐 저장)
# browser.get_screenshot_as_file('파일이름.확장자명')

# 브라우저 창 닫음
# browser.close()