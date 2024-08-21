'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for removing element from tuple.

'''
def remove_item(sample_tuple,element):
    """
    Description:
        This program removes a given element from tuple and it will return new tuple
    Parameter:
        sample_tuple:contains a number of integer element
    Return:
        tuple which removed the provided element
    """
    new_list=[]
    for item in list(sample_tuple):
        if element !=item:
            new_list.append(item)
    return tuple(new_list)

def main():
    sample_tuple=(12,34,56,77,88,66)
    result=remove_item(sample_tuple,66)
    print(result)

if __name__=="__main__":
    main()


