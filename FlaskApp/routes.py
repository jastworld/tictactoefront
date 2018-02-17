from flask import  Flask, render_template, redirect, request, jsonify
from app import app
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import datetime
import simplejson as json
import json
import requests

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
@app.route('/getResult', methods=['POST'])
def getResult():
    print(request.form['grid'])
    data = json.loads(request.form['grid'])
    '''data  = request.json['grid']'''
    winner = checkwinner(data);
    if(winner!=""):
        return jsonify({'grid': data,'winner': winner})

    for i in range(0, 10):
        if (data[i] == ""):
            data[i] = "O"
            break
    return jsonify({'grid': data,'winner': checkwinner(data)})



@app.route('/ttt/play', methods=['POST'])
def play():
    data = request.json['grid']
    '''data  = request.json['grid']'''
    winner = checkwinner(data)
    if(winner!=""):
        return jsonify({'grid': data,'winner': winner})

    for i in range(0, 10):
        if (data[i] == ""):
            data[i] = "O"
            break
    winner = checkwinner(data)
    return jsonify({'grid': data,'winner': winner})




def checkwinner(game):
    i=0;
    '''check for horizontal winner'''
    while (i < 9):
        print("1: "+str(i))
        if game[i]==game[i+1] and game[i]==game[i+2]:
            if game[i]=="":
                break
            else:
                return game[i];
        i+=3

    i=0;
    '''Check for vertical winner'''
    while(i<3):
        print("2: "+str(i))
        if game[i]==game[i+3] and game[i]==game[i+6]:
            if game[i]=="":
                break
            else:
                return game[i]
        i+=1

    print(game[0])
    '''Diagonal winner'''
    if game[0]==game[4] and game[0]==game[8]:
        return game[0]
    if game[2]==game[4] and game[0]==game[6]:
        return game[2]


    return ""
