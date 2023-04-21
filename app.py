from flask import Flask, render_template, request, jsonify
import numpy as np
import pandas as pd
from datetime import date
import datetime
import calendar
from database import *

app = Flask(__name__) 


spend = Spend("Groceries", 200, "Groceries", "", "Debit")
spend2 = Spend("Rent", 600, "Rent", "", "Debit")
spend3 = Spend("Party", 200, "Party", "", "Debit")
spend4 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend5 = Spend("Rent", 600, "Rent", "", "Debit")
spend6 = Spend("Party", 200, "Party", "", "Debit")
spend7 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend8 = Spend("Rent", 600, "Rent", "", "Debit")
spend9 = Spend("Party", 200, "Party", "", "Debit")
spend10 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend11 = Spend("Rent", 600, "Rent", "", "Debit")
spend12 = Spend("Party", 200, "Party", "", "Debit")
spend13 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend14 = Spend("Rent", 600, "Rent", "", "Debit")
spend15 = Spend("Party", 200, "Party", "", "Debit")
spend16 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend17 = Spend("Rent", 600, "Rent", "", "Debit")
spend18 = Spend("Party", 200, "Party", "", "Debit")
spend19 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend20 = Spend("Rent", 600, "Rent", "", "Debit")
spend21 = Spend("Party", 200, "Party", "", "Debit")
spend22 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend23 = Spend("Rent", 600, "Rent", "", "Debit")
spend24 = Spend("Party", 200, "Party", "", "Debit")
spend25 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend26 = Spend("Rent", 600, "Rent", "", "Debit")
spend27 = Spend("Party", 200, "Party", "", "Debit")
spend28 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend29 = Spend("Rent", 600, "Rent", "", "Debit")
spend30 = Spend("Party", 200, "Party", "", "Debit")
spend31 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend32 = Spend("Rent", 600, "Rent", "", "Debit")
spend33 = Spend("Party", 200, "Party", "", "Debit")
spend34 = Spend("Groceries", 200, "Groceries", "", "Debit")
spend35 = Spend("Rent", 600, "Rent", "", "Debit")
spend36 = Spend("Party", 200, "Party", "", "Debit")

spend37 = Spend("Car Damanges", 400, "Car", "", "Debit")
spend38 = Spend("Ticket", 200, "Ticket", "", "Debit")
spend39 = Spend("Doctor", 500, "Health", "", "Debit")


person = Person("Jacob", {}, {}, 1200)

income = Income("Work", 1400, "Work", "", "Debit")
income2 = Income("Work", 1400, "Work", "", "Debit")
income3 = Income("Work", 1400, "Work", "", "Debit")
income4 = Income("Work", 1400, "Work", "", "Debit")
income5 = Income("Work", 1400, "Work", "", "Debit")
income6 = Income("Work", 1400, "Work", "", "Debit")
income7 = Income("Work", 1400, "Work", "", "Debit")
income8 = Income("Work", 1400, "Work", "", "Debit")
income9 = Income("Work", 1400, "Work", "", "Debit")
income10 = Income("Work", 1400, "Work", "", "Debit")
income11 = Income("Work", 1400, "Work", "", "Debit")
income12 = Income("Work", 1400, "Work", "", "Debit")


income17 = Income("Birthday", 200, "Gift", "", "Cash")
income18 = Income("Raffle", 20, "Gift", "", "Venmo")
income19 = Income("Fantasy Football", 50, "Gift", "", "Venmo")
income20 = Income("March Madness", 75, "Gift", "", "Venmo")
income21 = Income("Christmas", 100, "Gift", "", "Cash")



person.add_income(income, datetime.date(2022, 1, 1))
person.add_income(income2, datetime.date(2022, 2, 1))
person.add_income(income3, datetime.date(2022, 3, 1))
person.add_income(income4, datetime.date(2022, 4, 3))
person.add_income(income5, datetime.date(2022, 5, 1))
person.add_income(income6, datetime.date(2022, 6, 3))
person.add_income(income7, datetime.date(2022, 7, 1))
person.add_income(income8, datetime.date(2022, 8, 3))
person.add_income(income9, datetime.date(2022, 9, 1))
person.add_income(income10, datetime.date(2022, 10, 3))
person.add_income(income11, datetime.date(2022, 11, 1))
person.add_income(income12, datetime.date(2022, 12, 3))
person.add_income(income17, datetime.date(2022, 6, 20))
person.add_income(income18, datetime.date(2022, 8, 15))
person.add_income(income19, datetime.date(2022, 3, 15))
person.add_income(income20, datetime.date(2022, 3, 7))
person.add_income(income21, datetime.date(2022, 12, 25))




person.add_spending(spend, datetime.date(2022, 1, 10))
person.add_spending(spend2, datetime.date(2022, 1, 15))
person.add_spending(spend3, datetime.date(2022, 1, 17))
person.add_spending(spend4, datetime.date(2022, 2, 20))
person.add_spending(spend5, datetime.date(2022, 2, 15))
person.add_spending(spend6, datetime.date(2022, 2, 17))
person.add_spending(spend7, datetime.date(2022, 3, 10))
person.add_spending(spend8, datetime.date(2022, 3, 15))
person.add_spending(spend9, datetime.date(2022, 3, 17))
person.add_spending(spend10, datetime.date(2022, 4, 10))
person.add_spending(spend11, datetime.date(2022, 4, 15))
person.add_spending(spend12, datetime.date(2022, 4, 17))
person.add_spending(spend13, datetime.date(2022, 5, 10))
person.add_spending(spend14, datetime.date(2022, 5, 15))
person.add_spending(spend15, datetime.date(2022, 5, 17))
person.add_spending(spend16, datetime.date(2022, 6, 10))
person.add_spending(spend17, datetime.date(2022, 6, 15))
person.add_spending(spend18, datetime.date(2022, 6, 17))
person.add_spending(spend19, datetime.date(2022, 7, 10))
person.add_spending(spend20, datetime.date(2022, 7, 15))
person.add_spending(spend21, datetime.date(2022, 7, 17))
person.add_spending(spend22, datetime.date(2022, 8, 10))
person.add_spending(spend23, datetime.date(2022, 8, 15))
person.add_spending(spend24, datetime.date(2022, 8, 17))
person.add_spending(spend25, datetime.date(2022, 9, 10))
person.add_spending(spend26, datetime.date(2022, 9, 15))
person.add_spending(spend27, datetime.date(2022, 9, 17))
person.add_spending(spend28, datetime.date(2022, 10, 10))
person.add_spending(spend29, datetime.date(2022, 10, 15))
person.add_spending(spend30, datetime.date(2022, 10, 17))
person.add_spending(spend31, datetime.date(2022, 11, 10))
person.add_spending(spend32, datetime.date(2022, 11, 15))
person.add_spending(spend33, datetime.date(2022, 11, 17))
person.add_spending(spend34, datetime.date(2022, 12, 10))
person.add_spending(spend35, datetime.date(2022, 12, 15))
person.add_spending(spend36, datetime.date(2022, 12, 17))
person.add_spending(spend37, datetime.date(2022, 10, 27))
person.add_spending(spend38, datetime.date(2022, 2, 9))
#end of testing

# index.html routes

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

@app.route('/api/income/<int:year>', methods=['GET'])
def get_yearly_income_by_cat(year):
    yearly_income = person.get_yearly_income_by_category(year)
    return jsonify(yearly_income)

@app.route('/api/spend/<int:year>', methods=['GET'])
def get_yearly_spend_by_cat(year):
    yearly_income = person.get_yearly_spend_by_category(year)
    return jsonify(yearly_income)

# graph.html routes

@app.route('/trend_monthly_income/<int:year>/<int:month>', methods=['GET'])
def trend_monthly_income(year, month):
    trend_data = person.get_trend_monthly_income(month, year)
    return jsonify(trend_data.to_dict(orient='records'))


@app.route('/trend_yearly_income/<int:year>', methods=['GET'])
def trend_yearly_income(year):
    trend_data = person.get_trend_yearly_income(year)
    return jsonify(trend_data.to_dict(orient='records'))


@app.route('/trend_monthly_spend/<int:year>/<int:month>', methods=['GET'])
def trend_monthly_spend(year, month):
    trend_data = person.get_trend_monthly_spend(month, year)
    return jsonify(trend_data.to_dict(orient='records'))

@app.route('/trend_yearly_spend/<int:year>', methods=['GET'])
def trend_yearly_spend(year):
    trend_data = person.get_trend_yearly_spend(year)
    return jsonify(trend_data.to_dict(orient='records'))



@app.route('/trend_monthly_diff/<int:year>/<int:month>', methods=['GET'])
def trend_monthly_difference(year, month):
    trend_data = person.get_trend_monthly_difference(month, year)
    return jsonify(trend_data.to_dict(orient='records'))


@app.route('/graph', methods=['POST'])
def graph():
    return render_template('graph.html')

@app.route('/cat', methods=['GET'])
def cat():
    return render_template('cat.html')


@app.route('/income', methods=['GET'])
def incomePage():
    return render_template('income.html')

@app.route('/spending', methods=['GET'])
def spendingPage():
    return render_template('spending.html')
if __name__ == '__main__':
    app.run(debug=True)
