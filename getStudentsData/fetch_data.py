from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
# import os
import time


driver = webdriver.Chrome()
driver.get('http://127.0.0.1:5500/test2.html')

