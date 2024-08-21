'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Python Program for Removing Key From the Dictionary.


'''
def remove_key(dictionary,keytoremove):
    """
    Description:
        This Program will take an dictionary and which key to remove as a parameter and it will remove that key from the dictionary
    Parameter:
        dictionary(dict),keytoremove(int)
    Return:
        None
    """
    for key,values in dictionary.items():
        if key==keytoremove:
            del dictionary[key]
            break
    print(dictionary)

def main():
    sample=dict(p=18,q=21,r=12,s=45)
    
    remove_key(sample,"r")

main()
