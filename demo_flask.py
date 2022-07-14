from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World changed</h1>"

# @app.route('/information')
# def info():
#     return '<h1>New Page</h1>'

# @app.route('/puppy/<name>')
# def puppy(name):
#     return f'<h1>{name} is aa good dog</h1>'

@app.route('/word/<item>')
def word_change(item):
    new_word = item[0: len(item)-1]
    if item[-1] == 'y':
        return f'<h1>{new_word}ifull</h1>'
    else:
        return f'<h1>{new_word}y</h1>'


if __name__ == "__main__":
    app.run(debug= True)
    