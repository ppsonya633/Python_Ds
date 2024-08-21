'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for getting list of longer numbers.


'''
def check_common(demolist1,demolist2):
    """
    Description:
        This function will take an two lists as a input and it will return true if one of the element is common in this list
    Parameter:
        list1-contains a list of string
        list2-contains a list of string
    Return:
        boolean-return true or false according to the condition
    """
    for item in demolist1:
        if item in demolist2:
            return True
    return False

def main():
    list1=["Apple", "Banana", "Cherry", "Jaguar", "Elderberry"]
    list2=["Fox", "Giraffe", "Horse", "Iguana", "Jaguar"]
    result=check_common(list1,list2)
    print(result)

if __name__=="__main__":
    main()

