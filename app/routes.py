from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/sendUserData', methods = ['GET', 'POST'])
def sendUserData():
    if request.method == 'GET':
        return "You did not fill out the form!"
    else: 
        userInfo = dict(request.form)
        collegename = userInfo["collegename"]
        tuition = userInfo["tuition"]
        gradMonth = userInfo["gradMonth"]
        gradYear = userInfo["gradYear"]
        currentMonth = userInfo["currentMonth"]
        currentYear = userInfo["currentYear"]
        weeksleft = model.weeksLeft(gradYear, gradMonth, currentYear, currentMonth)
        saving = model.equation(weeksleft, tuition)
        return render_template("amount.html", collegename = collegename, tuition = tuition, gradMonth = gradMonth, gradYear = gradYear, currentMonth = currentMonth, currentYear = currentYear, weeksleft = weeksleft, saving = saving)


    