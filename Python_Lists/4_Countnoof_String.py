'''

@Author: Pratik Patil
@Date: 2024-08-20
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-20
@Title : Python Program for count string.


'''
def count_string(list1):
    """
    Description:
        Program will give the string whise first and last letter is same
    Parameter:
        list1-list which contains a string
    Return:
        None
    """
    count=0
    for item in list1:
        if item[0]==item[-1]:
            count+=1
    return count

def main():
    Sample=['abc', 'xyz', 'aba', '1221']
    result=count_string(Sample)
    print(f"no of strings are : {result}")

if __name__=="__main__":
    main()

