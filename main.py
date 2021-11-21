from flask import Flask,request,jsonify
from flask_restful import Api,Resource
from flask_jwt import JWT,jwt_required
from security import authenticate,identity
from flask_pymongo import PyMongo


app = Flask(__name__)
api=Api(app)
app.secret_key="Mangesh@1997"
jwt=JWT(app,authenticate,identity)
app.config['MONGO_DBNAME'] = 'Nimbadevi'
app.config['MONGO_URI'] = 'mongodb+srv://Mangesh:MrPw5april@mangesh.29rlr.mongodb.net/Nimbadevi?retryWrites=true&w=majority'

mongo = PyMongo(app)


class AllData(Resource):

    def get(self,collname):
        collection = mongo.db[collname]
        output = {}
        for s in collection.find({}, {"_id": 0}):
            output.update(s)

        return jsonify(output)

    @jwt_required()
    def post(self,collname):
        collection = mongo.db[collname]
        data=request.get_json(force=True)
        collection.insert_one(data)
        return jsonify({"data":"inserted"})

    @jwt_required()
    def put(self,collname):
        collection = mongo.db[collname]
        data = request.get_json(force=True)
        collection.update_many(data['old'], {"$set": data['new']})

        return jsonify({"Data":"Updated.."})

    @jwt_required()
    def delete(self,collname):
        collection = mongo.db[collname]
        data = request.get_json(force=True)
        collection.delete_one(data["cond"])
        return jsonify({"data":"Deleted."})


class FormData(Resource):
    @jwt_required()
    def get(self):
        collection = mongo.db["FormData"]
        output = {}
        for s in collection.find({}, {"_id": 0}):
            output.update(s)

        return jsonify(output)

    def post(self):
        collection = mongo.db["FormData"]
        data=request.get_json()
        collection.insert_one(data)
        return jsonify({"data":"inserted"})

    @jwt_required()
    def put(self):
        collection = mongo.db["FormData"]
        data = request.get_json(force=True)
        collection.update_many(data['old'], {"$set": data['new']})

        return jsonify({"Data":"Updated.."})

   # @jwt_required()
    def delete(self):
        collection = mongo.db["FormData"]
        data = request.get_json(force=True)

        collection.delete_one(data["cond"])
        return jsonify({"data":"Deleted."})
##
api.add_resource(AllData, "/AllData/<string:collname>")
api.add_resource(FormData, "/FormData")

if __name__ == '__main__':
    app.run(debug=True)
