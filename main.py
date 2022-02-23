import getStudentsData

class_data = {
    "session" : "Dec-2021",
    "date" : "29-01-2022",
    "examSession" : "A",
    "centre" : 14,
    "class" : "B.Sc. (Information Technology)",
    "semester" : 5,
    "subject" : "computer Networks",
    "subjectYear" : 2021,
}

getStudentsData.from_website(class_data)