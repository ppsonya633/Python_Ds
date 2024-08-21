'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for get Repeated numbers in tuple.

'''
def repeated_items(sample):
    """
    Description:
        This Program will take an tuple is a input and it will return the list of elements which are duplicate in tuple
    Parameter:
        tuple:contains a integer numbers
    Return:
        list of items which duplicated in tuple
    """
    repeated=[]
    for i in sample:
        if i in sample[i+1:]:
            if i not in repeated:
                repeated.append(i)

    return repeated

def main():
    sample=(1,2,3,4,2,1)
    result=repeated_items(sample)
    print(result)

if __name__=="__main__":
    main()

