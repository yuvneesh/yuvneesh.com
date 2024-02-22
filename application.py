from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """render the homepage"""
    # return "<html><body><h1>Welcome to my app!</h1></body></html>\n"
    return render_template("home.html")