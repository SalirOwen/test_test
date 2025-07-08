from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello,全世界!</h1>"

@app.route("/name")
def name():
    return "<h1>您好, 這是name的頁面!</h1>"