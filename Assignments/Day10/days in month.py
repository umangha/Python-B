# Lesson 24 Day 10 - Days in Month

# Takes year and return True or False
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        # print("Leap year")
        return True
      else:
            # print("Not leap year")
            return False
    else:
        # print("Leap year")
        return True
  else:
        # print("Not leap year")
        return False
  
# TODO: Add more code here 

# Main working function to calculate days in a month
def days_in_month(year,month):
    """Takes Year and Month and return the number of days in the month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year):
        month_days[1]=29

    # Month is starting as Jan=1. Feb=2
    no_of_days=month_days[month-1]
    return no_of_days


  
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)

