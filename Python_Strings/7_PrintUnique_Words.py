'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for Printing unique name.

'''
def unique_words(string):
    """
    Description:
        This function will take an string with separated by ,
    Parameter:
        string of words separated by ,
    Return:
        unique words which separated by comma
    """
    words=[word.strip() for word in string.split(',')]
    
    uniquenames=set()
    listnames=[]
    for word in words:
        if word not in uniquenames:
            uniquenames.add(word)
            listnames.append(word)

    listnames.sort()
    return ', '.join(listnames)


    
def main():
    data=input("Enter a input :")
    result=unique_words(data)
    print(result)

if __name__=="__main__":
    main()

