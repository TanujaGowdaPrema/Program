'''
Created on 18-Feb-2023

@author: tanuj
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("start-maximized")
#options.add_argument("incognito")
driver=webdriver.Chrome(options=options)
#driver.maximize_window()
#driver.get("http://google.com")
driver.get("https://testautomationpractice.blogspot.com/")
driver.switch_to.parent_frame()
source=driver.find_element(By.XPATH,"//div[@id='draggable']")
target=driver.find_element(By.XPATH,"//div[@id='droppable']")
action=ActionChains(driver)
#action.drag_and_drop_by_offset(source,150,50).perform()
action.drag_and_drop(source,target).perform()
print(source.get_attribute("id"))
print(target.get_attribute("id"))



