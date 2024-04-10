from flask import Flask, jsonify, render_template

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/api/v1.0/tasks', methods = ['GET'])
def ReturnJSON():
    return jsonify({'tasks': tasks})

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')
    

if __name__ == '__main__':
    app.run(debug=True)