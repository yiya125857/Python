from selenium import webdriver
from time import sleep

on_off=1
#窗口开关
if on_off :
    driver = webdriver.Chrome()
else:
    
    from selenium.webdriver.chrome.options import Options
    chrome_options =Options()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('blink-settings=imagesEnabled=false') #图片加载
    driver = webdriver.Chrome(options=chrome_options)


driver.get("https://ping.chinaz.com/github.com")
print(driver.title)

sleep(126)
driver.quit()
