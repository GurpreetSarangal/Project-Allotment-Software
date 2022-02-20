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

    # * this command opens a new tab
    # * element = driver.find_element_by_link_text('''Mark Absentee / Date Wise Centre Wise Candidate List For May-2020/2021''')
    # * element.send_keys(Keys.RETURN)

    driver.get("https://collegeadmissions.gndu.ac.in/ExUserArea/MarkAbsentee.aspx")
    # action = ActionChains(driver)
    # action.click(on_element=element)
    # action.perform()
    time.sleep(2)
    # Select(driver.find_element(By.ID, "DropDownSession")).select_by_index(2)

    sel = driver.find_element(By.ID, "DropDownSession")
    sel = Select(sel)
    sel.select_by_visible_text("Dec-2021")

    day = driver.find_element(By.ID, "textboxDay")
    month = driver.find_element(By.ID, "textboxMonth")
    year = driver.find_element(By.ID, "textboxYear")

    day.send_keys("29")
    month.send_keys("01")
    year.send_keys("2022")

    examSession = Select(driver.find_element(By.ID, "dropDownExamsession"))
    examSession.select_by_visible_text("A")

    centres = Select(driver.find_element(By.ID, "dropDownCentres"))
    centres.select_by_visible_text("Amritsar-15 [D.A.V.College,Block-3 , Amritsar]")

    time.sleep(1)

    sel_class = Select(driver.find_element(By.ID, "dropDownClass"))
    sel_class.select_by_visible_text("Bachelor of Computer Applications, Semester - V")

    sel_class = Select(driver.find_element(By.ID, "dropDownSubject"))
    sel_class.select_by_visible_text("COMPUTER NETWORKS {2021}")

    year = driver.find_element(By.ID, "buttonDateSubmit")
    year.send_keys(Keys.RETURN)
    return driver