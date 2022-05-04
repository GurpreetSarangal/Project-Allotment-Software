import os
import time
from dotenv import load_dotenv
import logging

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By



load_dotenv()
def login():
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  
    logger = logging.getLogger("WebsiteLogger")
    logger.setLevel(logging.DEBUG) 
    
    logger.info("logging-in to website")
    driver = webdriver.Chrome()
    driver.get("https://collegeadmissions.gndu.ac.in/loginNew.aspx")
    uname = driver.find_element(By.ID, "ContentPlaceHolder1_TXT_CollegeID")
    password = driver.find_element(By.ID, "ContentPlaceHolder1_TXT_CollPassword")
    submit = driver.find_element(By.ID, "ContentPlaceHolder1_But_CollSignIn")

    uname.send_keys(os.environ.get("username"))
    password.send_keys(os.environ.get("password"))
    time.sleep(1)
    submit.send_keys(Keys.RETURN)

    time.sleep(1)
    logger.info("logged-in")
    driver.get("https://collegeadmissions.gndu.ac.in/ExUserArea/MarkAbsentee.aspx")
    return driver  

