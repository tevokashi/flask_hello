from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Ola mundo!"

@app.route('/api/v1/status')
def service_status():
    return "Ola mundo2!"
