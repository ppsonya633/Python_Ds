'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for checking element is exist or not in tuple.

'''
def check_element(sample_tuple,element):
    """
    Description:
        this program will take check the provided element is exists or not in tuple
    Parameter:
        sample_tuple:it contains a tuple with numbers
        element:element to check for exists or not
    Return:
        it return boolean values True or False
    """
    for item in sample_tuple:
        if item==element:
            return True
    return False

def main():
    sample_tuple=(23,54,66,74,789,90)
    result=check_element(sample_tuple,66)
    print(result)

if __name__=="__main__":
    main()

