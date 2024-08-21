'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for calculating length of string.

'''
def calculate_length(string):
    """
    Description:
        This function will take an string as a input and it will return a length of it
    Parameter:
        string:the string which length we have to calculate
    Return
        it will return a number
    """
    length=0
    for i in string:
        length+=1

    return length

def main():
    string=input("Enter a string for checking a length")
    result=calculate_length(string)
    print(result)

if __name__=="__main__":
    main()