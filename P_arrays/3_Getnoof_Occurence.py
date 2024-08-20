'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Get no of occurence of element



'''
def getnoofOccurenceof_element(array,element):
    """
    Description:
       This Function will take an array and element which have to check the occurence
    Parameter:
       array,element
    Return:
       none
    """
    count=0
    for i in array:
        if i==element:
            count+=1
    print(f"The occurence of {element} is appear {count} times")

def main():
    numbers=[3,4,5,6,4,4]
    getnoofOccurenceof_element(numbers,5)

main()
    

