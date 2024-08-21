'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for sorting a list.


'''
def sorted_list(list1):
    """
    Description:
        This program will take an list which inside have a tuples for sorting it
    Parameter:
        list-list which contains touples with two values
    Return:
        None
    """
    return sorted(list1,key=lambda x:x[-1])

def main():
    data=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    result=sorted_list(data)
    print(result)

if __name__=="__main__":
    main()

