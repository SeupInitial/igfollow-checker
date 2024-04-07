from selenium import webdriver

options = webdriver.ChromeOptions()

options.add_argument('headless')
options.add_argument('no-sandbox')
options.add_argument('window-size=1920x1080')
options.add_argument('disable-gpu')
options.add_argument('lang=ko_KR')
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12.6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)

driver.get('https://naver.com')
driver.implicitly_wait(3)