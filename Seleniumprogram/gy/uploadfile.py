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
upload=driver.find_element(By.XPATH,"//input[@id='RESULT_FileUpload-10']")
= webdriver.Chrome(executable_path="C:\Users\tanuj\OneDrive\Documents")
action=ActionChains(driver)