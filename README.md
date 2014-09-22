CS253 Final
==========
This is Udacity CS253 final project in Flask.
----------

### Some difference between this one and origin cs253 final project:
- Using Flask
- Using Markdown as page content
- Using MongoDB
- Previews

## PAGE
- ### [CS253 Final](http://cs253-final.herokuapp.com/)

## TODO

### Things you have to install:
- MongoDB
- python3
- virtualenv

### Step by Step Guide:

Clone Repository:
```
git clone https://github.com/adrianliaw/CS253-Final-Flask.git
```

Run MongoDB:
```
sudo mongod
```

Then switch to another window.
Change to correct directory:
```
cd CS253-Final-Flask
```

Create a Virtual Environment (With Python3):
```
virtualenv -p python3 venv
source venv/bin/activate
```

Install Requirement packages:
```
pip install -r requirements.txt
```

Run gunicorn (WSGI server):
```
gunicorn main:app
```

Go to 127.0.0.1:8000 (localhost:8000)
