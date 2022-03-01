import getStudentsData


class_data = {
    "session" : "Dec-2021",
    "date" : "29-01-2022",
    "examSession" : "A",
    "centre" : 15,
    "class" : "Bachelor of Computer Applications",
    "semester" : 5,
    "subject" : "computer Networks",
    "subjectYear" : 2021,
}

CSV_PATH = "data/student/Bachelor of Computer Applications, Semester - V-2021.csv"
DATABASE_PATH = "ProjectAllotment/college.db"
getStudentsData.from_csv(CSV_PATH,DATABASE_PATH)