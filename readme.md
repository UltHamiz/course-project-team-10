
Personal Finance App

Project Introduction

- Personal Finace App centered around Budget Tracking for College Students, Allows for maintaining and viewing income and spending for user
- Creates an interface that is able to aid Students with little prior finacial budgeting experience

Technical Architecture

 - Uses 2 main components in project, backend for maintaining and changing the budget information for spending and income, and a frontend for displaying
 information and allowing user to input new data into application
 
 - Backend: Created using python, primarily using libraries such as Numpy, Pandas, Datetime, and Calender. Consists of a "Person" Class with contains variables 
 for storing data for income and spending (as well as other variables for monitoring relative spending). Includes function for changing income/spending data,
 getting total spending and income, being able to filter data by specific categories, and getting trends for the data based on different time intervals (to then be displayed on the front end.
 
 - Frontend: Created Using Flask (languages of HTML and CSS), allows users to interact with backend by inputing transactions, specifying differetn amounts, and categories. Also allows user to monitor trends of data across various time intervals, as well as categorical breakdowns of data.

