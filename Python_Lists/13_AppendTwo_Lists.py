'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for Appending Two Lists.

'''
def append_list(list1,list2):
    """
    Description:
        This Function will take an two lists as a parameter and it will return an appended list
    Parameter:
        list1:list of numbers to append
        list2:list of numbers to append
    Return:
        appended list of list1 and list2
    """
    return list1+list2

def main():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result=append_list(list1,list2)
    print(result)

main()

