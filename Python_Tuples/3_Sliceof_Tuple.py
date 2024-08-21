'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for slice a tuple.

'''
def tuple_slice(sample_tuple):
    """
    Description:
        This function will take an tuple as a input and it will slice tuple
    Parameter:
        sample_tuple:contains a integer numbers
    Return:
        None
    """
    first_slice=sample_tuple[:5]
    second_slice=sample_tuple[5:]
    print(first_slice)
    print(second_slice)

def main():
    my_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    tuple_slice(my_tuple)

if __name__=="__main__":
    main()