'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for remove duplicate from list.


'''
def remove_duplicate(list1):
    """
    Description:
        This function will take an list as a parameter and it will return unique elements in the list
    Parameter:
        list-list of numbers which can contain duplicate number as well
    Return:
        None
    """
    return list(set(list1))

def main():
    list=[2,3,4,5,3,3,2]
    result=remove_duplicate(list)
    print(result)

if __name__=="__main__":
    main()