from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from datetime import date
import datetime
import calendar
from database import *

app = Flask(__name__) 


#begin testing
transaction_name1 = "Grocery"
amount1 = 100
category1 = "Food"
notes1 = "Shopped at Target"
types1 = "Cash"

transaction_name2 = "Salary"
amount2 = 200
category2 = "Work"
notes2 = "CA for course"
types2 = "Debit"

transaction_name3 = "Gift for bday"
amount3 = 500
category3 = "Gift"
notes3 = "Thanks Hamiz"
types3 = "Cash"

transaction_name4 = "Too much"
amount4 = 500
category4 = "Gift"
notes4 = "Return money to Hamiz"
types4 = "Checking"


#Spending/Income Transaction Objects
spend = Spend(transaction_name1, amount1, category1, notes1, types1)
income = Income(transaction_name2, amount2, category2, notes2, types2)
income2 = Income(transaction_name3, amount3, category3, notes3, types3)
spend2 = Spend(transaction_name4, amount4, category4, notes4, types4)

spend3 = Spend(transaction_name4, amount1, category1, notes1, types1)
person = Person("Jacob", {}, {}, 1000)

person.add_income(income, datetime.date(2022, 12, 1))
person.add_income(income2, datetime.date(2022, 12, 3))
person.add_income(income2, datetime.date(2022, 12, 5))
person.add_income(income2, datetime.date(2022, 12, 14))
person.add_income(income2, datetime.date(2022, 12, 31))
person.add_income(income2, datetime.date(2022, 12, 22))
person.add_income(income2, datetime.date(2022, 1, 3))
person.add_income(income2, datetime.date(2022, 1, 30))


person.add_spending(spend, datetime.date(2022, 12, 5))
person.add_spending(spend2, datetime.date(2022, 12, 15))
person.add_spending(spend3, datetime.date(2023, 1, 2))
person.add_spending(spend2, datetime.date(2022, 1, 15))
person.add_spending(spend3, datetime.date(2023, 1, 1))
#end of testing


@app.route('/')
def index():
    total_income = person.get_total_income()
    total_spending = person.get_total_spending() 
    total_balance =  person.get_total_difference()
    return render_template('index.html', total_income=total_income, total_spending = total_spending, total_balance = total_balance)

@app.route('/add_income', methods=['POST'])
def add_income():
    transaction_name = request.form['transaction_name']
    amount = float(request.form['amount'])
    category = request.form['category']
    notes = request.form['notes']
    types = request.form['types']
    date_input = request.form['date']
    
    date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    income_transaction = Income(transaction_name, amount, category, notes, types)
    person.add_income(income_transaction, date_object)
    
    return index()

@app.route('/add_spending', methods=['POST'])
def add_spending():
    transaction_name = request.form['transaction_name']
    amount = float(request.form['amount'])
    category = request.form['category']
    notes = request.form['notes']
    types = request.form['types']
    date_input = request.form['date']
    
    date_object = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    spend_transaction = Spend(transaction_name, amount, category, notes, types)
    person.add_spending(spend_transaction, date_object)
    
    return index()


@app.route('/trend_monthly_income', methods=['GET'])
def trend_monthly_income():
    trend_data = person.get_trend_monthly_income(12, 2022)
    return jsonify(trend_data.to_dict(orient='records'))

@app.route('/graph')
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    #person = Person("Jacob", {}, {}, 1000)
    app.run(debug=True)
