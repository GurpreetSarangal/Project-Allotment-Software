from . import loginScript 
from . import selectClass 
from . import fetchData 
from . import formatData 
from . import csvToDb 
from . import inputs 


def from_website(data):
    driver = loginScript.login()
    selectClass.set_options(driver, data)
    csv_path = fetchData.data_scraper(driver)
    formatData.format_csv(csv_path)
    csvToDb.insert_stu_details(csv_path)

def from_csv(CSV_PATH, DATABASE_PATH='database/college.db'):
    formatData.format_csv(CSV_PATH)
    csvToDb.insert_stu_details(CSV_PATH,DATABASE_PATH)