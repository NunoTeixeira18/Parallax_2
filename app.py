from flask import Flask, render_template, redirect, request, session
from flask_session import Session

import jinja2

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
