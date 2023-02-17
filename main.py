import pymongo
from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
# filename = 'sample.json'


client = pymongo.MongoClient(connect_Db_link)
db = client.get_database('Students_db')
records = db.students_record

app = Flask(__name__)
api = Api(app)

class VideoCls(Resource):

    def get(self,name,views,likes):
        retMSG = {
                        "name": name,
                        "views": views,
                        "likes": likes,
                        "dB_total": records.count_documents({})
                    }


#         with open(filename, "r") as file:
#             data = json.load(file)
#         data.append(retMSG)
#         with open(filename, "w") as file:
#             json.dump(data, file,indent=4)

        records.insert_one(retMSG)


        return {"Success":200,"MongodB_Total_Records":retMSG["dB_total"]}


api.add_resource(VideoCls,"/video/<string:name>/<int:views>/<int:likes>")

if __name__ == "__main__":
    app.run(debug=True)
  
