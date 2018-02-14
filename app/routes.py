from flask import  Flask, render_template, redirect, request
from app import app
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField


@app.route('/ttt/')
@app.route('/',methods = ['GET','POST'])
def index():
    user = {'username': 'miguel'}
    try:

        if request.method == "POST":
            name = request.form['name']
            print("The name is '" + name + "'")
        else:
            return render_template('index.html', title='Home', user=user)

    except Exception as e:
        print("Error")

    '''return redirect('/ttt')'''
