
#import WFH # type: ignore

# Function to check condition for weekly working hours
"""def total_hours_worked(hours):
    if hours < 30:
        print(
            f"You didn't do enough work in the week {WFH.week_number}. Only {hours} hours !")
    if hours > 40:
        print(f"You are working too hard: {hours} hours")
    elif hours > 30 and hours < 40:
        print("Good Work !")"""


def daily_hours(monday_hours, tuesday_hours, wednesday_hours, thursday_hours, friday_hours):
    if monday_hours < 4:
        print(f"Insufficient hours worked on Monday: {monday_hours} Hours")
    if tuesday_hours < 4:
        print(f"Insufficient hours worked on Tuesday: {tuesday_hours} Hours")
    if wednesday_hours < 4:
        print(
            f"Insufficient hours worked on Wednesday: {wednesday_hours} Hours")
    if thursday_hours < 4:
        print(f"Insufficient hours worked on Thursday: {thursday_hours} Hours")
    if friday_hours < 4:
        print(f"Insufficient hours worked on Friday: {friday_hours} Hours")
    if monday_hours > 10:
        print(f"Too many hours worked on Monday: {monday_hours} hours")
    if tuesday_hours > 10:
        print(f"Too many hours worked on Tuesday: {tuesday_hours} hours")
    if wednesday_hours > 10:
        print(f"Too many hours worked on Wednesday: {wednesday_hours} hours")
    if thursday_hours > 10:
        print(f"Too many hours worked on Thursday: {thursday_hours} hours")
    if friday_hours > 10:
        print(f"Too many hours worked on Friday: {friday_hours} hours")


#total_hours_worked(20)
#daily_hours(2, 3, 5, 6, 11)
