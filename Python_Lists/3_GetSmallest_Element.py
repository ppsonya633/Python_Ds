'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for get smallest element from the list.


'''
def get_smallest(list1):
    """
    Description:
        This program will gave an smallest element in the list
    Parameter:
        list-list which contains the integer numbers
    Return:
        None
    """
    smallest=list1[0]
    for number in list1:
        if number<smallest:
            smallest=number
    return smallest

def main():
    list1=[45,87,5,15,35]
    result=get_smallest(list1)
    print(f"smallest element in the list is {result}")

if __name__=="__main__":
    main()