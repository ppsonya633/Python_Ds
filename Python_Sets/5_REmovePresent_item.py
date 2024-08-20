
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Remove the item from the set.


'''
def remove_item(demoset,item):
    """
    Description:
        This Function will take an item which we want to remove from the set
    Parameter:
        demoset(set),item
    Return:
        None
    """
    if item in demoset:
        demoset.remove(item)
    print(demoset)

def main():
    my_set = {1, 2, 3, 4, 5}
    remove_item(my_set,4)

main()