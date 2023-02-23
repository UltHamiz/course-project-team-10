import numpy as np
from datetime import date


#Where we store a person's income dictionary and spending dictionary
#Each Dictionary consists of a dictionary of lists, with keys as dates
#Able to append and access values for spending/income based on date
class Person:
    def __init__(self,name, income, spend = 0):
        self.name = name
        self.income = {} 
        self.spend = {}

    
    
#Income and Spending functions
#2022-12-27  ----- example of date from date.today
    def add_income(self, transaction, dates = date.today):
        if dates in self.income:
            self.income[dates].append(transaction)
        else:
            self.income[dates] = [transaction]
        
    def add_spending(self, transaction, dates = date.today):
        if dates in self.spend:
            self.spend[dates].append(transaction)
        else:
            self.spend[dates] = [transaction]
        
    def get_total_income(self, dates = date.today):
        income_list = self.income[dates]
        total_income = 0.0
        for i in range(0, len(income_list)):
            total_income += income_list[i].amount
        return(total_income)

    def get_total_spending(self, dates = date.today):
        spend_list = self.spend[dates]
        total_spend = 0.0
        for i in range(0, len(spend_list)):
            total_spend -= spend_list[i].amount
        return(total_spend)

    def get_total_difference(self, dates = date.today):
        income_list = self.income[dates]
        spend_list = self.spend[dates]
        total = 0.0
        for i in range(0, len(income_list)):
            total += income_list[i].amount
        for i in range(0, len(spend_list)):
            total -= spend_list[i].amount
        return(total)
    
#Income Class
#transaction_name is the name of the transaction
#amount is the amount of the transaction
#category is what the income is from (job, relative, gift)
#notes is any side notes the user would like to add
#type is the type of money it is (Cash, Credit, Debit)
class Income():
    def __init__(self, transaction_name, amount, category, notes, types):
        self.transaction_name = transaction_name
        self.amount = amount
        self.category = category
        self.notes = notes
        self.type = types

    def assign_name(self, _name):
        self.name = _name

#Spend Class
#transaction_name is the name of the transaction
#amount is the amount of the transaction
#category is what the spending is from (job, relative, gift)
#notes is any side notes the user would like to add
#type is the type of money it is (Cash, Credit, Debit)     
class Spend():
    def __init__(self, transaction_name, amount, category, notes, types):
        self.transaction_name = transaction_name
        self.amount = amount
        self.category = category
        self.notes = notes
        self.type = types




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

spend = Spend(transaction_name1, amount1, category1, notes1, types1)
income = Income(transaction_name2, amount2, category2, notes2, types2)
income2 = Income(transaction_name3, amount3, category3, notes3, types3)
spend2 = Spend(transaction_name4, amount4, category4, notes4, types4)
person = Person("Jacob", {}, {})

person.add_income(income)
person.add_income(income2)
person.add_spending(spend)
person.add_spending(spend2)
print("helloworld")
print("Income: ",person.get_total_income())
print("Spending: ",person.get_total_spending())
print("Balance: ", person.get_total_difference())