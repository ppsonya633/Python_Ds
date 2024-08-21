'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for Cloning or copying a list.


'''
def clone_list(list1):
    """
    Description:
        This function will take a list and it will copy into a another variable
    Parameter:
        list1-list of numbers
    Return:
        None
    """
    list2=list1.copy()
    return list2

def main():
    list1=[4,3,6,7,88]
    result=clone_list(list1)
    print(result)

if __name__=="__main__":
    main()