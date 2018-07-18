# flask-security-sample

This sample uses a sqlite database. If you want another database option, change the **SQLALCHEMY_DATABASE_URI** configuration. Check Flask-Security docs for syntax.

## Running the sample
Clone this repo and *enter the folder* using command prompt / terminal shell

### Create a Virtual Environment
If you are using Windows
```
python -m venv venv
venv\Scripts\activate
```
For Linux / Mac
```
python -m venv venv
source venv/bin/activate
```

### Install the requirements
Now, use the command
```
pip install -r requirements.txt
```

### Run
For the first time running, uncomment the function **create_user()** in the *projeto/__init__.py* file.
Inside the virtualenv, run 
```
python run.py
```
Open the url address in the browser, after that, comment the function **create_user()**
