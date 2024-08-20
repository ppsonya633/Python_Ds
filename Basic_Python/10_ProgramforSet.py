'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Program To Work on Two sets

'''

def get_colors_list1(color_list_1,color_list_2):
    """
    Description:
        This Program will take two sets as a parameter and will perform substraction operation on them
    Parameter:
        set:color_list_1
        set:color_list_2
    Return:
        None
     """
    print(color_list_1-color_list_2)
    print(color_list_1.difference(color_list_2))

def main():
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    get_colors_list1(color_list_1,color_list_2)

main()

