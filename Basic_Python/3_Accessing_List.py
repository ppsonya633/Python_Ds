
'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Accessing The List index

'''


def getFirstandLast_element(list):
    """
    Description:
        This Function will take list as a parameter and it will print the First and Last element from the list
    Parameter:
        list[]:list of the strings
    Return:
        None
    """

    print(f"{list[0]} {list[-1]}")


def main():
    color_list=["Red","Green","Whitr","Black"]
    getFirstandLast_element(color_list)

main()