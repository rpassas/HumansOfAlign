import os
from flask import Flask, render_template, request, redirect
import urllib.request

app=Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home() : 
	return render_template("index.html")

if __name__ == "__main__":
	app.run(debug=True)