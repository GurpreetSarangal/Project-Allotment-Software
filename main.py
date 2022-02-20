from getStudentsData.fetch_data import *
from getStudentsData.inputs import *
from getStudentsData.login_script import *
from getStudentsData.select_class import *

# data = get_inputs()
data = [
    "Dec-2021",
    "29-01-2022",
    "A",
    15,
    "Bachelor of Computer Applications",
    5,
    "computer Networks",
    2021,
]
driver = login()
set_options(driver, data)
fetch_students(driver)
