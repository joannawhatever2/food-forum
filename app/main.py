from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/post')
def addapost():
  return render_template('post.html')

@app.route('/veggies')
def veggies():
  return render_template('veggies.html')

@app.route('/fruits')
def fruits():
  return render_template('fruits.html')

@app.route('/cookies')
def cookies():
  return render_template('cookies.html')

app.run(host='0.0.0.0', port=81)
