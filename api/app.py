from flask import Flask, jsonify
from datetime import datetime
import datetime
from database import Person, Income, Spend

app = Flask(__name__)

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
person.add_spending(spend2, datetime.date(2022, 1, 15))
print("Income: ",person.get_total_income())
print("Monthly December Income: ", person.get_total_monthly_income(12, 2022))
print("Spending: ",person.get_total_spending()) 
print("Balance: ", person.get_total_difference())
print(person.get_trend_monthly_income(12, 2022))
print(person.get_trend_monthly_income(1, 2022))
print(person.get_trend_yearly_income(2022))
print(person.get_trend_monthly_spend(12, 2022))
print(person.get_trend_monthly_spend(1, 2022))


person.delete_income(income, datetime.date(2022, 12, 1))
print(person.get_trend_monthly_income(12, 2022))
person.delete_income(spend, datetime.date(2022, 12, 5))
print(person.get_trend_monthly_spend(12, 2022))
print(person.get_trend_yearly_income(2022))
print(person.get_trend_monthly_difference(12, 2022))

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/income')
def get_monthly_income():
    trend = person.get_trend_monthly_income(12,2022)
    return trend.to_json(orient='records')

if __name__ == '__main__':
    app.run()