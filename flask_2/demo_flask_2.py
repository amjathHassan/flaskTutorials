from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/phone/<name>')
def phone(name):
    return render_template('temp_var.html', name= name)

@app.route('/adv_phone/<name>')
def adv_phone(name):
    letters = list(name)
    phone_dict = {
        'brand': 'apple',
    }

    return render_template('temp_var.html', name = name, mylist = letters, mydict = phone_dict)

if __name__ == '__main__':
    app.run(debug= True)