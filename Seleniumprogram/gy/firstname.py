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
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
click_me=driver.find_element(By.XPATH,"//button[@Onclick='myFunction()']")
click_me.click()
time.sleep(5)
driver.switch_to.alert.accept()
search=driver.find_element(By.XPATH,"//p[@id='demo']")
print(search.text)
time.sleep(5)
click_me.click()
driver.switch_to.alert.dismiss()
print(search.text)
driver.switch_to.frame("frame-one1434677811")
first_name=driver.find_element(By.ID,"RESULT_TextField-1")
first_name.send_keys("Tanuja") 
last_name=driver.find_element(By.ID,"RESULT_TextField-2")
last_name.send_keys("H N") 
check_box=driver.find_element(By.XPATH,"//label[@for='RESULT_CheckBox-8_0']")
driver.execute_script("arguments[0].scrollIntoView();",check_box)
check_box.click()

