
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Creating a set.


'''
def create_set(noofitems):
    """
    Description:
        This Program will create an set and print it
    Parameter:
        number
    Return 
        None
    """
    DemoSet=set()
    for i in range(noofitems):
        number=int(input("Enter the number to add in set :"))
        DemoSet.add(number)
    print(DemoSet)

def main():
    number=int(input("Enter a length of set"))
    create_set(number)

main()