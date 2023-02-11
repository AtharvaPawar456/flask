# from flask import Flask, jsonify
# import os

# app = Flask(__name__)


# @app.route('/')
# def index():
#     return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


# if __name__ == '__main__':
#     app.run(debug=True, port=os.getenv("PORT", default=5000))

    
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import request
import json
import time
import pymongo

# testing api link :

connect_Db_link = "mongodb+srv://Atharva:gta456@cluster0.bkejbfi.mongodb.net/?retryWrites=true&w=majority"

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def handle_request():
    text1 = str(request.args.get('input1'))   #request the ?inpur=a
    character_count = len(text1)

    text2 = str(request.args.get('input2'))   #request the ?inpur=a
    character_count = len(text2)

    text3 = str(request.args.get('input3'))   #request the ?inpur=a
    character_count = len(text3)

    data_set = {'input1': text1,'input2': text2,'input3': text3, 'timestamp': time.time(), 'character_count': character_count}
    json_dump = json.dumps(data_set)

    client = pymongo.MongoClient(connect_Db_link)
    db = client.get_database('Students_db')
    records = db.students_record
    dictionary = {'name':text1,'roll_no':text2,'mks':text3}
    records.insert_one(dictionary)

    return json_dump
