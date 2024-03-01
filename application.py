from flask import Flask, render_template, request
from sootByFTIR import sootCalc
from loginPage import loginForm
from authentication import UserManager
import json
import os

app = Flask(__name__)

#Adding secret key
app.config['SECRET_KEY'] = "jEXPcuXLDIUXbHROfl2CXIu9slYX5p6tf"
app.userManager = UserManager(r"./db.db")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/apps")
def apps():
    return render_template("apps.html")

@app.route("/sootByFTIR", methods=['GET','POST'])
def sootByFTIR():
    form = sootCalc()
    buttons = [form.calculate]
    fields = [form.Absorbance, form.Soot]

    return render_template("sootByFTIR.html", form=form, fields=fields, buttons=buttons)

@app.route("/calculateSoot", methods=['POST'])
def calculateSoot():
    givenAbsorbance = float(request.get_json()["Absorbance"])
    calculatedSoot = (0.0156 * givenAbsorbance) + 0.0147
    return {"percentage": calculatedSoot}

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = loginForm()
    buttons = [form.login]
    fields = [form.username, form.password]
        
    return render_template("login.html", form=form, fields=fields, buttons=buttons)

@app.route("/authenticate", methods=['POST'])
def authenticate():
    if app.userManager.validateCredentialsDummy(request.get_json()["username"], request.get_json()['password']):
        return json.dumps({"status": True})
    else:
        return json.dumps({"status": False})
