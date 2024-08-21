'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for count the no of character from string.

'''
def count_characters(string):
    """
    Description:
        This Program will take an string as a input and it will return a dictionary which contains key value pair
    Parameter:
        string:contains a charcters to check their occurence
    Return:
        dictionary which contains char as a key and their occurence as a number
    """
    characterscount={}
    for i in string:
        if i in characterscount:
            characterscount[i]+=1
        else:
            characterscount[i]=1

    return characterscount

def main():
    data=input("Enter a string which character have to count")
    result=count_characters(data)
    print(result)

if __name__=="__main__":
    main()