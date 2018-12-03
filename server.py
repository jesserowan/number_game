from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"
import random

@app.route('/')
def index():
    if "random" not in session:
        session['random'] = random.randint(1, 100)
    print(session['random'])
    return render_template('index.html')

@app.route('/guess', methods=["POST"])
def guess():
    if int(request.form['guess']) < session['random']:
        session['too_low'] = True
        session['too_high'] = False
        session['correct'] = False
        print("Too low!")
    elif int(request.form['guess']) > session['random']:
        session['too_high'] = True
        session['too_low']  = False
        session['correct'] = False
        print("Too high!")
    else:
        session['correct'] = True
        session['too_low'] = False
        session['too_high'] = False
        print("Correct!")
    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)