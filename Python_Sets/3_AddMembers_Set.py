'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Add a Members into set.


'''
def add_members(set1,element):
    """
    Description:
        This Program will add a member into set
    Parameter:
        set
    Return:
        None
    """
    set1.add(element)

    print(set1)

def main():
    data={2,3,4,5,6,7}
    add_members(data,16)

main()
