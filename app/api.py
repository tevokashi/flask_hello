"""basic flask api
"""
from os import environ
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

redis_url = environ.get('REDISTOGO_URL')
try:
    r = redis.from_url(redis_url)
    redis_status = 'OK'
except:
    redis_status = 'Down'

@app.errorhandler(404)
def not_found():
    message = {
        'status' : 404,
        'message': 'Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

def test_db():
    """ Check database connection

    Returns:
        [string] -- database status
    """
    try:
        db.session.query("1").all()
        return 'OK'
    except:
        return 'Down'

@app.route('/')
def index():
    """Hello World

    Returns:
        [string] -- Ola mundo
    """
    return "Ola mundo!"

@app.route('/api/v1/enqueue')
def funcname():
    """Adiciona uma soma na fila

    Arguments:
        parameter_list {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    if redis_status == 'OK':
        return f"job enqueued{redis_status}"
    else:
        return "Redis is down unable to enqueue your job"

@app.route('/api/v1/status')
def service_status():
    """Check all api deps:
    db-sql, redis and queue

    Returns:
        [dict] -- API version, status of everyone of the deps
    """
    data = {}
    data['API'] = {}
    data['API']['api'] = "1.0"
    data['API']['dep'] = {}
    data['API']['dep']['db-sql'] = test_db()
    data['API']['dep']['db-nosql'] = redis_status
    resp = jsonify(data)
    resp.status_code = 200
    return resp

if __name__ == '__main__':
    app.run(debug=False)
