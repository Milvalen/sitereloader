from selenium import webdriver
from time import sleep

# opens the page
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get('https://github.com/Milvalen')


# main cycle
while True:
    sleep(0.01)
    driver.refresh()
driver.quit()