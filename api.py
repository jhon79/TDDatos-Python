from flask import Flask, request, Response
from queryfun import get_company_information
import requests
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/api/yahoo')
def get_company():
    #symbol = "DIS"
    symbol = request.args.get('ticker')
    if symbol is None:
        return Response(json.dumps({"error": "missing 'ticker' query-parameter"}), status=400, mimetyp='application/json')
    return Response(json.dumps(get_company_information(symbol)),status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run()