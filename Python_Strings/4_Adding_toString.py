'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for adding ing or ly at the end of the string.

'''
def add_ing(string):
    """
    Description:
        This program will take a string as a input and it will add a ing or ly at end of string
    Parameter:
        string:contains a string
    Return:
        string added ing or ly at last
    """
    if len(string)<3:
        return string
    
    if string.endswith("ing"):
        return string+"ly"
    else:
        return string+"ing"
    

def main():
    name=input("Enter an string to add ing or ly")
    result=add_ing(name)
    print(result)

if __name__=="__main__":
    main()