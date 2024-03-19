from flask import Flask
from flask_restful import reqparse, Api, Resource


# Initializing flask app
app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')
class Message(Resource):
    def get(self):
        return {"message": 'Hello World'}
api.add_resource(Message, '/api/hello')

@app.route('/chat')
def index():
    chat.py
    return "<h1>RF Workshop Limted.</h1>"

     
# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=True)