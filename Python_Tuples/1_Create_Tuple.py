'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for Creating a tuple.


'''
def create_tuple(length):
    """
    Description:
        This Program will take an length as a input and it will return a tuple
    Parameter:
        length:how many elements we want to include in tuple
    Return:
        tuple:contains tuple of integer numbers
    """
    list1=[]
    for i in range(length):
        number=int(input("Enter a number"))
        list1.append(number)

    return tuple(list1)
    
    

def main():
    n=int(input("Enter a length of tuple"))
    result=create_tuple(n)
    print(result)

if __name__=="__main__":
    main()


