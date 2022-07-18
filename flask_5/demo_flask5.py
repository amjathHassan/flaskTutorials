from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import ( StringField, BooleanField, RadioField, TextAreaField, SubmitField, SelectField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

class InfoForm(FlaskForm):
    pet = StringField('Pet Type :', validators= [DataRequired()])
    vaccinated = BooleanField('Is it vaccinated : ')
    gender = RadioField('Please pick your choice of gender :', choices=[('M', 'male'), ('F', 'female')])
    food_choice = SelectField('Pick your favorite food : ', choices= [('NV', 'Non Veg'), ('v', 'Veg'), ('NA', 'Not An Issue')])

    feedBack = TextAreaField()
    submit = SubmitField('submit')

@app.route('/', methods = ['POST', 'GET'])
def homepage():
    form = InfoForm()

    if form.validate_on_submit():

        session['pet'] = form.pet.data
        session['vaccinated'] = form.vaccinated.data
        session['gender'] = form.gender.data
        session['food_choice'] = form.food_choice.data
        session['Feedback'] = form.feedBack.data

        return redirect(url_for('thankyou'))
    
    return render_template('homepage.html' , form = form)
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')



if __name__ == '__main__' : 
    app.run(debug= True)