'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for Removing list elements at given indexes.


'''
def remove_element(list1,list2):
    """
    Description:
        This function will take two list as a parameter one contains a items and another one contains indexes
    Parameter:
        list1-it contains a list of elements
        list2-it contains a list of indexes which we have to remove
    Return:
        return the modified list
    """
    for index in list2:
        list1.remove(list1[index])
    return list1

def main():
    data= ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    indexes=[0,4,5]
    indexes.sort(reverse=True)
    result=remove_element(data,indexes)
    print(result)

if __name__=="__main__":
    main()


