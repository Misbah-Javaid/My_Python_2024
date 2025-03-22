

"""
    Scenario: 

            The current climate has forced many employees to work 
            from home. Diamond Realty, a local real estate agent, has contacted
            you to write a program to help them track the hours worked by their
            seven (7) employees from home. The “Work From Home Tracker” program
            will track the daily hours worked from Monday to Friday, and then 
            calculate the total weekly hours worked for each employee.
            You have met with your client (teacher) and have obtained the project
            specifications for the program you will build as outlined below.
"""

# Number of Employees = 7
# Number of Days worked = 5 days Monday to Friday

import csv  # Module to write in csv file
import comparisons
import sys


def total_hours_worked(hours, week_number):
    if hours < 30:
        print(
            f"You didn't do enough work in the week {week_number}. Only {hours} hours !")
    if hours > 40:
        print(f"You are working too hard: {hours} hours")
    elif hours > 30 and hours < 40:
        print("Good Work !")


hours_worked_each_week = []
total_employees = 7
while True:
    total_weeks = [1,2,3,4]
    week_number = int(input("Please enter current working week number (1,2,3,4): "))
    if week_number not in total_weeks:
        print("Invalid Input")
    else:
        for emp in range(1,8):
            employee_name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
        """monday_hours = int(input("Enter working hours for Monday: "))
        tuesday_hours = int(input("Enter working hours for Tuesday: "))
        wednesday_hours = int(input("Enter working hours for Wednesday: "))
        thursday_hours = int(input("Enter working hours for Thursday: "))
        friday_hours = int(input("Enter working hours for Friday: "))
        print()
        print("****************************************************")
        print(f"Summary for Employee {employee_id}")
        total_hours = monday_hours + tuesday_hours + wednesday_hours + thursday_hours + friday_hours
        comparisons.daily_hours(monday_hours, tuesday_hours, wednesday_hours, thursday_hours, friday_hours)
        print(f"Total hours worked for week {week_number}: {total_hours} hours")
        total_hours_worked(total_hours, week_number)
        print()
        print("****************************************************")
        print()
        print("[Employee 2]")"""

"""

# Writing to csv file 

entry1 = input("name")
entry2 = input("name")
entry3 = input("name")
entry4 = input("name")
entry5 = input("name")
entry6 = input("name")
entry7 = input("name")
entry8 = input("name")

csv_main_header = ["Week Number", "Employee ID", "Employee Name", "Hours worked on Monday", 
              "Hours worked on Tuesday", 
              "Hours worked on Wednesday", "Hours worked on Thursday", "Hours worked on Friday"]

csv_rows = [[entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8]]

# Open the file in write mode using io.open()
with open("Work from Home Hours Tracking.csv", mode = 'w', newline = '') as file:
    # Write content to the file
    csv_writer = csv.writer(file)
    
    csv_writer.writerow(csv_main_header)
    csv_writer.writerows(csv_rows)

csv_weekly_report = ["Weekly Employee Report"]

# Data to write
header = ['Weekly Employee Report']
rows = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Open the file in write mode
with open('output_with_header.txt', mode='w', newline='') as file:
    csv_writer = csv.writer(file)
    
    # Write header
    csv_writer.writerow(header)
    
    # Write the rows
    csv_writer.writerows(rows) """
