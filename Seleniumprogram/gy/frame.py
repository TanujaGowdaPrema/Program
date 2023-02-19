'''
Created on 17-Feb-2023

@author: tanuj
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://google.com")
time.sleep(5)
driver.switch_to.frame("callout")
driver.find_element(By.XPATH,"//a[@aria-label='Sign in']").click()
time.sleep(5)
driver.switch_to.parent_frame()
#driver.find_element(By.XPATH,"//a[@class='gb_p' and @ aria-label='Gmail (opens a new tab)']").click()