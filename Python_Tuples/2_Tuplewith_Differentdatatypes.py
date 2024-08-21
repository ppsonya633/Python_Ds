'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for tuple with different data types.


'''
def mixed_tuple(mixed_datatype):
    """
    Description:
        This function return a tuple which contains a different data types
    Parameter:
        take an tuple which contains different data types
    Return:
        tuple with different data types
    """
    
    return mixed_datatype

def main():
    mixed_datatype = (42, 3.14, "Hello, World!", True, [1, 2, 3], {'key': 'value'}, (7, 8, 9))
    result=mixed_tuple(mixed_datatype)
    print(result)

if __name__=="__main__":
    main()