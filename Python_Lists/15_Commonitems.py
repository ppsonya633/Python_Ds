'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program to check common items in the list.

'''
def find_common_items(list1, list2):
    """
    Description:
        This Program will take two lists as a parameter and it will return a new list which contains common item of both lists
    Parameter:
        list1:contains a number of integers
        list2:contains a number of integers
    Return:
        return a new list which contains a same element from list 1 and list 2
    """
    common_items = set(list1) & set(list2)
    
    return list(common_items)

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]

    common_items = find_common_items(list1, list2)
    print("Common items:", common_items)

if __name__=="__main__":
    main()
