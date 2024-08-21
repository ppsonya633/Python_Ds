'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for getting string in upper case and lower case.

'''
def upper_lower(data):
    """
    Description:
        This Function will take an string as a input and it converts it into upper case and lower case
    Parameter:
        string which we have to convert into upper case and lower case
    Return:
        String included upper case and lower case
    """
    upper=data.upper()
    lower=data.lower()
    return f"Upper: {upper}  Lower: {lower}"

def main():
    name=input("Enter a input")
    result=upper_lower(name)
    print(result)

if __name__=="__main__":
    main()