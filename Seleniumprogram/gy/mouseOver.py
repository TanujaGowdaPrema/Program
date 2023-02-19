'''
Created on 19-Feb-2023

@author: tanuj
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver = webdriver.Chrome(options=options)
#driver.get("http://www.google.com")
driver.get("https://amzn.to/3XXFkKd")
#https://amzn.to/3XXFkKd
img=driver.find_element(By.ID,"landingImage")
#//img[@id='landingImage']
action=ActionChains(driver)
action.move_to_element(img).perform()

# //img[@id='landingImage']"
