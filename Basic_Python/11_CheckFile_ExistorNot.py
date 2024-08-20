'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : Check File Exist or not.

'''

import os

def check_file(file_path):

    """
    Description:
       This function will take a path of a file and it will check this file is exists or not in current directory
    Parameter:
       string:file_path 
    Return:
       None
    """
    
    if os.path.exists(file_path):
        print(f"file {file_path} is exists in directory ")
    else:
        print(f"file {file_path} is not exists in directory")


def main():
    file_path=input("Enter a path of file to check")
    check_file(file_path)

main()
