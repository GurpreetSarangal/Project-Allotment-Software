# Developer's Guide

## Step 1 : Get Code
First of all you'll need to download all the code to your local machine. For this there are two ways: noob and pro. 
### Noob way
Download the zip file and extract it to the folder of your choice.
### Pro Way
1. Install `git` 
2. Go to the folder and open terminal here.
3. Type command :
    
        git clone https://github.com/GurpreetSarangal/Project-Allotment-Software.git


## Step 2 : Install the requirements
1. Once all the code is downloaded, open it in VSCode (coz I use it).
2. Make sure the folder __`Project-Allotment-Software`__ is open in terminal.
3. Here we are gonna require virtual environment of python. If you don't know how to create a virtual environment refer to this [heading](#how-to-create-virtual-environment)
4. After activating venv we'll install all the requirements by typing following command

        pip install -r requirements.txt
5. After all the requirements installed we are ready to start our project

>Always make sure to activate venv before starting the project

## Step 3 : Start the django server
1. If your terminal is on `Project-Allotment-Software` then cd to `ProjectAllotment`

        cd ProjectAllotment/

2. Once you are on `ProjectAllotment` folder, type `ls` to check if the folder contains `manage.py` file.

        $ ls

        collegeAdmin  college.db  login  manage.py  ProjectAllotment  staff

3. Now you can start the django server by typing following command:

        python manage.py runserver

4. After starting the server your website will be live on `localhost:8000//`

5. To Quit the server press <kbd>Ctrl</kbd> + <kbd>C</kdb>

> If you accidentally close the terminal without quitting the server, and again try to run the server, it'll show an error that `this port is already in use`. To remove this error refer [this](#error--this-port-is-already-in-use)

## Step 4 : Login as a user
In this project we have two types of susers: Staff and the Admin. And you will need to contact me for usernames and passwords ; )

---
>>Now you will need to understand internal working of the project so refer to [this](internal_working.md) guide

---

### How to create virtual environment
1. Firstly install the `virtualenv` library on your local computer.
2. Then open the folder and invoke the terminal here.
3. Type in the command :

        $ virtualenv <my_env_name>
        $ source <my_env_name>/bin/activate
        

4. For example:

        virtualenv venv
        source venv/bin/activate

5. These commands will create and activate the virtual environment for python. Now you'll have to install all the requirements of the project explained [here](#step-2--install-the-requirements)

> Note that all these commands are for linux or unix based operating systems for windows refer [here](#creating-virtual-environment-on-windows)

---
## Troubleshooting
### Creating virtual environment on windows
1. Install `virtualenv` 

        pip install virtualenv

2. Type this to create the virtual environment 

        virtualenv <my_env_name>

3. Now activate the virtual environment

        <my_env_name>\Scripts\activate

4. It can be deactivated by this command :

        deactivate


### Error : `this port is already in use`
This error can be resolved by explicitly closing the port :

        sudo fuser -k 8000/tcp


