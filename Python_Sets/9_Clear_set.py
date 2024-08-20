'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Peform for clearing set.


'''
def clear_set(demoset):
    """
    Description:
        This Program will Clear a set
    Parameter:
        set
    Return:
        None
    """
    demoset.clear()
    print(demoset)

def main():
    set_A = {1, 2, 3, 4, 5}
    clear_set(set_A)
main()