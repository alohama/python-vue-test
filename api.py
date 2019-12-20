from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify
from flask import request
from flask_cors import CORS

db_connect = create_engine('sqlite:///user.db')
app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resorces={r'/': {"origins": '*'}})
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("SELECT * FROM users;") # This line performs query and returns json result
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_ID(Resource):
    def get(self, user_id):
        conn = db_connect.connect()
        query = conn.execute("select * from users where id =%d "  %int(user_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, first_name):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users where first_name like '%"+first_name+"%'")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_LastName(Resource):
    def get(self, last_name):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users where last_name like '%"+last_name+"%'")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Email(Resource):
    def get(self, email):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users where email like '%"+email+"%'")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Age(Resource):
    def get(self, age):
        string = age.split("-")
        print(len(string))
        if len(string) == 1:
            querySQL = "SELECT * FROM users WHERE age = "+string[0]
        if len(string) == 2:
            querySQL = "SELECT * FROM users WHERE age BETWEEN "+string[0]+" AND "+string[1]
        conn = db_connect.connect()
        query = conn.execute(querySQL)
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Gender(Resource):
    def get(self, gender):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM users where gender = '"+gender+"'")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Delete(Resource):
    def delete(self, userID):
        conn = db_connect.connect()
        conn.execute("DELETE FROM users where id = "+userID)
        return "success"

class Employees_Update(Resource):
    def post(self):
        userID = request.form.get('userID')
        conn = db_connect.connect()
        if request.form.get('gender'):
            conn.execute("UPDATE users SET gender = '"+request.form.get('gender')+"' WHERE id = "+userID)
        if request.form.get('fname'):
            conn.execute("UPDATE users SET first_name = '"+request.form.get('fname')+"' WHERE id = "+userID)
        if request.form.get('lname'):
            conn.execute("UPDATE users SET last_name = '"+request.form.get('lname')+"' WHERE id = "+userID)
        if request.form.get('email'):
            conn.execute("UPDATE users SET email = '"+request.form.get('email')+"' WHERE id = "+userID)
        if request.form.get('age'):
            conn.execute("UPDATE users SET age = "+request.form.get('age')+" WHERE id = "+userID)
        
        return "success"
        

api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Employees_ID, '/employeeByID/<user_id>') # Route_3
api.add_resource(Employees_Name, '/employeeByName/<first_name>') # Route_3
api.add_resource(Employees_LastName, '/employeeByLastName/<last_name>') # Route_3
api.add_resource(Employees_Email, '/employeeByEmail/<email>') # Route_3
api.add_resource(Employees_Age, '/employeeByAge/<age>') # Route_3
api.add_resource(Employees_Gender, '/employeeByGender/<gender>') # Route_3
api.add_resource(Employees_Update, '/employeeUpdate') # Route_3
api.add_resource(Employees_Delete, '/employeeDelete/<userID>') # Route_3

if __name__ == '__main__':
     app.run(host='localhost',port='5002')