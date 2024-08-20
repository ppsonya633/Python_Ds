
'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Difference Between Two Dates

'''
from datetime import datetime

def difference_betweenDates(date_1,date_2):
    """
    Discription:
        This Function will take atwo date as a parameter and it will returen the total difference between them
    Parameter:
        date_1,date_2: both are string
    Return:
        number"""

    date_format="%y-%m-%d"
    date1=datetime.strptime(date_1,date_format)
    date2=datetime.strptime(date_2,date_format)

    difference=date1-date2

    return abs(difference)

def main():
    date_1=input("Enter the date 1")
    date_2=input("Enter the date 2")
    print(difference_betweenDates(date_1,date_2))

main()