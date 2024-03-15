from flask import Flask
import datetime
 
x = datetime.datetime.now()

# Initializing flask app
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>RF Workshop Limted.</h1>"

@app.route('/chat')
def index():
    chat.py
    return "<h1>RF Workshop Limted.</h1>"

     
# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=True)