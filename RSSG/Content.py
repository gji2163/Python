from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
options.add_argument('headless')
options.add_argument("disable-gpu") # OR options.add_argument("--disable-gpu")  

driver = webdriver.Chrome('chromedriver', options=options)

f=open('Index.txt','w')
driver.get('https://readnovelfull.com/reincarnation-of-the-strongest-sword-god.html#tab-chapters-title')
sleep(2)
f.write(driver.find_element_by_class_name('panel-body').text)

driver.quit()
