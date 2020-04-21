from flask import Flask, jsonify

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status' : 404,
            'message': 'Not Found'
    }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

@app.route('/')
def index():
    return "Ola mundo!"

@app.route('/api/v1/status')
def service_status():
    return "Ola mundo2!"

if __name__ == '__main__':
    app.run(debug=False)