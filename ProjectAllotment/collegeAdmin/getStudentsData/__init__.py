from . import loginScript 
from . import selectClass 
from . import fetchData 
from . import formatData 
from . import csvToDb 
from . import inputs 


def from_website(data, CSV_PATH=''):
    driver = loginScript.login()
    selectClass.set_options(driver, data)
    # ? check if csv path is provided of not
    if CSV_PATH=='':
        CSV_PATH = fetchData.data_scraper(driver)
    else:
        CSV_PATH = fetchData.data_scraper(driver, CSV_PATH)

    formatData.format_csv(CSV_PATH)
    return CSV_PATH
    # csvToDb.insert_stu_details(CSV_PATH)


# def from_csv(CSV_PATH, DATABASE_PATH='database/college.db'):
#     formatData.format_csv(CSV_PATH)
#     csvToDb.insert_stu_details(CSV_PATH,DATABASE_PATH)