from app import app
from flask import render_template, request
from app.models import model, formopener

import os
from app import app

from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = 'tuitionapp' 

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:wONmnr26uAo5Nz6A@cluster0-tqevt.mongodb.net/tuitionapp?retryWrites=true&w=majority' 

mongo = PyMongo(app)


@app.route('/')
@app.route('/calculator')
def home():
    return render_template('index.html')
@app.route('/index')
def index():
    return render_template('home.html')

# @app.route('/add')
# def add():
#     # connect to the database
#     user = mongo.db.users

#     # insert new data
#     user.insert({'name':'Lisette', 'age':17})

#     # return a message to the user
#     return "User has been added!"



@app.route('/sendUserData', methods = ['GET', 'POST'])
def sendUserData():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        global collegename, tuition, fullName, gradMonth, gradYear, currentMonth, currentYear, weeksleft, saving
        userInfo = dict(request.form)
        collegename = userInfo["collegename"]
        tuition = userInfo["tuition"]
        fullName = userInfo["fullName"]
        gradMonth = userInfo["gradMonth"] 
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        schoolinfo = mongo.db.schoolinfo
        schoolinfo.insert({'collegename':collegename, 'tuition':int(tuition), 'gradYear':int(gradYear)})
        users = mongo.db.users
        users.insert({'fullName': fullName, 'gradMonth': gradMonth, 'gradYear': gradYear, 'currentMonth': currentMonth, 'currentYear': currentYear, 'weeksleft': weeksleft, 'saving': saving})
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving, fullName = fullName)
 
@app.route('/aidPage')
def aidPage():
    return render_template('aid.html')

@app.route('/aid', methods = ['GET', 'POST'])
def aid():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else:
        newContribution = dict(request.form)
        contribution = newContribution["contribution"]
        print("Contribution = " + contribution)
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        extraMoney = model.neededAid(tuition, weeksleft, contribution)
        return render_template("newCost.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, contribution = contribution, extraMoney = extraMoney)
        
        
    