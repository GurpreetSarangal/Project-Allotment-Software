from getStudentsData.fetch_data import *
from getStudentsData.inputs import *
from getStudentsData.login_script import *
from getStudentsData.select_class import *
from getStudentsData.format_data import *
from getStudentsData.csv_to_db import *
# data = get_inputs()
data = [
    "Dec-2021",
    "29-01-2022",
    "A",
    14,
    "B.Sc. (Information Technology)",
    5,
    "computer Networks",
    2021,
]
driver = login()
set_options(driver, data)
raw_csv_path = fetch_students(driver)
csv_path = format_csv(raw_csv_path)
insert_stu_details(csv_path)