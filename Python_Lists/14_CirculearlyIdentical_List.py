'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program to check lists are circurley identical or not.

'''
def are_circularly_identical(list1, list2):
    """
    Description:
        This program will take two lists as a parameter and it will return true or false
    Parameter:
        list1:list1 contains a integer numbers
        list2:list2 contains a rotated list
    Return:
        it will return boolean values True or False
    """
    if len(list1) != len(list2):
        return False

    combined = list1 + list1

    return any(list2 == combined[i:i+len(list2)] for i in range(len(list1)))

def main():

    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 1, 15]

    if are_circularly_identical(list1, list2):
        print("The lists are circularly identical.")
    else:
        print("The lists are not circularly identical.")

if __name__=="__main__":
    main()

