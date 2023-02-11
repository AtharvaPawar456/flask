from flask import Flask, request
import json
import time
import pymongo

app = Flask(__name__)

connect_Db_link = "mongodb+srv://Atharva:gta456@cluster0.bkejbfi.mongodb.net/?retryWrites=true&w=majority"

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    text1 = str(request.args.get('input1'))
    text2 = str(request.args.get('input2'))
    text3 = str(request.args.get('input3'))
    character_count = len(text1) + len(text2) + len(text3)

    data_set = {'input1': text1, 'input2': text2, 'input3': text3, 'timestamp': time.time(), 'character_count': character_count}
    json_dump = json.dumps(data_set)

    client = pymongo.MongoClient(connect_Db_link)
    db = client.get_database('Students_db')
    records = db.students_record
    dictionary = {'name': text1, 'roll_no': text2, 'mks': text3}
    records.insert_one(dictionary)

    return json_dump
