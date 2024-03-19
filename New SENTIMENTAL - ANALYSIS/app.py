from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/registation')
def registation():
    return render_template('registation.html')

if __name__ =='_main_':
    app.run(debug=True)