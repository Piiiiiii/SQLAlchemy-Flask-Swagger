# Author: Pi
# Debug command: heroku logs --tail -a infinite-coast-22486

from flask import Flask, request, jsonify
import psycopg2
import json

app = Flask(__name__)
cur = None
conn = None
new_table_name = 'revised_campaigns'


@app.route('/')
def connect_heroku_pqsql():
    try:
        # Update this URL with yours
        DATABASE_URL = 'postgres://atzsrcjrnfaauu:f5b344ab9841661b4c5e8381a9474eb45fdb3d017e6faacf7ef853244b57a417' \
                       '@ec2-107-22-234-204.compute-1.amazonaws.com:5432/deaqbkvj1rtk6f'
        global conn
        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        conn_info = json.dumps(conn.info.dsn_parameters)
        global cur
        cur = conn.cursor()
        return 'Connect success ' + conn_info
    # Catch all errors from psycopg2
    except psycopg2.Error as error:
        return "error: {}".format(str(error))


@app.route('/create_types', methods=['GET'])
def create_types():
    try:
        # Define types
        cur.execute("CREATE TYPE campaign_obj_type_enum AS ENUM ('私域促活/留存', '私域拉新', '裂变');")
        cur.execute("CREATE TYPE campaign_time AS (campaign_time_start date, campaign_time_end date);")
        cur.execute("CREATE TYPE campaign_object_type AS (object_type varchar, editorial_topic_name varchar, editorial_topic_tags varchar[]);")
        cur.execute("CREATE TYPE campaign_core_metric_type AS (type varchar, value varchar);")
    except psycopg2.Error as error:
        conn.rollback()
        return "error: {}".format(str(error))
    # Occurs when cur is NoneType due to the failed connection
    except AttributeError as error:
        return "error: no connection"


@app.route('/create_table', methods=['GET'])
def create_table():
    try:
        # Create a new table
        cur.execute("CREATE TABLE " + new_table_name + " (id serial PRIMARY KEY, campaign_name varchar,"
                                                       " campaign_obj_type campaign_obj_type_enum,"
                                                       " campaign_timeline campaign_time, campaign_object campaign_object_type, "
                                                       " campaign_core_metric campaign_core_metric_type,"
                                                       " user_id UUID, token varchar, campaign_id varchar);")
        # Fetch the names of all the tables in this database
        cur.execute("""SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'""")
    except psycopg2.Error as error:
        conn.rollback()
        return "error: {}".format(str(error))
    else:
        tables = cur.fetchall()
        # Traverse the tables reversely
        for i in range(len(tables) - 1, -1, -1):
            table = tables[i]
            table = table[0]
            if table == new_table_name:
                conn.commit()
                return 'Create success'
        return 'Create failed'


@app.route('/create_campaign', methods=['POST'])
def create_campaign():
    user_id = request.values.get('user_id')
    token = request.values.get('token')

    request_body = request.get_json()
    campaign_name = request_body['campaign_name']
    campaign_obj_type = request_body['campaign_obj_type']
    campaign_time_start = request_body['campaign_time_start']
    campaign_time_end = request_body['campaign_time_end']

    try:
        cur.execute("INSERT INTO " + new_table_name + " (campaign_name, campaign_obj_type,"
                                                      " campaign_timeline, user_id, token)"
                                                      " VALUES (%s, %s, (%s, %s), %s, %s);",
                    (campaign_name, campaign_obj_type, campaign_time_start, campaign_time_end, user_id, token))
        conn.commit()
        return 'success'
    except psycopg2.Error as error:
        conn.rollback()
        return "error: {}".format(str(error))
    except AttributeError as error:
        return "error: no connection"


@app.route('/add_topic_task', methods=['POST'])
def add_topic_task():
    user_id = request.values.get('user_id')
    token = request.values.get('token')

    request_body = request.get_json()
    campaign_id = request_body['campaign_id']
    campaign_object = request_body['campaign_object']
    object_type = campaign_object["object_type"]
    editorial_topic_name = campaign_object["editorial_topic_name"]
    editorial_topic_tags = campaign_object["editorial_topic_tags"]
    try:
        cur.execute("INSERT INTO " + new_table_name + " (user_id, campaign_id, campaign_object, token)"
                                                      " VALUES (%s, %s, (%s, %s, %s), %s);",
                    (user_id, campaign_id, object_type, editorial_topic_name, editorial_topic_tags, token))
        conn.commit()
        return 'success'
    except psycopg2.Error as error:
        conn.rollback()
        return "error: {}".format(str(error))
    except AttributeError as error:
        return "error: no connection"


@app.route('/get_campaigns', methods=['GET'])
def get_campaigns():
    user_id = request.values.get('user_id')
    token = request.values.get('token')
    try:
        items_per_page = int(request.values.get('items_per_page'))
        page_number = int(request.values.get('page_number'))
    except TypeError as error:
        # Default values
        items_per_page = 15
        page_number = 1

    try:
        cur.execute("SELECT campaign_name, campaign_obj_type, campaign_timeline, campaign_core_metric FROM " + new_table_name
                    + " WHERE user_id = %s AND token = %s LIMIT %s;",
                    (user_id, token, items_per_page * page_number))
        #conn.commit()
        select_list = cur.fetchall()
        response_list = []
        for i in range(len(select_list)):
            temp_tuple = select_list[i]
            temp_dict = {
                "campaign_name": temp_tuple[0],
                "campaign_obj_type": temp_tuple[1],
                # Uncomment when these data are not None
                # "campaign_time_start": temp_tuple[2][0],
                # "campaign_time_end": temp_tuple[2][1],
                # "campaign_core_metric": {
                #     "type": temp_tuple[3][0],
                #     "value": temp_tuple[3][1]
                # }
            }
            response_list.append(temp_dict)
        res_dict = {"response_body": response_list}
        return jsonify(res_dict)

    except psycopg2.Error as error:
        #conn.rollback()
        return "error: {}".format(str(error))
    except AttributeError as error:
        return "error: no connection"
    except TypeError as error:
        return "error: {}".format(str(error))
