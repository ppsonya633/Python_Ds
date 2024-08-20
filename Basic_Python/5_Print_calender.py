
'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Print the calender of Given Month

'''
import calendar

def print_calender(year,month):
  
  """
    Discription:
        This function will take the year and month as input and print the calender of that month.
    
    Parameters:
        year : int : year of the calender
        month : int : month of the calender
    
    Returns:
        None
  """
  calendar.prmonth(year,month)

def main():
    year=int(input("Enter the year:"))
    month=int(input("Enter the month"))
    print_calender(year,month)

main()

















