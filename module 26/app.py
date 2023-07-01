from flask import Flask, request

sr = Flask(__name__)
database = {'sabbir': '100', "sadia" : "32", 'salman': '23'}

@sr.route('/', methods = ['GET'])
def home():
    return "<h1>wellcome to my API</h1>"



@sr.route('/getdatabase', methods = ['GET'])
def get_detabase():
    return database


@sr.route('/adddata', methods = ['PUT'])
def add_data():
    kye, value = list(request.args.items())[0]
    database[kye] = value
    return(f'{kye} added value = {value} kye = {kye}')


@sr.route('/deletedata', methods = ['DELETE'])
def delete_data():
    for users in database:
        kye, value = list(request.args.items())[0]
        if users in value:
                database.pop(value)
                return(f'{value} Deleted')
        else:
            return "Name not found"



if __name__ == '__main__':
    sr.run()
    
