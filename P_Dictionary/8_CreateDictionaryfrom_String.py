'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Creating Dictionary from string.


'''
def createDictionary_fromString(input_string):
    """
    Description:
        This Function will take an input as a string and it will convert that into the dictionary with no of times occurence of keys
    Parameter:
        input_string(str)
    Return:
        None
    """
    dictionary={}
    for char in input_string:
        if char in dictionary:
            dictionary[char]+=1
        else:
            dictionary[char]=1
    print(dictionary)

def main():
    input_string=input("Enter a string to convert into dictionary")
    createDictionary_fromString(input_string)

main()
