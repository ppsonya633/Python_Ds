'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for changing a string.

'''
def change_string(string):
    """
    Description:
        This function will take an string as ainput and it will replace ocuured first character with $
    Parameter:
        string:string which contains a characters
    Return:
        None
    """
    element=string[0]
    new_string=[]
    for item in string:
        if item==element and item in new_string:
            new_string.append("$")
        else:
            new_string.append(item)
    return ''.join(new_string)

def main():
    string=input("Enter an name to change string")
    result=change_string(string)
    print(result)

if __name__=="__main__":
    main()
