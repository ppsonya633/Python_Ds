'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for Reversing a tuple.

'''
def reverse_tuple(sample_data):
    """
    Description:
        This function will take an tuple as a input and it will reverse a tuple
    Parameter:
        sample_data:this takes an tuple as a input
    Return:
        return a tuple in reverse order
    """
    store=list(sample_data)
    return tuple(store[::-1])

def main():
    sample_data=(1,2,3,4,5,6,7,8)
    result=reverse_tuple(sample_data)
    print(result)

if __name__=="__main__":
    main()