from flask import Flask, request, jsonify, send_from_directory
import os
import requests
import json
import datetime
import json
import secrets
import string

app = Flask(__name__, static_folder=".", template_folder=".")

@app.after_request
def add_headers(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization, data')
    return response


@app.route("/")
def home():
    return "GPU MONITORING"

@app.route("/data")
def data():
    return send_from_directory(".","data.csv")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31919)
