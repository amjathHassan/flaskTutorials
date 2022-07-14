from tokenize import Number
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('form_index.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup_form.html')

@app.route('/thankyou')
def thankyou():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    return render_template('thankyou.html', fname= first_name, lname = last_name)

@app.route('/work_form')
def work_form():
    return render_template('work_form_page.html')

import re

@app.route('/work_thankyou')
def work_thankyou():
    user_name = request.args.get('user_name')
    password = request.args.get('password')
    confirm_password = request.args.get('confirm_password')
    user_name_lower_status = 'Username should contain at least one lowercase character'
    user_name_upper_status = 'Username should contain at least one uppercase character'
    user_name_last_digit_status = 'Last character of username should be a number'
    password_match_status = "Passwords didn't match, Please confirm again"
    
    if not(re.search('[a-z]', user_name)):
        return render_template('custom_error.html', error_status= user_name_lower_status)
    
    elif not(re.search('[A-Z]', user_name)):
        return render_template('custom_error.html', error_status= user_name_upper_status)
    
    elif not(re.search('[0-9]', user_name[-1])):
        return render_template('custom_error.html', error_status= user_name_last_digit_status)
    elif password != confirm_password:
        return render_template('custom_error.html', error_status= password_match_status)
    else:
        return render_template('work_thankyou.html', user_name= user_name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404 

if __name__ == "__main__":
    
    app.run(debug= True)

