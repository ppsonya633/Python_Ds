'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for getting part of code from given character.

'''
def get_last_part_before_char(string, char):
    """
    Description:
        This program will take an string and character as a input and it will print remeaning string
    Parameter:
        string:the string is passed
        char:character from that onwards remaining string gets
    Return:
        string till the given character
    """
    part_before, separator, part_after = string.rpartition(char)
    return part_before

def main():
    string = input("Enter a string: ")
    char = input("Enter the character to find the last part before it: ")
    result = get_last_part_before_char(string, char)
    print("The last part of the string before the specified character is:", result)

if __name__ == "__main__":
    main()
