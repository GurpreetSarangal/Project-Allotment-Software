import re

def get_inputs():
    inputs = []
    while True:
        userinput = input("Input Session eg:Dec-2021 :: ")
        session_regex = re.compile(r"[A-Z][a-z][a-z]-20[1|2][0-9]")
        session = session_regex.search(userinput)
        if session == None: 
            print("Warning: Invalid Input")
            continue
        inputs.append(session.group())
        break

    while True:
        userinput = input("Input Date eg:29-02-2022 :: ")
        dateRegex = re.compile(r"[0-3][0-9]-[0-1][0-9]-20[1|2][0-9]")
        date = dateRegex.search(userinput)
        if date == None: 
            print("Warning: Invalid Date")
            continue
        inputs.append(date.group())
        break

    while True:
        userinput = input("Input exam Session eg: M,E,A :: ")
        examRegex = re.compile(r"M|E|A")
        examSession = examRegex.search(userinput)
        if examSession == None: 
            print("Warning: Invalide Exam Session")
            continue
        inputs.append(examSession.group())
        break

    while True:
        centerNumber = int(input("Input center number eg:13,14,15,16 :: "))
        if centerNumber < 13 or centerNumber > 16:
            print("Warning: Invalid Center Number")
            continue
        inputs.append(centerNumber)
        break

    className = input("Input class name: B.A. ")
    inputs.append(className) 
    while True:
        sem = int(input("Input Semester eg: 1,2,3,4,5,6 :: "))
        if sem < 1 or sem > 6:
            print("Warning: Invalid Semester Number")
            continue 
        inputs.append(sem)
        break


    inputs.append(input("Input subject eg: COMPUTER NETWORKS :: "))

    inputs.append(input("Input subject year eg: 2019,2021,2022:: "))
    
    return inputs