
'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Print The name in reverse order

'''
def printname(firstname,lastname):
    """
    Description:
            
        This function takes the first name and last name as input and prints the name in reverse order.
    
    Parameters:
        firstname : str : first name of the user
        lastname : str : last name of the user
    
    Return:
        None
        
        """

    print(f"{lastname} {firstname}")

def main():
    firstname=input("Enter your first name: ")
    lastname=input("Enter your last name: ")
    printname(firstname,lastname)

main()