'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program to count occurence of substring.

'''
def count_substring(main_string, substring):
    """
    Description:
        This function will take an two string as a input and it will return number of occurence of substring
    Parameter:
        main_string:the string inside the substring to check
        substring:the substring for which occurence have to count
    Return:
        count:no of ocuurence of substring
    """
    return main_string.count(substring)

def main():
    main_string = input("Enter the main string: ")
    substring = input("Enter the substring to count: ")
    result = count_substring(main_string, substring)
    print(f"The substring '{substring}' occurs {result} time(s) in the main string.")

if __name__ == "__main__":
    main()
