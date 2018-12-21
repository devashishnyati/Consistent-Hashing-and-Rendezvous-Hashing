from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
import sys

port_number = sys.argv[1]

app = Flask(__name__)
api = Api(app)

DATA_STORE = {
    'num_entries': 0,
    'entries': []
}

# parser = reqparse.RequestParser()
# parser.add_argument('hash_key', type=str, help='hash key')
# parser.add_argument('hash_value', type=str, help='hash value')

class Server(Resource):
    def get(self):
        return DATA_STORE

    def post(self):
        #request.get_json()
        #args = parser.parse_args()
        DATA_STORE['num_entries']=DATA_STORE['num_entries']+1
        DATA_STORE['entries'].append(request.get_json(force=True))
        return DATA_STORE, 201

api.add_resource(Server, '/api/v1/entries')



if __name__ == '__main__':
    app.run(port= port_number,debug=True)