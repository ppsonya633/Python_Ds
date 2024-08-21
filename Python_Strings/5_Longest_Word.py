'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for getting longest number from list.

'''
def longest_word(list1):
    """
    Description:
        This function will take an list of strings and it will return the longest string
    Parameter:
        list1:list of strings
    Return:
        longest string
    """
    longest=list1[0]
    for item in list1:
        if len(item)>len(longest):
            longest=item
    return longest

def main():
    list1=["PratikPatil","rutikev","somnath","shreyash","Takshashil"]
    result=longest_word(list1)
    print(result)

if __name__=="__main__":
    main()
