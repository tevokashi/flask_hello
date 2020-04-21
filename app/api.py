from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status' : 404,
            'message': 'Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

def test_db():
    try:
        db.session.query("1").all()
        return 'OK'
    except Exception as e:
        return 'Down'

@app.route('/')
def index():
    return "Ola mundo!"

@app.route('/api/v1/status')
def service_status():
    data = {}
    data['API'] = {}
    data['API']['api'] = "1.0"
    data['API']['dep'] ={}
    data['API']['dep']['db-sql'] = test_db()
    return jsonify(data)
    
if __name__ == '__main__':
    app.run(debug=False)