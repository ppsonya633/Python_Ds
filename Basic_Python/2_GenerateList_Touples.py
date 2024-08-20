'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Convert into list and touples

'''

def generate_list_touples(*number):
    """
    Description:
        This function will take the input from the user and convert it into list and touple
    Args:
        sequence of numbers like(1,2,3,4,5)
    return:
        None
    """
    list1=list(number)
    touples=tuple(number)
    print("List: ",str(list1))
    print("Touples: ",str(touples))
    
def main():
    number=input("Enter the numbers separated by comma:")
    #print(number)
    generate_list_touples(number)
main()