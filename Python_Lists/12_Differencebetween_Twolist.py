'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for Difference between two list.

'''
def differenceBetween_lists(list1,list2):
    """
    Description:
        this program takes an two lists as a input and it will return a list which contains a list1 unique element which not present in list 2
    Parameter:
        list1:contains a list of numbers
        list2:contains a list of 
    Return:
        it returns a difference between list1 and list2
    """
    result=[x for x in list1 if x not in list2]
    return result

def main():
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [4, 5, 6, 7, 8, 9]
    result=differenceBetween_lists(list1,list2)
    print(result)

main()