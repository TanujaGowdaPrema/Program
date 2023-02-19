'''
Created on 18-Feb-2023

@author: tanuj
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(5)
#driver.switch_to.frame("callout")
click_me=driver.find_element(By.XPATH,"//button[@Onclick='myFunction()']")
click_me.click()
#driver.switch_to.window(driver.window_handles[1])
time.sleep(5)
driver.switch_to.alert.accept()
search=driver.find_element(By.XPATH,"//p[@id='demo']")
print(search.text)
time.sleep(5)
click_me.click()
driver.switch_to.alert.dismiss()
