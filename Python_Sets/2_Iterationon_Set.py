'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Iterate on set.


'''
def iterationon_set(set1):
    """
    Description:
        This Program will take an set as a Parameter an it will iterate through it using for loop
    Parameter:
        set
    Return:
        None
    """
    for value in set1:
        print(value)

def main():
    demoset={3,4,5,6,7,8}
    iterationon_set(demoset)

main()