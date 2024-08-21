'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program to reverse a string.

'''
def reverse_string(string):
    """
    Description:
        This Program will take a string as a input and it will return the string in reverse order
    Parameter:
        string:string which we have to reverse
    Return:
        string in reverse order
    """
    newlist=[]
    for i in range(len(string),-1,-1):
        newlist.append(i)
    return ''.join(newlist)

def main():
    string=input("Enter a string which have to reverse")
    result=reverse_string(string)
    print(result)

if __name__=="__main__":
    main()
