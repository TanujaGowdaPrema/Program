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
driver.get("https://testautomationpractice.blogspot.com/")
slideer=driver.find_element(By.XPATH,"//span[@tabindex='0']")
action=ActionChains(driver)
#action.move_to_element(slide).perform()
#action.drag_and_drop_by_offset(slide,150,0).perform()
action.click_and_hold(slideer).move_by_offset(180,0).perform()