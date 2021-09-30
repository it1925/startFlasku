from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def ahoj():
    return "Deaz NUTS!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    pole = ["jedna","dve","tri"]
    return render_template('script.html', name=name, pole=pole)