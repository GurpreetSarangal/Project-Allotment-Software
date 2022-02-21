import pandas as pd
import sqlite3

def create_table():
    conn = sqlite3.connect("database/college.db")
    # Session,Roll_no,Student_Name,Father_Name,Class_Name,Email_ID,Mobile_1,Mobile_2

    try:
        create_student_table = '''create table students(
        Session varchar2(10),
        Roll_no int primary key,
        Student_Name varchar2(30),
        Father_Name varchar2(30),
        Class_Name varchar2(60),
        Email_ID varchar2(60),
        Mobile_1 int,
        Mobile_2 int
        );'''
        conn.execute(create_student_table)
    except:
        pass

    conn.commit()
    return conn
    
def insert_stu_details(csv_path):
    conn = create_table()

    sql = 'insert into students values (?,?,?,?,?,?,?,?)'

    # csv_path = "data/student/Bachelor of Computer Applications, Semester - V-2021.csv"
    data = pd.read_csv(csv_path)
    student_details = data.values

    for student in student_details:
        conn.execute(sql,student)

    conn.commit()
    conn.close()