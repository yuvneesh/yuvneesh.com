from flask import Flask, render_template, request
from sootByFTIR import sootCalc

app = Flask(__name__)

#Adding secret key
f = open("secretKey.secret","r")
f2 = f.read()
app.config['SECRET_KEY'] = f2

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

@app.route("/calculateSoot", methods=['GET', 'POST'])
def calculateSoot():
    givenAbsorbance = float(request.get_json()["Absorbance"])
    calculatedSoot = (0.0156 * givenAbsorbance) + 0.0147
    return {"percentage": calculatedSoot}