'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for Displaying formatted output.

'''
import textwrap

def format_text(text, width=50):
    """
    Description:
        This function will take text and width as a input and it will return formatted string
    Parameter:
        text:large number of character string
    Return:
        it returns a formatted string
    """
    return textwrap.fill(text, width=width)

def main():
    text = (
        "Python is an interpreted, high-level, general-purpose programming language. "
        "Created by Guido van Rossum and first released in 1991, Python's design philosophy "
        "emphasizes code readability with its notable use of significant whitespace."
    )
    
    formatted_text = format_text(text)
    print("Formatted Text:\n")
    print(formatted_text)

if __name__ == "__main__":
    main()
