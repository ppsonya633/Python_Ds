
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Peform union on two sets.


'''
def set_intersection(set1,set2):
    """
    Description:
        This Function will perform union on two sets
    Parameter:
        set,set2:(set)
    Return:
        None
    """
    print(set1|set2)
    return set1|set2

def main():
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    result=set_intersection(set_A,set_B)
    print(result)