from flask import Flask, render_template
import time


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("hello.html")


@app.route("/normal")
def normal():
    return render_template("normal.html")


@app.route("/slow")
def slow():
    time.sleep(5)
    return "<div id='slow-results'>this was slow!</div>"
