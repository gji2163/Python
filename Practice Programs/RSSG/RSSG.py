from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }

options = webdriver.ChromeOptions()
options.binary_location = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
options.add_experimental_option('prefs', prefs)

options.add_argument('--kiosk-printing')


driver = webdriver.Chrome('chromedriver', options=options)

file=open('Index.txt','r').readlines()
for i in range(2918):
    a=''
    for j in file[i].split('-')[1].strip(' \n'):
        if j==' ':
            a+='-'
        elif j.isalpha():
            a+=j.lower()
    driver.get('https://readnovelfull.com/reincarnation-of-the-strongest-sword-god/chapter-'+str(i+1)+'-'+a+'.html')
    driver.execute_script('window.print();')
