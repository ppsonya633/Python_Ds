'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for convert list into tuples.

'''
def listto_tuple(list1):
    """
    Description:
        this program takes list as a input and it will convert it into tuple
    Parameter:
        list1:list of integer numbers
    Return:
        it will return an tuple
    """
    return tuple(list1)

def main():
    sample_list=[1,2,3,4,5,6]
    result=listto_tuple(sample_list)
    print(result)

if __name__=="__main__":
    main()
