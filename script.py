from selenium.webdriver import Firefox
from time import sleep 

url = 'https://www.google.com'
browser = Firefox()
browser.get(url)

sleep(2)

browser.quit()