'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Dictionary Comprehension.


'''
def dictionary_comprehension(n):
    """
    Description:
        This Program will take a number as a input and it will print number as a key and for value it allocate number square
    Parameter:
        number
    Return:
        None
    """
    result={x:x*x for x in range(1,n+1)}
    print(result)

def main():
    number=int(input("Enter a number"))
    dictionary_comprehension(number)

main()
