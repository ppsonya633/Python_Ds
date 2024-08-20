'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Find Maximum and Minimum value.


'''
def find_max_min(my_set):
    """
    Description:
        This Function will find an maximum and minimum value
    Parameter:
        Set
    Return:
        None
    """
    if not my_set:
        print("The set is empty. Cannot find max or min values.")
        return None, None

    max_value = max(my_set)
    min_value = min(my_set)
    
    return max_value, min_value

def main():
    my_set = {10, 25, 3, 9, 14}
    
    max_val, min_val = find_max_min(my_set)
    
    if max_val is not None and min_val is not None:
        print("Maximum value in the set:", max_val)
        print("Minimum value in the set:", min_val)

main()
