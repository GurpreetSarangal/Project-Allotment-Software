from ast import Str
from email.utils import formataddr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import re

def format_inputs(inputs):
    formatted_input = {
        "session" : inputs[0],
    }

    # format the date
    date = re.split(r"-",inputs[1])
    formatted_input["day"] = date[0]
    formatted_input["month"] = date[1]
    formatted_input["year"] = date[2]

    formatted_input["ExamSession"]= inputs[2]# Exam Session
    if int(inputs[3]) < 16:
        centernumber = 'Amritsar-'+str(inputs[3])+' [D.A.V.College,Block-'+str(inputs[3]-12)+' , Amritsar]'# Center number
    else:
        centernumber = 'P-Amritsar-16 [D.A.V.College,Block-4(Common) , Amritsar]'
    formatted_input["centerNumber"] = centernumber
    className = inputs[4]
    sem = inputs[5]
    if sem == 1 : sem = 'I'
    if sem == 2 : sem = 'II'
    if sem == 3 : sem = 'III'
    if sem == 4 : sem = 'IV'
    if sem == 5 : sem = 'V'
    if sem == 6 : sem = 'VI'

    formatted_input["className"] = className + ", Semester - " + sem

    subjectName = str(inputs[6])
    subjectName = subjectName.upper()
    subjectName = subjectName + ' {'+str(inputs[7]) + '}'

    formatted_input["subjectName"] = subjectName
    # print(formatted_input)
    return formatted_input


def set_options(driver,data):
    data = format_inputs(data)

    sel = driver.find_element(By.ID, "DropDownSession")
    sel = Select(sel)
    sel.select_by_visible_text(data["session"])

    day = driver.find_element(By.ID, "textboxDay")
    month = driver.find_element(By.ID, "textboxMonth")
    year = driver.find_element(By.ID, "textboxYear")

    day.send_keys(data["day"])
    month.send_keys(data["month"])
    year.send_keys(data["year"])

    examSessionElement = Select(driver.find_element(By.ID, "dropDownExamsession"))
    examSessionElement.select_by_visible_text(data["ExamSession"])

    centres = Select(driver.find_element(By.ID, "dropDownCentres"))
    centres.select_by_visible_text(data["centerNumber"])

    time.sleep(1)

    sel_class = Select(driver.find_element(By.ID, "dropDownClass"))
    sel_class.select_by_visible_text(data["className"])

    sel_class = Select(driver.find_element(By.ID, "dropDownSubject"))
    sel_class.select_by_visible_text(data["subjectName"])

    year = driver.find_element(By.ID, "buttonDateSubmit")
    year.send_keys(Keys.RETURN)
    return driver

