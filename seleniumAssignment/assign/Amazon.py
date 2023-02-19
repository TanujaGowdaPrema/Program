'''
Created on 16-Feb-2023

@author: tanuj
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://amazon.com")
driver.find_element(By.XPATH,
#act_title=driver.title
#exp_title="shirt"
#//*[@id="glow-ingress-line2"]