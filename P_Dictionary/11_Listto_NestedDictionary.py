'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for converting list to nested dictionary.


'''
def nested_dict(list):
    """
    Description:
        This Program will take an list as a parameter an dit will convert it into nested dictionary
    Parameter:
        list
    Return:
        None
    """
    new_dictionarhy=current={}
    for number in list:
        current[number]={}
        current=current[number]
    print(new_dictionarhy)


def main():
    list=[1,2,3,4,5]
    nested_dict(list)

main()