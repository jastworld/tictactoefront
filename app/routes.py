from flask import  Flask, render_template, redirect, request
from app import app
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import datetime

now = datetime.datetime.now()

@app.route('/ttt/')
@app.route('/',methods = ['GET','POST'])
def index():
    try:
        if request.method == "POST":
            name = request.form['name']
            return render_template('game.html', name=name, time = str(now))
        else:
            return render_template('index.html', title='Home')

    except Exception as e:
        print(name)
        return render_template('index.html', title='Home')

    '''return redirect('/ttt')'''
