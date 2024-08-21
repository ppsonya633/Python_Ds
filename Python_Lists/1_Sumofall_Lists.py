'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for sum of all list elements.


'''
def sumof_list(list1):
    """
    Description:
        This Program will take an list as a input and it will return list of all elements
    Parameter:
        list1-list for iterating through all elements
    Return
        sum of all elements of list
    """
    sum=0
    for number in list1:
        sum+=number
    return sum

def main():
    list1=[1,2,3,4,7,8]
    result=sumof_list(list1)
    print(f"sum of all list elements in {result}")

if __name__=="__main__":
    main()