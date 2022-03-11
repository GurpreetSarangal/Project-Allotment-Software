import sqlite3
import logging
import pandas as pd
# from ..models import student
DATABASE_PATH = "database/college.db"

def create_students_table():
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  
    logger = logging.getLogger("CreateStudentsTable")
    logger.setLevel(logging.DEBUG) 
    conn = sqlite3.connect(DATABASE_PATH)

    # Session,Roll_no,Student_Name,Father_Name,Class_Name,Email_ID,Mobile_1,Mobile_2

    try:
        create_student_table = '''
        create table students(
            Session varchar2(10),
            Roll_no int primary key,
            Student_Name varchar2(30),
            Father_Name varchar2(30),
            Class_Name varchar2(60),
            Email_ID varchar2(60),
            Mobile_1 int,
            Mobile_2 int
        );
        '''
        conn.execute(create_student_table)
    except:
        logger.error("students table already existed")

    conn.commit()
    conn.close()
    
# ! this function will create a new database if not present and don't use django's models
def create_and_insert_stu_details(csv_path, DATABASE_PATH=DATABASE_PATH):
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  

    logger=logging.getLogger("DataInserter")
    logger.setLevel(logging.DEBUG) 
    
    conn = sqlite3.connect(DATABASE_PATH)
    check = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='student';")
    if not check.fetchall():
        create_students_table()

    sql = 'insert into student values (?,?,?,?,?,?,?,?)'
    data = pd.read_csv(csv_path)
    student_details = data.values

    for student in student_details:
        try:
            conn.execute(sql,student)
        except:
            logger.warning(f"Student rollno- {student[1]} already existed in database")

    logger.info("CSV converted to DB")
    conn.commit()
    conn.close()

# def insert_stu_details(csv_path):
#     logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  

#     logger=logging.getLogger("DataInserter")
#     logger.setLevel(logging.DEBUG)

#     data = pd.read_csv(csv_path)
#     student_details = data.values

#     for std in student_details:
#         try:
#             temp_student = student(
#                 session = std[0],
#                 rollNo = std[1],
#                 name = std[2],
#                 fatherName = std[3],
#                 className = std[4],
#                 email = std[5],
#                 mobile_1 = std[6],
#                 mobile_2 = std[7],
#             )
#             temp_student.save()
        
#         except:
#             logger.error(f"student with rollno {std[1]} already existed")
            

#     logger.info("CSV converted to DB")



