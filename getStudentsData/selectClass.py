import time
import re
import logging

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

def isValide(inputs):
    pass


def formatInput(inputs):
    formatted_input = {
        "session": inputs["session"],
    }

    # format the date
    date = re.split(r"-", inputs["date"])
    formatted_input["day"] = date[0]
    formatted_input["month"] = date[1]
    formatted_input["year"] = date[2]

    formatted_input["ExamSession"] = inputs["examSession"]  # Exam Session
    if int(inputs["centre"]) < 16:
        centerName = (
            "Amritsar-"
            + str(inputs["centre"])
            + " [D.A.V.College,Block-"
            + str(inputs["centre"] - 12)
            + " , Amritsar]"
        )  # Center number
    else:
        centerName = "P-Amritsar-16 [D.A.V.College,Block-4(Common) , Amritsar]"
    formatted_input["centerNumber"] = centerName
    className = inputs["class"]
    sem = inputs["semester"]
    if sem == 1:
        sem = "I"
    if sem == 2:
        sem = "II"
    if sem == 3:
        sem = "III"
    if sem == 4:
        sem = "IV"
    if sem == 5:
        sem = "V"
    if sem == 6:
        sem = "VI"

    formatted_input["className"] = className + ", Semester - " + sem

    subjectName = str(inputs["subject"])
    subjectName = subjectName.upper()
    subjectName = subjectName + " {" + str(inputs["subjectYear"]) + "}"

    formatted_input["subjectName"] = subjectName
    # print(formatted_input)
    return formatted_input


def set_options(driver, data):
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  
    logger = logging.getLogger("ClassSelector")
    logger.setLevel(logging.DEBUG) 

    if isValide(data) == False:
        logger.critical("Invalide Inputs")
        return 0

    data = formatInput(data)
    logger.info("Selecting class...")

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

    logger.info("Class Selected")
    return driver
