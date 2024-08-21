'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for getting list of longer numbers.


'''
def longer_words(listdata,n):
    """
    Description:
        This Program will take an list and the length of string as input and it will return new list of strings
    Parameter:
        list-takes a list of strings
    Return:
        new list of strings whose length is greater than n"""
    new_list=[]
    for item in listdata:
        if len(item)>n:
            new_list.append(item)
    return new_list

def main():
    names=["Pratik","Prafull","Patil","gbrhhrhrgrtg","grtgrbbfg"]
    n=int(input("Enter a length of string"))
    result=longer_words(names,n)
    print(result)

if __name__=="__main__":
    main()

