
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Reverse an order of array



'''
def reverse_array(array):
    """
    Description:
        This function will take an array as a parameter and it will reverse the order of an array
    Perimeter:
        array
    Return:
        array in reverse order 
    """
    for i in range(len(array)-1,-1,-1):
        print(array[i])
    

def main():
    list1=[1,2,3,4,5]
    reverse_array(list1)

main()