import pymysql

# global var
conn = None
cur = None
host = ''
port = 0
user = 'root'
password = ''
charset = 'utf8'

sql = ""

# db connection
conn = pymysql.connect(host=host, port=port, user=user, password=password,charset=charset)
cur = conn.cursor()

# DB creation
sql = "CREATE DATABASE IF NOT EXISTS PythonDB"
cur.execute(sql)

# DB selection
sql = "USE PythonDB"
cur.execute(sql)

# Table creation
sql = 'CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(10), email char(15), birthYear int)'
cur.execute(sql)

conn.commit()

conn.close()