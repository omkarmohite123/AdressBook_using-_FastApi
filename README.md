## Need To Install


Xampp


pycharm


virtual environment


install mysql client from pycharn



## Command For Installing



pip install virtualenv



for ven activation :: venv/Scripts/activate.bat



pip install fastapi


for refreshing fastpi swagger automaticaly ::: uvicorn index:app --reload



pip install pymysql


pip install pydantic


pip install sqlalchemy


## Process


Creating 4 Directory:


1 models directory contain index.py and user.py 


2 routes directory contain index.py and user.py 


3 schemas directory contain index.py and user.py 


4 create seperate index.py


5 create configration file and create db on it



## Import Command



in db.py-> importing engine to connect sqlite db


in schemas -> importing basemodel to create user in user.py


in models-> in mporting api router for connecting to user in user.py 


in routes-> creating operation of update and add and delete in user.py


in.index.py->create Fastapi


## Source



Fastapi tutorial
