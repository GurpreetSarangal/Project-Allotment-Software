# Project Allotment Software

Provides an interactive interface for the process of manual allotment of projects to final year students.  

### Why this project?
It was noticed that staff of our college used to type all the details of each student into an excel file (CSV). These excel files were then used by staff to allocate projects manually on paper. Then again they type a new file for each class with allocation data.  
This whole process is made easy for the staff in this project.  
    

### What this project does?
This project automatically generates the excel files required by the staff and also provides an interface to allocated projects, and provides an automatically generated excel file which is required for office work. The final excel file contains information about __student, project and guide__ allocated to that student.

### How to get this project?
Currently this project is in development phase so if one wants to use this project please refer [developer's documentations](developer_guide.md).

---
## Features
__ONLY AUTHORIZED USERS CAN LOGIN TO THE WEBSITE__  
Once the user is logged in, the staff can __[allocate projects]( #allocate-project ) or [guides]( #allocate-guides )  to students__ or can [edit](#edit-an-existing-project)/[create](#create-new-project)/[delete](#delete-a-project) projects.  
After allocating projects and guides to the students, final Allocation-table can be viewed and downloaded (<font size="2"> currently in development </font>) for distribution and office work.

- ### Allocate Project 
    First Select the class which is to be allocated. Then we can chose __first__ and __second*__ roll numbers to which the project is to be allocated.  
    Only those projects can be allocated which are not allocated yet. So the __projects__ dropbox only shows those projects which are not allocated yet. 
    Staff member can change the language and technology to be used in the project. Doing such will create a altogether new project with same title but different lang and tech, and this will be allocated to roll number(s) selected. But if a completely new project is required then it should be first [created](#create-new-project)
- ### Allocate Guides
    The student which are already been allocated a project, requires a guide. This window will help in that. Firstly select name of the guide which is going to be allocated, then select the entries of allocation-table, and click _Assign_.
    
- ### Create New Project
    To register a new project we need it's title, languages which can be used to develop the project and other technologies used in project. Technologies can be optional. 
    A new project may have a same title as other project, but the languages and technologies must differ.
- ### Edit an existing Project
    To edit an existing project click the __edit__ button in the project details. This will take to the edit page, edit the details and click __EDIT__ button to save the changes.
- ### Delete a Project
    To delete an existing project, click to __edit__ button of the project, then click the __DELETE__ button on edit page.

- ### Viewing Project Wise Allocation Project
    Just select the class, and the table will contain information of all the students which are allocated a project. For downloading this table read [this](#downloading-final-excel-file)
- ### Viewing Guides Wise Allocation Project
    ust select the guide, and the table will contain information of all the students which are allocated to the guide. For downloading this table read [this](#downloading-final-excel-file)
- ### Downloading final Excel file
    Currently this feature is under development phase.