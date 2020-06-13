# https://stackshare.io/stackups/flask-vs-sinatra#pros
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask
from flask import request
from flask import json
from flask import jsonify
from flask_cors import CORS
from cat import Cat

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/cats', methods=['GET', 'POST'])
def cats():
    if request.method == 'POST':
        cat_data = request.get_json()
        new_cat = Cat(cat_data['name'], cat_data['age'], cat_data['image'])
        print(Cat.all())
        return json.dumps(new_cat.__dict__)
    else:
        cats = Cat.all()
        cats_json = []
        for cat in cats:
            cats_json.append(json.dumps(cat.__dict__))
        return jsonify({"cats": cats_json})

app.run()