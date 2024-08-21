'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Printing Dictionary in table form.


'''
def print_dictionary(dictionary):
    """
    Description:
        This Program will take an dictionary as an input and it will print key value pairs
    Parameter:
        dictionary(dict)
    Return:
        None
    """
    for key,value in dictionary.items():
        print(f"{key} {value}")

def main():
    sample=dict(a=10,b=15,c=35,d=2,e=9)
    print_dictionary(sample)

main()