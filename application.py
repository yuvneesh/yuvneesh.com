from flask import Flask, render_template, request, url_for
from sootByFTIR import sootCalc
from loginPage import loginForm
from authentication import UserManager
import json
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

#Adding secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.userManager = UserManager(os.getenv('LOGIN_APP_CONNECTION_STRING'))

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

    return render_template("apps/sootByFTIR.html", form=form, fields=fields, buttons=buttons)

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
        
    return render_template("apps/login.html", form=form, fields=fields, buttons=buttons)

@app.route("/authenticate", methods=['POST'])
def authenticate():
    try:
        if app.userManager.validateCredentials(request.get_json()["username"], request.get_json()['password']):
            return json.dumps({"status": True})
        else:
            return json.dumps({"status": False})
    except UserManager.UserNotFound:
            return json.dumps({"status": False})
    
@app.route("/blogs", methods=['GET', 'POST'])
def blogs():
    return render_template("blogs.html")

@app.route("/blogs/<id>", methods=['GET', 'POST'])
def testBlog(id:int):
    #return f"{id}"
    return render_template(f'blogs/{id}.html')