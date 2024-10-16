# APP_Project

## How to use

1) Make a new folder in your system
    - For Windows or Mac/Ubuntu use:
  `mkdir FolderName`
  
2) Change Directory into the newly created folder
    - For Windows or Mac/Ubuntu use:
  `cd FolderName`

3) Run this to create a virtual environment
    - For Windows or Mac/Ubuntu use:
  `python3 -m venv .venv`
  
4) Activate the virtual environment using
    - For Windows:
  `.venv/Scripts/activate`
    - For Mac/Ubuntu:
  `source .venv/bin/activate`

5) Run this to install `Flet` into your venv
    - For Windows or Mac/Ubuntu:
  `pip install flet mysql-connector-python`

6) Clone the repo into the current working directory

7) In the `└─backend` directory make a file named `.env` with this inside

```python
MYSQL_HOSTNAME="localhost"
MYSQL_USERNAME="your-username"
MYSQL_PASSWORD="your-password"
```

**Replace your username and password with the MySQL username and password**

8) Run this to start the app
    - For Windows or Mac/Ubuntu:
  `flet run main.py`

> Run this to deactivate the virtual environment
>
> - For Windows or Mac/Ubuntu: `deactivate`

## How to check for data in MySQL:

For Windows:
Open a Command Prompt/PowerShell Window and run this
```
# replace X.X with your own MYSQL Server version (optionally add this to your environment variables)
cd "Program Files\MySQL\MySQL Server X.X\bin" 
run mysql -u root -p
#enter your password

run USE lockedin;
run SHOW TABLES;
run SELECT * FROM (table_name);
```

For Mac/Linux:
Open a Terminal window and run this
```
run mysql -u root -p 
#enter your password

run USE lockedin;
run SHOW TABLES;
run SELECT * FROM (table_name);
```
