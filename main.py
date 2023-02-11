from flask import Flask, request
import pymongo

app = Flask(__name__)

connect_Db_link = "mongodb+srv://<username>:<password>@cluster0.bkejb.mongodb.net/?retryWrites=true&w=majority"

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    text1 = str(request.args.get('input1'))
    text2 = str(request.args.get('input2'))
    text3 = str(request.args.get('input3'))
    character_count = len(text1) + len(text2) + len(text3)

    client = pymongo.MongoClient(connect_Db_link)
    db = client.get_database('Students_db')
    records = db.students_record
    dictionary = {'name': text1, 'roll_no': text2, 'mks': text3, 'CharCount': character_count}
    records.insert_one(dictionary)

    return "Data uploaded successfully."

if __name__ == '__main__':
    app.run(debug=True)
