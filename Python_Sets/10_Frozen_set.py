'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Peform for Frozenset.


'''
def frozenset_operations():
    """
    Description:
        This Program Will Perform Operation on Frozen set
    Parameter:
        None
    Return:
        None
    """
    frozen_set_A = frozenset([1, 2, 3, 4, 5])
    frozen_set_B = frozenset([4, 5, 6, 7, 8])

    print("Frozen Set A:", frozen_set_A)
    print("Frozen Set B:", frozen_set_B)

    union_result = frozen_set_A | frozen_set_B
    print("Union of A and B:", union_result)

    intersection_result = frozen_set_A & frozen_set_B
    print("Intersection of A and B:", intersection_result)

def main():
    frozenset_operations()

main()