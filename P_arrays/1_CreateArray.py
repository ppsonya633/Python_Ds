
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Create an array



'''

def Create_Array(length):
    """
    Description:
          This Function Wil take an length as a input how many elements we want to add
    Parameter:
          length(number)
    Return:
          None """
    number=[]
    for i in range(length):
        number.append(int(input(f"Enter an {i+1} element")))
    Print_Array(number)

def Print_Array(number):
    """
    Description:
         This function will take an array as a input and it will Print it
    Parameter:
          number
    Return:
          None
    """
    for i in range(len(number)):
        print(f"{number[i]}")

def main():
    length=int(input("Enter a length of an array"))
    Create_Array(length)

main()
    
