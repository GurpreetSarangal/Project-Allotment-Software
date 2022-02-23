import re
import logging
import pandas as pd

def format_csv(csv_path):
    logging.basicConfig(format='%(asctime)s %(name)s %(levelname)s :  %(message)s')  
    logger = logging.getLogger("CSV-formatter")
    logger.setLevel(logging.DEBUG) 

    try:
        data = pd.read_csv(csv_path) 
    except:
        logger.error("CSV don't exist")
        return 0
    
    logger.info("Formatting Started")

    # Headers before formatting
    # ['Roll No.', 'Name / Father', 'Class Name', 'Subject Year', 'Subject Name', 'Email-ID', 'Mobile']

    # formatting the headers
    raw_header = list(data.columns) 
    header = ["Session"]  # 1st header
    header.append("Roll_no")  # 2nd header
    name = re.split(r' / ',raw_header[1])
    if(len(name)>1):
        name[0] = 'Student_'+name[0]
        name[1] = name[1] + '_Name'
    else:
        logger.info("CSV already formatted")
        return 
    header.extend(name)  # 3rd Student_Name and 4th Father_Name
    header.append("Class_Name")  # 5th Class_Name
    # header.append(raw_header[4]) # subject name
    header.append("Email_ID")  # 6th Email_ID
    header.append(raw_header[6]+'_1')  # 7th first mobile number Mobile_1
    header.append(raw_header[6]+'_2')  # 8th second mobile number Mobile_2

    # headers after formatting
    # Session, Roll_no, Student_Name, Father_Name, Class_Name, Email_ID, Mobile_1, Mobile_2

    # formatting the details of each student
    raw_data = data.values

    final_data = []
    for student in raw_data:
        temp_final_data = []
        temp_final_data.append(f"{int(student[3]) - 1}-{student[3]}") # Session 
        temp_final_data.append(student[0]) # Roll_no
        temp_final_data.extend(re.split(r' / ',str(student[1]))) # Student_Name and Father_Name
        temp_final_data.append(student[2]) # Class_Name
        # temp_final_data.append(student[4]) # subject name is not required in the project
        temp_final_data.append((re.split(r" \-\(", student[5]))[0]) # Email_ID sliced from -(verified)
        temp_final_data.extend(re.split(r", ",student[6])) # splited two mobile numbers Mobile_1 Mobile_2
        final_data.append(temp_final_data)

    csv_data = pd.DataFrame(final_data, columns=header)
    csv_data.to_csv(csv_path, index=False)
    logger.info("Formatting completed")
        