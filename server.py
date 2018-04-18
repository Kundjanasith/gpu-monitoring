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

@app.route("/data60")
def data60():
    f = open("data.csv","r")
    lines = f.readlines()
    res = "x"
    print(len(lines))
    if len(lines) < 60:
       res = lines[1:len(lines)]
    else:
       res = lines[len(lines)-59:len(lines)]
    content = ""
    for i in res:
        content = content + i
    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=31919)
