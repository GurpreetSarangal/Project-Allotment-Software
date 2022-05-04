# Fetch Student Details from Website Using Selenium

I am using a library 'selenium' although this library is also available in other languages like JAVA. This uses the browser to access the internet through a webdriver. Every browser has its own webdriver which can be downloaded using following commands in linux:

```
sudo apt-get install unzip

wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip

unzip chromedriver_linux64.zip

chmod +x chromedriver

sudo mv -f chromedriver /usr/local/share/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
```

and to install selenium package

    python -m pip install selenium

##### simple example
```python
from selenium import webdriver

driver = webdriver.chrome()
driver.get("https://google.com")
```

----

### Use of `.env` files

If we are using sensitive data like passwords with our testing script then is not safe to store them directly in the code, so for keeping them safe we can use environment variables of the system. The `.env` file contains the key-value pairs for the variables we want to store. The file name starting with ' . ' are hidden so they add another layer as they are not directly visible. 
We need to import 
```python
from dotenv import load_dotenv
```
`load_dotenv()` is called to load all variable in the system. <br>
Once loaded we can access them by importing `os` library as
```python
import os
value = os.envron.get("environment_name")
```

----

### `.find_element()` method 
T
his method is used to locate elements in html file.
syntax
```python
driver.find_element(By.ID, 'id')
driver.find_element(By.CLASS_NAME, 'class_name')
driver.find_element(By.CSS_SELECTOR, 'Selector')
driver.find_element(By.LINK_TEXT, 'Link_text')
driver.find_element(By.PARTIAL_LINK_TEXT, 'partial_link')
driver.find_element(By.TAG_NAME, 'tag')
driver.find_element(By.X_PATH, 'path')
```

Once the element is selected we can press keys using method `send_keys()`

### `send_keys()` method

This method is used to input data to `<input>` tag or to press different keys using `Keys`.
The syntax is 
```python
from selenium.webdriver.common.keys import Keys

element = driver.find_element(By.ID, 'id')
element.send_keys("keys to be pressed")
element.send_keys(keys.RETURN)
# Other examples

element.send_keys(keys.ADD)
element.send_keys(keys.ARROW_UP)
element.send_keys(keys.ARROW_DOWN)
element.send_keys(keys.TAB)
element.send_keys(keys.COMAND)
element.send_keys(keys.CONTROL)
element.send_keys(keys.ESCAPE)
element.send_keys(keys.HOME)
element.send_keys(keys.INSERT)
element.send_keys(keys.BACKSPACE)
element.send_keys(keys.CANCEL)
```

----

### `Select()` method
Select method throws an exception if the selected element is not a `<select>` tag.
Syntax
```python
from selenium.webdriver.support.select import Select

drop = Select(driver.find_element(By.ID, 'id'))
```
after pointing the `<select>` tag we can use `select_by_*()` methods on the element to select from the `<option>` tags in the `<select>` tag.
syntax
```python
drop.select_by_index(1)
drop.select_by_value("value_of_option")
drop.select_by_visible_text("The visible text of option")
```
----
### `sleep()` method
This method stops the execution of program for the number of seconds passed as argument.
Syntax:
```python
import time

time.sleep(10)# this will stop execution for 10 seconds
```
# Django

### Installing django
    pip install django
    
### Starting django project
    django-admin startproject <project_name>

### Running project
    python manage.py runserver

### Sreating new app
    python manage.py startapp <app_name>

Django does not automatically detect that an app exists. Instead it has to be registered by adding its name to the list of `INSTALLED_APPS` in your settings.
```python
INSTALLED_APPS = [
    # ...
    'app_name'
]
```

### Create models
```python
from django.db import models
class model_name(models.Model):
    column_name = models.IntegerField()
    # ...
```
These models represents tables in database. We can use different models fields for various relations.

After creating models we need to run 

    python manage.py makemigrations
makemigrations - create changes and store them in a file.

    python manage.py migrate

migrate - apply the pending changes to database

to execute the changes in database.

### Create views
```python
def index(request):
    return HttpResponse("this is dummy text")
```

```python

urlpatterns = [
    path('index/', views.index, name='index'),
]
```
In views.py of app, this function will be called if we visit 
`http://127.0.0.1:8000/index/` 

### Create templates
```django html
<html>
{% block block_name %}
{% endblock block_name %}
</html>
```
basically write you html in pieces and join them at time of rendering

`{% extends 'base.html' %}`

this is used to specify base html file, this `base.html` file basically contains the basic format of the html page

### Create views that acutally do something
```python
def index(request):
    return render(request, 'index.html')
```
this view will return an html page (`index.html`) 

### How to handle forms

### How to fetch data from tables

### How to generate html dynamically

### How to input values to tables using the existing data in csv files

## Troubleshooting

__Error: That port is already in use.__  
    
    sudo fuser -k 8000/tcp

# preload
sudo apt install preload