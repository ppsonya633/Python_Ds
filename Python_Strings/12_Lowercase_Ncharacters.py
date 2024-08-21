'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program to Lowercase n character.

'''
def lowercase_first_n_chars(s, n):
    """
    Description:
        This Program will take an string and number as a character and it will make string lowercase till n character
    Parameter:
        string string contains a character
        n contains a number
    Return
        it will return a new string in which the first n character will be in lower case
    """
    if n > len(s):
        n = len(s)
    
    return s[:n].lower() + s[n:]

def main():
    input_string = "HELLO World"
    n = 5
    result = lowercase_first_n_chars(input_string, n)
    print(result) 


 

    

    