from flask import Flask
import psycopg2
import json

app = Flask(__name__)
cur = None

@app.route('/')
def ConnectHerokuPqsql():
    try:
        # Update this URL with yours
        DATABASE_URL = 'postgres://atzsrcjrnfaauu:f5b344ab9841661b4c5e8381a9474eb45fdb3d017e6faacf7ef853244b57a417@ec2-107-22-234-204.compute-1.amazonaws.com:5432/deaqbkvj1rtk6f'
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn_info = json.dumps(conn.info.dsn_parameters)
        global cur
        cur = conn.cursor()
        return 'Connect success ' + conn_info
    except psycopg2.DatabaseError as error:
        return 'Connect failed'


@app.route('/CreateTable', methods=['GET'])
def CreateTable():
    new_table_name = 'test8'
    # Create a new table
    cur.execute("CREATE TABLE " + new_table_name + " (id serial PRIMARY KEY, num integer, data varchar);")
    # Fetch the names of all the tables in this database
    cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    for table in cur.fetchall():
        table = table[0]
        if table == new_table_name:
            return 'Create success'
    return 'Create failed'
