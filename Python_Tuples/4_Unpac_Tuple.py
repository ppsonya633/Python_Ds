'''

@Author: Pratik Patil
@Date: 2024-08-21
@Last Modified by: Pratik Patil
@Last Modified time: 2024-08-21
@Title : Python Program for unpacking tuple in different variable.

'''
def unpac_tuple(sample_tuple):
    """
    Description:
        This Program will take an sample tuple as a input and it will unpack in different variable
    Parameter:
        tuple:contains a list of integer numbers
    Return:
        none
    """
    a,b,c,*d=sample_tuple
    print(f"a:{a}")
    print(f"b:{b}")
    print(f"d:{d}")

def main():
    data=(1,2,3,4,5,6,7,8)
    unpac_tuple(data)

if __name__=="__main__":
    main()