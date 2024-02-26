from ast import Sub
from tokenize import String
from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms import SubmitField

class sootCalc(FlaskForm):
    Absorbance = FloatField(label='Absorbance')
    Soot = FloatField('Soot %')

    calculate = SubmitField('Submit')