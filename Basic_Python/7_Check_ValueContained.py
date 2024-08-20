'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Check Value is contain or not

'''
list=[1,5,8,3]
def check_value(value):
    """
    Discription:
        This function will check the value in the list
    Args:
        value : int : value to check in the list
    Returns:
        bool : True if value is present in the list else False
    """

    if value in list:
        return True
    else:
        return False
    
def main():
    value=int(input("Enter the value to check:"))
    print(check_value(value))

main()