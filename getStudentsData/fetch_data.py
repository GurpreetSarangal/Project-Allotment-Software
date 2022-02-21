from operator import index
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import pandas as pd
# import os
import time




def fetch_students(driver):
    table = driver.find_element(By.XPATH, '//table[@id="gridViewDetail"]')
    header = []
    data = []
    for row in table.find_elements(By.XPATH,'.//tr/th'):
        # print(row.text)
        header.append(row.text)
    del header[0]

    for row in table.find_elements(By.XPATH,'.//tr'):
        # print(row.text)
        st_det = []
        for td in row.find_elements(By.XPATH, './/td'):
            # print(td.text)
            st_det.append(td.text)
        if len(st_det) > 0:
            st_det.remove('')
            data.append(st_det)

    driver.close()
    csv_data = pd.DataFrame(data, columns=header)
    csv_data.to_csv(f'data/student/{(data[0])[2]}-{(data[0])[3]}.csv', index=False)
    return f'data/student/{(data[0])[2]}-{(data[0])[3]}.csv'