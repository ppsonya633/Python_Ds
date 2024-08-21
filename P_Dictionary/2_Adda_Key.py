'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for adding key to dictionary.


'''
def add_key(dictionary,key,value):
    """
    Description:
        This Program will take an key and value and it will add it into a dictionary
    Parameter:
        dictionary(dict),key(str),value(int)
    Return:
        None
    """
    dictionary.update()
    print(dictionary)

def main():
    sample=dict(pratik=22,niru=16,harshu=18,samarth=14)
    add_key(sample,"vivan",10)

main()
