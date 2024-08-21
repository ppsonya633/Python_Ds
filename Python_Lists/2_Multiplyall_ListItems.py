
'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for multiplecation of all list elements.


'''
def multiply_listItems(list1):
    """
    Description:
        This Program will take an list as a input and it will return multiplecation of all elements
    Parameter:
        list1-list for iterating through all elements
    Return
        multiplecation of all elements of list
    """
    multiplecation=1
    for number in list1:
        multiplecation*=number
    return multiplecation

def main():
    list1=[1,2,3,4,7,8]
    result=multiply_listItems(list1)
    print(f"Multiplecation of all list elements in {result}")

if __name__=="__main__":
    main()