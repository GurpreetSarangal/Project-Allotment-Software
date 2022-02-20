from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from dotenv import load_dotenv

import os
import time

load_dotenv()


def login():
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
    driver.get("https://collegeadmissions.gndu.ac.in/ExUserArea/MarkAbsentee.aspx")
    return driver  