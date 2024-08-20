'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Printing unique values from list of dictionaries.


'''
def print_UniqueValues(dictionary):
    """
    Description:
        This program will take a list which contais a dictionaries with key value pairs and it will print the unique values
    Parameter:
        list
    Return:
        None
    """
    result=[]
    for item in dictionary:
        result.append(list(item.values())[0])
    print(set(result))

def main():
    Data=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    print_UniqueValues(Data)

main()
