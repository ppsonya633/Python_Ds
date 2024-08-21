
'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Sort Dictionary in ascending and decending orders.


'''

def sort_dictionary(dictionary):
    """
    Description:
        This Function will take an Dictionary as a parameter and it will sort it according to a values
    Parameter:
        Dictionary(dict)"""
    result=dict(sorted(dictionary.items(),key=lambda x:x[1]))
    return result

def main():
    sample=dict(x=9,y=12,z=10)
    result=sort_dictionary(sample)
    print(result)

main()


