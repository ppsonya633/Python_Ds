
'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Concatenate List into String

'''
def concatenate_list_data(list):
   
    """
    Discription:
        This function will concatenate the list data into string
    Args:
        list : list : list of elements
    Returns:
        str : concatenated string of list elements
    """
    result=""
    result=result.join(str(e) for e in list)
    return result

def main():
    list=[1,5,8,3]
    print(concatenate_list_data(list))

main()