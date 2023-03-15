import numpy as np
import pandas as pd
from datetime import date
import datetime
import calendar


#Where we store a person's income dictionary and spending dictionary
#Each Dictionary consists of a dictionary of lists, with keys as dates
#Able to append and access values for spending/income based on date
#Also manages limits on spending based on income
class Person:
    def __init__(self,name, income, spend = 0, monthlyIncome = 0.0 ):
        self.name = name
        self.income = {} 
        self.spend = {}
        self.needlimit = 0.5*monthlyIncome
        self.wantlimit = 0.3*monthlyIncome
        self.monthly_income = monthlyIncome
    
    
#Income and Spending functions
#2022-12-27  ----- example of date from date.today

# This will take in the current month and year and return the monthly income for it
    def get_total_monthly_income(self, month = datetime.datetime.now().strftime("%B"), year = datetime.datetime.now().year):
        monthly = 0
        num_days = calendar.monthrange(year, month)[1]
        for i in range (1, num_days):
            temp = datetime.date(year, month, i)
            if (temp in self.income):
                income_list = self.income[temp]
                for i in range(0, len(income_list)):
                    monthly += income_list[i].amount
        return(monthly)

# This will take in the current month and year and return a dataframe for the monthly trend

    def get_trend_monthly_income(self, month = datetime.datetime.now().strftime("%B"), year = datetime.datetime.now().year):
        monthly = 0 
        num_days = calendar.monthrange(year, month)[1]
        
        #days = [datetime.date(year, month, day) for day in range (1, num_days+1)]
        income_days = []
        days = []

        for i in range (1, num_days+1):
            temp = datetime.date(year, month, i)
            if (temp in self.income):
                income_list = self.income[temp]
                for j in range(0, len(income_list)):
                    monthly += income_list[j].amount
                income_days.append(monthly)
                days.append(i)
        trend = pd.DataFrame({'Days': days, 'Income': income_days})
        return(trend)
    
    def get_trend_yearly_income(self, year = datetime.datetime.now().year):
        income_monthly = []
        month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        month_with_income = []

        for i in range(12):
            
            monthly_income = self.get_total_monthly_income(i + 1, year)
            if (monthly_income != 0):
                income_monthly.append(monthly_income)
                month_with_income.append(month[i])
                
        
        trend = pd.DataFrame({'Month': month_with_income, 'Income': income_monthly})
        return(trend)
    
# Returns 
    def get_trend_monthly_spend(self, month = datetime.datetime.now().strftime("%B"), year = datetime.datetime.now().year):
        monthly = 0 
        num_days = calendar.monthrange(year, month)[1]
        
        #days = [datetime.date(year, month, day) for day in range (1, num_days+1)]
        spend_days = []
        days = []

        for i in range (1, num_days+1):
            temp = datetime.date(year, month, i)
            if (temp in self.spend):
                spend_list = self.spend[temp]
                for j in range(0, len(spend_list)):
                    monthly += spend_list[j].amount
                spend_days.append(monthly)
                days.append(i)
        trend = pd.DataFrame({'Days': days, 'Spending': spend_days})
        return(trend)

# Returns a dataframe containing difference between spending and income in a month, used in monthly trend
    def get_trend_monthly_difference(self, month = datetime.datetime.now().strftime("%B"), year = datetime.datetime.now().year):
        monthly = 0 
        num_days = calendar.monthrange(year, month)[1]
        
        #days = [datetime.date(year, month, day) for day in range (1, num_days+1)]
        dif_days = []
        days = []
        income_check = False
        spend_check = False
        for i in range (1, num_days+1):
            temp = datetime.date(year, month, i)
            if (temp in self.spend):
                spend_list = self.spend[temp]
                for j in range(0, len(spend_list)):
                    monthly -= spend_list[j].amount
                income_check = True
            if (temp in self.income):
                income_list = self.income[temp]
                for j in range(0, len(income_list)):
                    monthly += income_list[j].amount
                spend_check = True
            if (spend_check or income_check):
                dif_days.append(monthly)
                days.append(i)
            income_check = False
            spend_check = False
        trend = pd.DataFrame({'Days': days, 'Difference': dif_days})
        return(trend)

        

#Remove Transaction from Income from certain day if it exists
    def delete_income(self, transaction, dates = date.today()):
        if (dates in self.income) and (transaction in self.income[dates]):
            self.income[dates].remove(transaction)
        
#Remove Transaction from Spend from certain day if it exists
    def delete_spending(self, transaction, dates = date.today()):
        if (dates in self.spend) and (transaction in self.spend[dates]):
            self.spend[dates].remove(transaction)

# This will take in the current month and year and return the monthly spend for it    
    def get_total_monthly_spending(self, month = datetime.datetime.now().strftime("%B"), year = datetime.datetime.now().year):
        monthly = 0
        for i in range (1, 31):
            temp = datetime.date(year, month, i)
            if (temp in self.spend):
                spend_list = self.spend[temp]
                for i in range(0, len(spend_list)):
                    monthly += spend_list[i].amount
        return(monthly)

# This will take in the current month, year and the category for which we need to find the monthly spend for and returns the monthly spend for the category    
    def get_categorical_monthly_spending(self, category, month = datetime.datetime.now().strftime("%B"), year = datetime.datetime.now().year):
        monthly = 0
        for i in range (1, 31):
            temp = str(year) + "-" + str(month) + "-" + str(i)
            if (temp in self.spend):
                spend_list = self.spend[temp]
                for i in range(0, len(spend_list)):
                    if (spend_list[i].category == category):
                        monthly += spend_list[i].amount
        return(monthly)

# This takes in an object of class income and appned it to the list of values in the dictionary with todays date as the key               
    def add_income(self, transaction, dates = date.today()):
        if dates in self.income:
            self.income[dates].append(transaction)
        else:
            self.income[dates] = [transaction]

# # This takes in an object of class spend and appned it to the list of values in the dictionary with todays date as the key      
    def add_spending(self, transaction, dates = date.today()):
        # if (transaction.amount + self.get_total_monthly_spending()) > self.wantlimit:
        #     print("Spending over Want Limit")
        # elif (transaction.amount + self.get_total_monthly_spending()) > self.needlimit:
        #     print("Spending over Need Limit")
        
        if dates in self.spend:
            self.spend[dates].append(transaction)
        else:
            self.spend[dates] = [transaction]

# This will return the total life income of the person    
    def get_total_income(self):
        total_income = 0.0
        for i in self.income:
            income_list = self.income[i]
            for j in range(0, len(income_list)):
                total_income += income_list[j].amount
        return(total_income)

# This will return the total income for today
    def get_day_total_income(self, dates = date.today()):
        if (self.income.get(dates) is None):
            return 0
        income_list = self.income[dates]
        total_income = 0.0
        for i in range(0, len(income_list)):
            total_income += income_list[i].amount
        return(total_income)

# This will return the total life spending of the person    
    def get_total_spending(self):
        total_spend = 0.0
        for i in self.spend:
            spend_list = self.spend[i]
            for j in range(0, len(spend_list)):
                total_spend += spend_list[j].amount
        return(total_spend)

# This will return the total spend of today for the person
    def get_day_total_spending(self, dates = date.today()):
        if (self.spend.get(dates) is None):
            return 0
        spend_list = self.spend[dates]
        total_spend = 0.0
        for i in range(0, len(spend_list)):
            total_spend -= spend_list[i].amount
        return(total_spend)

# This will return the difference in the life income and spend of the person
    def get_total_difference(self):
        total = 0
        total += self.get_total_income()
        total -= self.get_total_spending()
        return(total)

# This will return the difference in todays income and spend of the person        
    def get_day_total_difference(self, dates = date.today()):
        total = 0,0
        total += self.get_day_total_income()
        total -= self.get_day_total_income()
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


# Testing Functions
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

