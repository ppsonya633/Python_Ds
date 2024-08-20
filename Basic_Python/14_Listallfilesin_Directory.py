'''

@Author: Pratik Patil
@Date: 2024-08-16
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-16
@Title : List all Files in the Directory

'''

import os
def list_files(directory):
    """ This Function Will take an directory name and it will print all the files which are available in that directory.
        Argument:directory(str)
        return:None
    """
    print(os.listdir(directory))

def main():
    directory=input("Enter a directory name for listing a files  :")
    list_files(directory)
main()