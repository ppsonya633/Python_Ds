'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program to remove duplicate from list.

'''
def remove_duplicates(list_of_lists):
    """
    Description:
        This Program will take an list as a input and it will remove the duplicates from it
    Paramete:
        list:contains a list of integers which contains a duplicate
    Return:
        return a new list of numbers which does not contain duplicate
    """
    seen = set()
    unique_lists = []
    
    for sublist in list_of_lists:
        tuple_sublist = tuple(sublist)
        if tuple_sublist not in seen:
            unique_lists.append(sublist)
            seen.add(tuple_sublist)
    
    return unique_lists

def main():

    sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

    new_list = remove_duplicates(sample_list)
    print("New List:", new_list)

if __name__=="__main__":
    main()