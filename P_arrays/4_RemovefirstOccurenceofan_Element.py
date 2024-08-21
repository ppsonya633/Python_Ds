'''

@Author: Pratik Patil
@Date: 2024-08-19
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-19
@Title : Remove First Occurence of an Element.



'''
def removeFirst_Occurence(array1,element):
    """
    Description:
        This Function will take an array and element which we have to remove first occurence
    Parameter:
        array(list of elements),element(int)"""
    for i in array1:
        if i==element:
            array1.remove(i)
            break
    print(array1)


def main():
    array1=[23,34,56,22,43,56,22]
    removeFirst_Occurence(array1,22)

main()

            