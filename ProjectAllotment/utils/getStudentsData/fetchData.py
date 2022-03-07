import logging

from selenium.webdriver.common.by import By
import pandas as pd



def data_scraper(driver):
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  
    logger = logging.getLogger("DataScraper")
    logger.setLevel(logging.DEBUG) 

    logger.info("Starting to fetch data...")
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

    logger.info("Fetching done")
    driver.close()
    RAW_CSV_PATH = f'data/student/{(data[0])[2]}-{(data[0])[3]}.csv'
    
    logger.info("Converting Fetched data into raw CSV")
    csv_data = pd.DataFrame(data, columns=header)
    csv_data.to_csv(RAW_CSV_PATH, index=False)
    logger.info("Raw CSV created")
    return RAW_CSV_PATH